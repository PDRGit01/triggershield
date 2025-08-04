TriggerShield Chrome Extension

This folder contains the Chrome Extension logic for TriggerShield. It detects emotionally triggering content in real time and blurs it before the user sees it.

🔹 Files
    •	manifest.json — Extension metadata and permissions
    •	content.js — Main script that scans webpages for keywords/images
    •	background.js — (Optional) Can be used for persistent actions or messaging
    •	triggershield.css — Styles for blurred images and warning overlays

🔄 Functionality
    1.	Scans all visible content
    2.	Matches alt/title/text against trigger keywords
    3.	Sends images to local server for AI prediction
    4.	Blurs content if it's likely to be a trigger
    5.	Adds overlay: "Blurred by TriggerShield"

🔺 To Edit Trigger Keywords
    Currently located in content.js as a list under triggerWords. These can be updated or expanded.
