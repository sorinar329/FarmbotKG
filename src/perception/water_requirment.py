import torch
import clip
from PIL import ImageDraw
from PIL import Image as PILImage


def run_clip(img_path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-L/14@336px", device=device)

    text_prompts = ["no water required", "low water requirement", "medium water requirement", "high water requirement"]
    text_inputs = clip.tokenize(text_prompts).to(device)

    image = PILImage.open(img_path)
    image_tensor = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image_tensor)
        text_features = model.encode_text(text_inputs)

        # Normalize features
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        # Calculate similarity
        similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    # Show me every score and not only the highest one


        # Get the index of the highest similarity score
        highest_index = similarity.argmax(dim=-1).item()
        highest_score = similarity[0][highest_index].item()
        highest_label = text_prompts[highest_index]

    return highest_label, highest_score
#
def get_water_requirement(img_path):
    """
    Get the water requirement for a given image using CLIP model.

    :param img_path: Path to the image file.
    :return: A tuple containing the water requirement label and its score.
    """
    label, score = run_clip(img_path)
    return label, score

if __name__ == "__main__":
    img_path = "/home/sorin/dev/FarmbotKG/ressources/plant_capacity_imgs/25%_field_capacity/10_0_2.jpg"  # Replace with your image path
    label, score = get_water_requirement(img_path)
    print(f"Water Requirement: {label}, Score: {score:.2f}")