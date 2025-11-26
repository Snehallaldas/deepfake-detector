import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

MODEL_NAME = "sakshamkr1/deitfake-v2"

# Load processor + model
processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)
model.eval()

def predict_image(img: Image.Image):
    """
    Full-image deepfake detection (no cropping).
    """
    inputs = processor(images=img, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits
        probs = logits.softmax(dim=1)[0]

    real_prob = float(probs[0])
    fake_prob = float(probs[1])

    return {
        "real_probability": real_prob,
        "fake_probability": fake_prob,
        "label": "REAL" if real_prob > fake_prob else "FAKE"
    }
