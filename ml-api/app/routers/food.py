from fastapi import APIRouter, File, UploadFile, HTTPException
from PIL import Image
import io
from ..services.foodDetection import predict_food

router = APIRouter()

ACCEPTED_IMAGE_TYPES = [
    "image/jpeg",
    "image/png",
    "image/bmp",
    "image/tiff",
    "image/webp",
    "image/heic",
    "image/heif"
]

@router.post("/food/predict", tags=["food"])
async def predict(image: UploadFile = File(...)):
    if image.content_type not in ACCEPTED_IMAGE_TYPES:
        raise HTTPException(status_code=404, detail="Invalid file type. Only images are allowed.")

    image_bytes = await image.read()
    img = Image.open(io.BytesIO(image_bytes))

    [label, confidence] = predict_food(img)

    return {"food": label, "confidence": confidence*100}