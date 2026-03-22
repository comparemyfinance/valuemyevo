import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "EvoWorth",
  description: "Minimal landing page for submitting evolved FC card inputs and rendering valuation API responses.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

