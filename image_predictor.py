import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import os



# Constants
img_size = 150
model_path = os.path.join(os.getcwd(), "image_model.pt")
data_dir = os.path.join(os.getcwd(), "images") # Needed to get class names

print("model_path is : ",model_path)
print("data_dir is : ",data_dir)


# Load class names from folder structure
class_names = sorted(entry.name for entry in os.scandir(data_dir) if entry.is_dir())

# Define image transforms (same as training)
transform = transforms.Compose([
	transforms.Resize((img_size, img_size)),
	transforms.ToTensor()
])


# Load image
def load_image(image_path):
	image = Image.open(image_path).convert("RGB")
	return transform(image).unsqueeze(0) # Add batch dimension


# Load model
model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()


# Predict
def predict(image_path):
	input_tensor = load_image(image_path)
	with torch.no_grad():
		output = model(input_tensor)
		_, predicted = torch.max(output, 1)
		return class_names[predicted.item()]



# Run test
if __name__ == "__main__":
	image_path = input("Enter path to the image you want to classify: ").strip()
	if os.path.exists(image_path):
		result = predict(image_path)
		print(f"🔍 Prediction: This image looks like a **{result}**.")
	else:
		print("❌ File not found. Please check the path.")
