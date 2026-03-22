export interface WebRuntimeConfig {
  apiBaseUrl: string;
}

export function getWebRuntimeConfig(): WebRuntimeConfig {
  return {
    apiBaseUrl: process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000",
  };
}

