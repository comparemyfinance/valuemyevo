import { landingPageContent } from "../lib/content";
import { getWebRuntimeConfig } from "../lib/config";

export default function HomePage() {
  const { apiBaseUrl } = getWebRuntimeConfig();

  return (
    <main className="page-shell">
      <section className="hero">
        <p className="eyebrow">{landingPageContent.productName}</p>
        <h1>{landingPageContent.headline}</h1>
        <p className="lede">
          {landingPageContent.description}
        </p>
        <div className="actions">
          <a href={apiBaseUrl} target="_blank" rel="noreferrer">
            {landingPageContent.apiLinkLabel}
          </a>
          <a href={`${apiBaseUrl}/health`} target="_blank" rel="noreferrer">
            {landingPageContent.healthLinkLabel}
          </a>
        </div>
      </section>
    </main>
  );
}

