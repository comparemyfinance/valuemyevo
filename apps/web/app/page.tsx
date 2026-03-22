import { getWebRuntimeConfig } from "../lib/config";
import { EvoLandingPage } from "./valuation-landing";

export default function HomePage() {
  const { apiBaseUrl } = getWebRuntimeConfig();

  return <EvoLandingPage apiBaseUrl={apiBaseUrl} />;
}

