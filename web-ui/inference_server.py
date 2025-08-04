from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from torchvision import models, transforms
from PIL import Image,UnidentifiedImageError
import os
 
app = Flask(__name__)
CORS(app) # You can fine-tune origins later

# Load model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model-training', 'image_model.pt')
model = models.resnet18(weights="IMAGENET1K_V1")
model.fc = torch.nn.Linear(model.fc.in_features, 3) # Assuming 3 classes
model.load_state_dict(torch.load(model_path, map_location="cpu"))
model.eval()

# Transform
transform = transforms.Compose([
    transforms.Resize((150, 150)),
    transforms.ToTensor()
])

# Fake class list for now (can be passed from training or stored in a .json)
class_names = ['cupcake', 'neutral', 'pineapple']

from PIL import Image, UnidentifiedImageError

@app.route("/predict", methods=["POST"])

def predict():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "no image uploaded"}), 400
        
        img_file = request.files['image']
        print(f"📸 Received: {img_file.filename} ({img_file.content_type})")

        if img_file.content_type not in ["image/jpeg", "image/png"]:
            print("⚠️ Unsupported image type:", img_file.content_type)
            return jsonify({"prediction": "neutral"})  # fallback label

        try:
            img = Image.open(img_file).convert("RGB")
        except UnidentifiedImageError:
            print("❌ PIL failed to recognize image format.")
            return jsonify({"prediction": "neutral"})

        img_tensor = transform(img).unsqueeze(0)

        with torch.no_grad():
            outputs = model(img_tensor)
            _, predicted = torch.max(outputs, 1)
        
        result = class_names[predicted.item()]
        print(f"✅ Final prediction: {result}")
        return jsonify({"prediction": result})

    except Exception as e:
        print("🔥 Server error:", e)
        return jsonify({"error": str(e)}), 500
 

if __name__ == '__main__':
    app.run(port=5001)
