console.log("🛡️ TriggerShield extension loaded.");

const TRIGGER_WORDS = ["pineapple", "cupcake"];

// Normalize and fuzzy match (e.g., "cupcakes", "CupCake")
function matchesTrigger(text) {
  const clean = text.toLowerCase().replace(/[^a-z]/g, "");
  return TRIGGER_WORDS.some(trigger => clean.includes(trigger));
}

function blurElement(el) {
  if (el.classList.contains("triggershield-blurred")) return;

  el.style.filter = "blur(12px)";
  el.style.transition = "filter 0.4s";
  el.classList.add("triggershield-blurred");

  const label = document.createElement("div");
  label.innerText = "🔒 Blurred by TriggerShield";
  label.style.position = "absolute";
  label.style.bottom = "4px";
  label.style.left = "4px";
  label.style.padding = "2px 6px";
  label.style.background = "rgba(0, 0, 0, 0.7)";
  label.style.color = "#fff";
  label.style.fontSize = "12px";
  label.style.borderRadius = "4px";
  label.style.zIndex = "9999";
  label.className = "triggershield-label";

  el.style.position = "relative";
  el.parentElement?.appendChild(label);
}

// Check alt/title/aria
function checkImageText(el) {
  const attrs = [
    el.alt || "",
    el.title || "",
    el.getAttribute("aria-label") || "",
    el.getAttribute("data-testid") || "",
    el.getAttribute("aria-describedby") || "",
  ].join(" ");

  return matchesTrigger(attrs);
}

// For YouTube and FB posts – scan nearby text
function scanSurroundingText(el) {
  const parent = el.closest("ytd-video-renderer, ytd-rich-item-renderer, .userContentWrapper, div[role='article']");
  if (!parent) return false;

  const textContent = parent.innerText || "";
  return matchesTrigger(textContent);
}

// Blur logic
function processImage(el) {
  if (!el || el.tagName !== "IMG") return;
  const src = el.src || "";

  // Check if it's SVG or base64 but continue processing
  if (src.includes("svg+xml") || src.startsWith("data:image")) {
    console.warn("⚠️ Special format detected (SVG/base64):", src);
    // Proceed with text-based check
    if (checkImageText(el) || scanSurroundingText(el)) {
      console.log("🔍 Match found in SVG/base64 image:", el);
      blurElement(el);
    }
    return;
  }

  // Normal image check
  if (checkImageText(el) || scanSurroundingText(el)) {
    console.log("🔍 Match found (text):", el);
    blurElement(el);
  }
}


// Initial + periodic scan
function scanAllImages() {
  document.querySelectorAll("img:not(.triggershield-blurred)").forEach(processImage);
}

scanAllImages();
setInterval(scanAllImages, 3000);
