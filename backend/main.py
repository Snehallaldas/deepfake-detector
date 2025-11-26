from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from model import predict_image
from utils import load_image, allowed_file
import io

app = FastAPI()

# ----------------------------------------------------
# CORS - allow frontend to connect (VERY IMPORTANT)
# ----------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow all frontends
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
# TEST ENDPOINT
# ----------------------------------------------------
@app.get("/")
def root():
    return {"status": "backend running"}


# ----------------------------------------------------
# MAIN PREDICT ENDPOINT
# ----------------------------------------------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Check file extension
    if not allowed_file(file.filename):
        return {"error": "Invalid file type. Allowed: JPG, JPEG, PNG, WEBP"}

    # Read file bytes
    content = await file.read()

    # Convert to PIL image using utils
    img = load_image(content)
    if img is None:
        return {"error": "Could not read this image. Please try another one."}

    # Pass image to the model
    result = predict_image(img)

    return result
