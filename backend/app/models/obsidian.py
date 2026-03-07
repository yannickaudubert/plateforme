from pydantic import BaseModel, Field


class ObsidianNoteContent(BaseModel):
    path: str
    content: str
    frontmatter: dict[str, str]
    bytes_size: int
    modified_at: str


class ObsidianCreateNoteRequest(BaseModel):
    path: str = Field(min_length=1, max_length=500)
    content: str = ""
    create_parents: bool = True


class ObsidianUpdateNoteRequest(BaseModel):
    path: str = Field(min_length=1, max_length=500)
    content: str
    expected_modified_at: str | None = None
    create_backup: bool = True


class ObsidianWriteResponse(BaseModel):
    path: str
    status: str
    bytes_written: int
    modified_at: str
