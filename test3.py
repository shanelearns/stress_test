import torch
import time
import torchvision.models as models

device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")

model = models.resnet50(pretrained=True).to(device)
model.eval()

input_data = torch.randn(32, 3, 224, 224).to(device)

start = time.time()
with torch.no_grad():
    for _ in range(1000):
        _ = model(input_data)
end = time.time()

print(f"ResNet50 inference (10 batches) took {end - start:.2f} seconds on {device}")
