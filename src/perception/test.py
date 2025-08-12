from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

# Load CLIP model
model = CLIPModel.from_pretrained("laion/CLIP-ViT-bigG-14-laion2B-39B-b160k")
processor = CLIPProcessor.from_pretrained("laion/CLIP-ViT-bigG-14-laion2B-39B-b160")

# Load your image
image_path = "/home/sorin/dev/FarmbotKG/ressources/plant_capacity_imgs/75%_field_capacity/10_0_1.jpg"  # your uploaded leaf image
image = Image.open(image_path)

# Define text prompts
text_prompts = ["The Leaf is mostly yellow and requires watering", "The Leaf is mostly green and does not require watering",
                "The leaf consists of a mix of yellow and green and requires some watering"]

# Preprocess
inputs = processor(text=text_prompts, images=image, return_tensors="pt", padding=True)

# Forward pass
with torch.no_grad():
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)

# Show probabilities
for prompt, p in zip(text_prompts, probs[0].tolist()):
    print(f"{prompt}: {p:.4f}")
