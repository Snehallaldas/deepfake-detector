import io
from PIL import Image

def load_image(file_bytes: bytes):
    """
    Convert uploaded file bytes to a PIL RGB image.
    """
    try:
        img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
        return img
    except Exception as e:
        print(f"❌ Error loading image: {e}")
        return None


def allowed_file(filename: str):
    """
    Check file extension is valid.
    """
    allowed_ext = (".jpg", ".jpeg", ".png", ".webp")
    return filename.lower().endswith(allowed_ext)


def debug_print(label: str, value):
    """
    Helper to print debug messages clearly.
    """
    print(f"🔍 {label}: {value}")


def format_prediction(real_prob: float, fake_prob: float):
    """
    Format prediction into a JSON-safe dictionary.
    """
    return {
        "real_probability": real_prob,
        "fake_probability": fake_prob,
        "label": "REAL" if real_prob > fake_prob else "FAKE"
    }
