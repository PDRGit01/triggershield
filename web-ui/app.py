from flask import Flask, render_template, request
from PIL import Image
import torch
from torchvision import transforms, models
import os



app = Flask(__name__)



# Load model
model_path = os.path.join(os.path.dirname(__file__), "..", "model-training", "image_model.pt")
model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, 3) # 3 classes
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()



# Image preprocessing
transform = transforms.Compose([
	transforms.Resize((150, 150)),
	transforms.ToTensor()
])


class_names = ['cupcake', 'neutral', 'pineapple']

@app.route("/", methods=["GET", "POST"])
def index():
	prediction = None
	if request.method == "POST":
		file = request.files["image"]
		if file:
			img = Image.open(file.stream).convert("RGB")
			img_tensor = transform(img).unsqueeze(0)
			
			with torch.no_grad():
				output = model(img_tensor)
				_, predicted = torch.max(output, 1)
				prediction = class_names[predicted.item()]
	return render_template("index.html", prediction=prediction)



if __name__ == "__main__":
	app.run(debug=True)
