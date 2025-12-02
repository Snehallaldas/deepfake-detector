from fastapi import FastAPI, UploadFile, File, Response
from fastapi.middleware.cors import CORSMiddleware
from model import predict_image
from utils import load_image, allowed_file

app = FastAPI()

# ----------------------------------------------------
# CORS CONFIG (Render + Browser Safe)
# ----------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # allow all frontends
    allow_credentials=False,      # must be False when using "*"
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
# HOME ROUTE
# ----------------------------------------------------
@app.get("/")
def root():
    return {"status": "backend running"}

# ----------------------------------------------------
# FIX CORS PREFLIGHT FOR /predict
# ----------------------------------------------------
@app.options("/predict")
def preflight_handler():
    return Response(status_code=200)

# ----------------------------------------------------
# MAIN PREDICT ENDPOINT (POST)
# ----------------------------------------------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Validate file extension
    if not allowed_file(file.filename):
        return {"error": "Invalid file type. Allowed: JPG, JPEG, PNG, WEBP"}

    # Read file data
    content = await file.read()

    # Convert to PIL image
    img = load_image(content)
    if img is None:
        return {"error": "Could not read this image. Please try another one."}

    # Run model inference
    result = predict_image(img)

    return result
