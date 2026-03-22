export interface LandingPageContent {
  productName: string;
  headline: string;
  description: string;
  apiLinkLabel: string;
  healthLinkLabel: string;
}

export const landingPageContent: LandingPageContent = {
  productName: "EvoWorth",
  headline: "Track value with a foundation built to grow.",
  description:
    "This monorepo starts with a clean Next.js frontend, a FastAPI backend, and the minimum structure needed to move quickly without accumulating noise.",
  apiLinkLabel: "View API",
  healthLinkLabel: "Check health",
};
