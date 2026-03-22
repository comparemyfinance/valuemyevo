import { getWebRuntimeConfig } from "../lib/config";
import { landingPageContent } from "../lib/content";
import { EvoLandingPage } from "./valuation-landing";

export default function HomePage() {
  const { apiBaseUrl } = getWebRuntimeConfig();

  return (
    <EvoLandingPage
      apiBaseUrl={apiBaseUrl}
      content={landingPageContent}
    />
  );
}

