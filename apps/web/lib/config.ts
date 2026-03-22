export interface WebRuntimeConfig {
  apiBaseUrl: string;
}

export function getWebRuntimeConfig(): WebRuntimeConfig {
  return {
    apiBaseUrl: normalizeApiBaseUrl(process.env.NEXT_PUBLIC_API_BASE_URL),
  };
}

function normalizeApiBaseUrl(rawApiBaseUrl: string | undefined): string {
  const normalizedApiBaseUrl = rawApiBaseUrl?.trim() || "http://localhost:8000";
  return normalizedApiBaseUrl.replace(/\/+$/, "");
}

