import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "EvoWorth",
  description: "EvoWorth compares evolving financial value with a clean web and API foundation.",
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

