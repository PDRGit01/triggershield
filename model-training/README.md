TriggerShield - AI Image Classifier

This folder contains code to train and store the machine learning model that identifies triggering images visually (even without matching text).
🔹 Files
      •	image_classifier.py — Script to train a ResNet18 model
      •	image_model.pt — Saved trained model used for inference
      •	images/ — Training data in 3 folders: pineapple/, cupcake/, neutral/

⚖️ How to Train the Model
      cd model-training
      python image_classifier.py
      
      This will:
      •	Resize images
      •	Use ResNet18 pretrained model
      •	Train a classifier with 3 categories
      •	Save model to image_model.pt

🔄 How to Use the Inference Server
      The file is located inside the /web-ui folder.
      cd web-ui
      python inference_server.py
      •	Runs at http://localhost:5001
      •	Receives POST image and returns label prediction (e.g., "cupcake")

✅ Requirements
      •	Python 3.13+
      •	Packages: torch, torchvision, flask, flask_cors

🚀 Model Output
      The model classifies every image as one of:
      •	pineapple
      •	cupcake
      •	neutral
      These are sent back to the extension for content filtering.
