import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

# Important for Render: reduce RAM and disable gradients
torch.set_grad_enabled(False)

MODEL_NAME = "sakshamkr1/deitfake-v2"

# Lazy loading (model loads only on first request)
processor = None
model = None


def load_model():
    """
    Load processor + model only on the first request.
    This prevents Render from killing the app during startup.
    """
    global processor, model

    if processor is None or model is None:
        processor = AutoImageProcessor.from_pretrained(MODEL_NAME)

        # FP32 preserved, no precision reduction
        model = AutoModelForImageClassification.from_pretrained(
            MODEL_NAME
        ).eval()

    return processor, model


def predict_image(img: Image.Image):
    """
    Full-image deepfake detection (no cropping).
    FP32 precision retained.
    """
    processor, model = load_model()

    img = img.convert("RGB")
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
