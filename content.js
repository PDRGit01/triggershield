console.log("🛡️ TriggerShield loaded");

const triggerWords = ["pineapple", "cupcake", "unicorn", "rainbow"];

function blurIfTriggered(img) {
  const text = (img.alt + " " + img.title + " " + img.getAttribute("aria-label")).toLowerCase();
  if (triggerWords.some(word => text.includes(word))) {
    img.style.filter = "blur(10px)";
    img.setAttribute("data-triggershield", "true");
  }
}

function scanImages() {
  const images = document.querySelectorAll("img");
  images.forEach(blurIfTriggered);
}

window.addEventListener("load", () => setTimeout(scanImages, 500));
