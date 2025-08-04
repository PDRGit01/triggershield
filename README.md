TriggerShield 🛡️
TriggerShield is an AI-powered Chrome Extension designed to protect users from emotionally triggering images or thumbnails while browsing the internet. It can blur images using both keyword-based text scanning and visual recognition with a trained machine learning model.
________________________________________
🌐 How It Works
TriggerShield scans webpages in real time. If an image or video is identified (via tags or image classifier) as a trigger, it is blurred with an optional overlay warning. The system works even if alt text or labels are missing.
•	Chrome Extension detects and blurs content on Facebook, YouTube, and other websites.
•	Local inference server uses a trained PyTorch model to classify user-defined image triggers (e.g., pineapple, cupcake).
________________________________________
📂 Project Structure
TriggerShield/
├── .git/                      # Git versioning
├── extension/                 # Chrome Extension source code
├── model-training/            # Training scripts + AI model
├── web-ui/                    # Flask web interface & backend server
│   └── inference_server.py    # Backend server for live predictions
├── image_predictor.py         # Standalone inference script
└── README.md                  # You're reading it!
________________________________________
⚡ How to Run It Locally
Step 1: Run the Inference Server
cd web-ui
python inference_server.py
   • Make sure Python 3.13+ and required packages (torch, torchvision, flask, flask_cors) are installed
   • Model file image_model.pt should exist in the model-training/ folder and be referenced accordingly

Step 2: Load the Chrome Extension
1.	Go to chrome://extensions
2.	Enable Developer Mode
3.	Click Load Unpacked and select the extension/ folder
4.	Extension will activate on all webpages

Step 3: Test
Visit any page with images. If content matches the trigger via text or visual, it will be blurred.
This MVP only works on "pineapple" and "cupcake" as trigger words.
________________________________________
🌍 Live Demos
•	Web UI: http://127.0.0.1:5001
•	Extension auto-runs on browser pages
________________________________________
🔧 Tech Stack
•	Python, PyTorch, Flask
•	HTML, CSS, JavaScript (Chrome Extension)
•	ResNet18-based classifier
________________________________________
✅ Contributors
•	Pratyusha Dutta Ray (375893)
•	Saikat Basu (124427)
________________________________________
🚀 Future Scope
•	Frame-based video blurring
•	Cross-platform (Firefox, mobile)
•	User control panel (toggle, keyword editor)
