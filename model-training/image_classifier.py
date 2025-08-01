import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
from torchvision.models import ResNet18_Weights


# Settings
img_size = 150
batch_size = 8
num_epochs = 5
data_dir = os.path.join(os.getcwd(), "images") # images/cupcake, images/pineapple, etc.
model_path = os.path.join(os.getcwd(), "image_model.pt")

print(f"....Looking for images in: {data_dir}")


# Transformations: Resize → Tensor
transform = transforms.Compose([
	transforms.Resize((img_size, img_size)),
	transforms.ToTensor()
])


# Load Datasets
train_data = datasets.ImageFolder(data_dir, transform=transform)
train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)


# Load ResNet18 with ImageNet weights
weights = ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)
model.fc = nn.Linear(model.fc.in_features, len(train_data.classes)) # adjust output layer


# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


# Define Loss & Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# Training Loop
for epoch in range(num_epochs):
	model.train()
	running_loss = 0.0

	for inputs, labels in train_loader:
		inputs, labels = inputs.to(device), labels.to(device)

		optimizer.zero_grad()
		outputs = model(inputs)
		loss = criterion(outputs, labels)
		loss.backward()
		optimizer.step()

		running_loss += loss.item()

	print(f"....Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss:.4f}")


# Save the trained model
torch.save(model.state_dict(), model_path)
print(f".... Model saved to {model_path}")
