document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("flower-effect");

  if (!container) return;

  function createFlower() {
    const flower = document.createElement("div");
    flower.classList.add("flower");

    flower.style.left = Math.random() * 100 + "vw";
    flower.style.animationDuration = 3 + Math.random() * 2 + "s";

    container.appendChild(flower);

    setTimeout(() => flower.remove(), 5000);
  }

  setInterval(createFlower, 300);
});
