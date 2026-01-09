import { CONFIG } from "./config.js";

export async function fetchAPI(endpoint) {
  try {
    const response = await fetch(`${CONFIG.API_BASE_URL}${endpoint}`);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error("API fetch failed:", error);
    throw error;
  }
}
