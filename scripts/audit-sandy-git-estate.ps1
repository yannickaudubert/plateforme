[CmdletBinding()]
param(
    [string[]]$Roots = @('C:\GitHub', 'C:\first', 'C:\SIIAOS'),
    [string]$OutputDirectory = '.\reports\git-estate',
    [int]$MaxDepth = 8
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-GitReadOnly {
    param(
        [Parameter(Mandatory = $true)][string]$RepoPath,
        [Parameter(Mandatory = $true)][string[]]$Arguments,
        [switch]$AllowFailure
    )

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = 'git'
    $psi.WorkingDirectory = $RepoPath
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.CreateNoWindow = $true
    foreach ($argument in $Arguments) {
        [void]$psi.ArgumentList.Add($argument)
    }

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $psi
    [void]$process.Start()
    $stdout = $process.StandardOutput.ReadToEnd()
    $stderr = $process.StandardError.ReadToEnd()
    $process.WaitForExit()

    if ($process.ExitCode -ne 0 -and -not $AllowFailure) {
        throw "git $($Arguments -join ' ') failed in $RepoPath : $stderr"
    }

    [pscustomobject]@{
        ExitCode = $process.ExitCode
        StdOut = $stdout.TrimEnd()
        StdErr = $stderr.TrimEnd()
    }
}

function Invoke-GitReadOnlyPs51 {
    param(
        [Parameter(Mandatory = $true)][string]$RepoPath,
        [Parameter(Mandatory = $true)][string[]]$Arguments,
        [switch]$AllowFailure
    )

    $escaped = foreach ($argument in $Arguments) {
        '"' + ($argument -replace '"', '\"') + '"'
    }
    $commandLine = 'git ' + ($escaped -join ' ')
    $output = & cmd.exe /d /s /c $commandLine 2>&1
    $exitCode = $LASTEXITCODE
    $text = ($output | ForEach-Object { $_.ToString() }) -join [Environment]::NewLine

    if ($exitCode -ne 0 -and -not $AllowFailure) {
        throw "$commandLine failed in $RepoPath : $text"
    }

    [pscustomobject]@{
        ExitCode = $exitCode
        StdOut = $text.TrimEnd()
        StdErr = if ($exitCode -ne 0) { $text.TrimEnd() } else { '' }
    }
}

function Git {
    param(
        [Parameter(Mandatory = $true)][string]$RepoPath,
        [Parameter(Mandatory = $true)][string[]]$Arguments,
        [switch]$AllowFailure
    )

    Push-Location $RepoPath
    try {
        if ($PSVersionTable.PSVersion.Major -ge 7) {
            return Invoke-GitReadOnly -RepoPath $RepoPath -Arguments $Arguments -AllowFailure:$AllowFailure
        }
        return Invoke-GitReadOnlyPs51 -RepoPath $RepoPath -Arguments $Arguments -AllowFailure:$AllowFailure
    }
    finally {
        Pop-Location
    }
}

function Get-RepositoryRoots {
    param([string[]]$SearchRoots, [int]$Depth)

    $found = New-Object System.Collections.Generic.HashSet[string]([System.StringComparer]::OrdinalIgnoreCase)

    foreach ($searchRoot in $SearchRoots) {
        if (-not (Test-Path -LiteralPath $searchRoot -PathType Container)) {
            continue
        }

        $rootFull = (Resolve-Path -LiteralPath $searchRoot).Path
        $queue = New-Object System.Collections.Generic.Queue[object]
        $queue.Enqueue([pscustomobject]@{ Path = $rootFull; Depth = 0 })

        while ($queue.Count -gt 0) {
            $item = $queue.Dequeue()
            $path = $item.Path
            $currentDepth = [int]$item.Depth

            if (Test-Path -LiteralPath (Join-Path $path '.git')) {
                $probe = Git -RepoPath $path -Arguments @('rev-parse', '--show-toplevel') -AllowFailure
                if ($probe.ExitCode -eq 0 -and $probe.StdOut) {
                    [void]$found.Add($probe.StdOut)
                }
                continue
            }

            if ($currentDepth -ge $Depth) {
                continue
            }

            try {
                $children = Get-ChildItem -LiteralPath $path -Directory -Force -ErrorAction Stop |
                    Where-Object { $_.Name -notin @('.git', 'node_modules', '.next', '.venv', 'venv', '__pycache__', 'dist', 'build', 'target', '.cache') }
                foreach ($child in $children) {
                    $queue.Enqueue([pscustomobject]@{ Path = $child.FullName; Depth = $currentDepth + 1 })
                }
            }
            catch {
                # Access errors are evidence too, but do not stop the estate scan.
            }
        }
    }

    return @($found | Sort-Object)
}

function Get-RepoRecord {
    param([Parameter(Mandatory = $true)][string]$RepoPath)

    $head = Git -RepoPath $RepoPath -Arguments @('rev-parse', 'HEAD') -AllowFailure
    $branch = Git -RepoPath $RepoPath -Arguments @('branch', '--show-current') -AllowFailure
    $status = Git -RepoPath $RepoPath -Arguments @('status', '--porcelain=v1', '--branch') -AllowFailure
    $remotes = Git -RepoPath $RepoPath -Arguments @('remote', '-v') -AllowFailure
    $worktrees = Git -RepoPath $RepoPath -Arguments @('worktree', 'list', '--porcelain') -AllowFailure
    $lastCommit = Git -RepoPath $RepoPath -Arguments @('log', '-1', '--date=iso-strict', '--format=%H%x09%aI%x09%an%x09%s') -AllowFailure
    $upstream = Git -RepoPath $RepoPath -Arguments @('rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{upstream}') -AllowFailure
    $submodules = Git -RepoPath $RepoPath -Arguments @('submodule', 'status', '--recursive') -AllowFailure
    $countObjects = Git -RepoPath $RepoPath -Arguments @('count-objects', '-vH') -AllowFailure

    $ahead = $null
    $behind = $null
    if ($upstream.ExitCode -eq 0 -and $upstream.StdOut) {
        $counts = Git -RepoPath $RepoPath -Arguments @('rev-list', '--left-right', '--count', "HEAD...$($upstream.StdOut)") -AllowFailure
        if ($counts.ExitCode -eq 0 -and $counts.StdOut -match '^\s*(\d+)\s+(\d+)\s*$') {
            $ahead = [int]$Matches[1]
            $behind = [int]$Matches[2]
        }
    }

    $remoteRows = @()
    if ($remotes.StdOut) {
        foreach ($line in ($remotes.StdOut -split "`r?`n")) {
            if ($line -match '^(\S+)\s+(\S+)\s+\((fetch|push)\)$') {
                $remoteRows += [pscustomobject]@{
                    Name = $Matches[1]
                    Url = $Matches[2]
                    Direction = $Matches[3]
                }
            }
        }
    }

    $statusLines = if ($status.StdOut) { @($status.StdOut -split "`r?`n") } else { @() }
    $worktreeLines = if ($worktrees.StdOut) { @($worktrees.StdOut -split "`r?`n") } else { @() }
    $submoduleLines = if ($submodules.StdOut) { @($submodules.StdOut -split "`r?`n") } else { @() }

    $dirtyLines = @($statusLines | Where-Object { $_ -notmatch '^## ' -and $_.Trim() })
    $last = $null
    if ($lastCommit.ExitCode -eq 0 -and $lastCommit.StdOut) {
        $parts = $lastCommit.StdOut -split "`t", 4
        if ($parts.Count -eq 4) {
            $last = [pscustomobject]@{ Sha = $parts[0]; Date = $parts[1]; Author = $parts[2]; Subject = $parts[3] }
        }
    }

    [pscustomobject]@{
        observed_at = (Get-Date).ToString('o')
        machine = $env:COMPUTERNAME
        path = $RepoPath
        repo_name = Split-Path -Leaf $RepoPath
        head_sha = if ($head.ExitCode -eq 0) { $head.StdOut } else { $null }
        branch = if ($branch.ExitCode -eq 0 -and $branch.StdOut) { $branch.StdOut } else { $null }
        detached_head = ($branch.ExitCode -eq 0 -and -not $branch.StdOut)
        upstream = if ($upstream.ExitCode -eq 0) { $upstream.StdOut } else { $null }
        ahead = $ahead
        behind = $behind
        dirty = ($dirtyLines.Count -gt 0)
        dirty_entry_count = $dirtyLines.Count
        status = $statusLines
        remotes = $remoteRows
        worktree_count = @($worktreeLines | Where-Object { $_ -like 'worktree *' }).Count
        worktrees = $worktreeLines
        submodules = $submoduleLines
        last_commit = $last
        object_store = $countObjects.StdOut
        remote_live_probe = 'NOT_RUN'
        runtime_service_probe = 'NOT_RUN'
        evidence_state = 'OBSERVED_LOCAL_READ_ONLY'
        notes = @(
            'No fetch/pull/push/reset/checkout/clean/prune was executed.',
            'Ahead/behind uses only the already-present local upstream tracking ref.',
            'Remote reachability and service runtime are intentionally not asserted.'
        )
    }
}

$startedAt = Get-Date
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputDirectory)
New-Item -ItemType Directory -Path $resolvedOutput -Force | Out-Null

$repoRoots = Get-RepositoryRoots -SearchRoots $Roots -Depth $MaxDepth
$records = @()
foreach ($repoRoot in $repoRoots) {
    try {
        $records += Get-RepoRecord -RepoPath $repoRoot
    }
    catch {
        $records += [pscustomobject]@{
            observed_at = (Get-Date).ToString('o')
            machine = $env:COMPUTERNAME
            path = $repoRoot
            repo_name = Split-Path -Leaf $repoRoot
            evidence_state = 'OBSERVATION_ERROR'
            error = $_.Exception.Message
        }
    }
}

$manifest = [pscustomobject]@{
    schema = 'siiaos.git-estate-observation.v1'
    mode = 'READ_ONLY'
    started_at = $startedAt.ToString('o')
    completed_at = (Get-Date).ToString('o')
    machine = $env:COMPUTERNAME
    roots = $Roots
    max_depth = $MaxDepth
    repository_count = $records.Count
    repositories = $records
}

$jsonPath = Join-Path $resolvedOutput 'repo_inventory.json'
$csvPath = Join-Path $resolvedOutput 'repo_inventory.csv'
$markdownPath = Join-Path $resolvedOutput 'repo_inventory.md'

$manifest | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $jsonPath -Encoding UTF8

$records | Select-Object repo_name,path,branch,head_sha,upstream,ahead,behind,dirty,dirty_entry_count,worktree_count,evidence_state,@{n='fetch_remotes';e={($_.remotes | Where-Object Direction -eq 'fetch' | ForEach-Object Url) -join ';'}},@{n='last_commit_date';e={$_.last_commit.Date}},@{n='last_commit_subject';e={$_.last_commit.Subject}} |
    Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding UTF8

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add('# SandY Git Estate Observation')
$lines.Add('')
$lines.Add("- Mode: `READ_ONLY`")
$lines.Add("- Machine: `$($env:COMPUTERNAME)`")
$lines.Add("- Observed: `$((Get-Date).ToString('o'))`")
$lines.Add("- Repositories: `$($records.Count)`")
$lines.Add('')
$lines.Add('| Repo | Path | Branch | Upstream | Ahead | Behind | Dirty | Worktrees | State |')
$lines.Add('|---|---|---|---|---:|---:|---|---:|---|')
foreach ($record in $records) {
    $lines.Add("| $($record.repo_name) | `$($record.path)` | $($record.branch) | $($record.upstream) | $($record.ahead) | $($record.behind) | $($record.dirty) | $($record.worktree_count) | $($record.evidence_state) |")
}
$lines.Add('')
$lines.Add('> This report does not prove remote reachability, deployed service state, or that a tracked remote is canonical. It only records local Git facts available without mutation.')
$lines | Set-Content -LiteralPath $markdownPath -Encoding UTF8

Write-Host "SIIAOS Git estate observation complete."
Write-Host "JSON: $jsonPath"
Write-Host "CSV:  $csvPath"
Write-Host "MD:   $markdownPath"
