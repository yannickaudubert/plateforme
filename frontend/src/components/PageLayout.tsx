import { ReactNode } from "react";

interface PageLayoutProps {
  title: string;
  description: string;
  children?: ReactNode;
}

export function PageLayout({ title, description, children }: PageLayoutProps) {
  return (
    <section className="page">
      <header className="page-header">
        <h2>{title}</h2>
        <p>{description}</p>
      </header>
      {children}
    </section>
  );
}
