import { fetchAPI } from "./api.js";

async function loadClubs() {
  const container = document.getElementById("clubs");

  try {
    const clubs = await fetchAPI("/clubs/");

    if (clubs.length === 0) {
      container.innerHTML = "<p>No clubs available.</p>";
      return;
    }

    clubs.forEach(club => {
      const card = document.createElement("div");
      card.className = "club-card";

      card.innerHTML = `
        ${club.cover_image ? `<img src="${club.cover_image}" alt="${club.name}">` : ""}
        <h3>${club.name}</h3>
        <p>${club.description}</p>
      `;

      container.appendChild(card);
    });

  } catch (err) {
    container.innerHTML = "<p>Failed to load clubs.</p>";
  }
}

loadClubs();
