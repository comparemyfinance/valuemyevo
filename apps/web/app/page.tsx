const apiBaseUrl =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export default function HomePage() {
  return (
    <main className="page-shell">
      <section className="hero">
        <p className="eyebrow">EvoWorth</p>
        <h1>Track value with a foundation built to grow.</h1>
        <p className="lede">
          This monorepo starts with a clean Next.js frontend, a FastAPI backend,
          and the minimum structure needed to move quickly without accumulating
          noise.
        </p>
        <div className="actions">
          <a href={apiBaseUrl} target="_blank" rel="noreferrer">
            View API
          </a>
          <a href={`${apiBaseUrl}/health`} target="_blank" rel="noreferrer">
            Check health
          </a>
        </div>
      </section>
    </main>
  );
}

