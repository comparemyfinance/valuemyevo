export interface LandingPageContent {
  productName: string;
  headline: string;
  description: string;
  healthLinkLabel: string;
}

export const landingPageContent: LandingPageContent = {
  productName: "EvoWorth",
  headline: "Price your evolved card with a cleaner valuation workflow.",
  description:
    "Enter the card profile, submit it to the valuation API, and review the estimated price, confidence, sources, and comparables in one place.",
  healthLinkLabel: "API health",
};
