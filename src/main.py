from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
from fastapi import status

from pydantic import BaseModel

from typing import List

import logging
import os

from src.model import (
    load_model,
    preprocess_image,
    predict_image
)

logging.basicConfig(

    level=os.environ.get(
        "LOG_LEVEL",
        "INFO"
    ).upper(),

    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(

    title="ML Prediction API",

    description="Image Classification API",

    version="1.0"
)


@app.on_event("startup")
async def startup():

    try:

        load_model()

        logger.info(
            "Model loaded successfully"
        )

    except Exception as e:

        logger.error(str(e))

        raise RuntimeError(str(e))


class PredictionResponse(BaseModel):

    class_label: str

    probabilities: List[float]


@app.get("/health")

async def health():

    return {

        "status": "ok",

        "message":
        "API is healthy and model is loaded."
    }


@app.post(

    "/predict",

    response_model=PredictionResponse,

    status_code=status.HTTP_200_OK
)

@app.post(
    "/predict",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK
)
async def predict(
    file: UploadFile = File(...)
):

    ALLOWED_TYPES = {
        "image/png",
        "image/jpeg",
        "image/jpg"
    }

    # Validate file type
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PNG and JPEG images are allowed."
        )

    MAX_FILE_SIZE = 5 * 1024 * 1024

    try:
        image_bytes = await file.read()

        if len(image_bytes) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="Image exceeds 5MB limit."
            )

        processed = preprocess_image(
            image_bytes
        )

        result = predict_image(
            processed
        )

        logger.info(
            f"Prediction completed for {file.filename}"
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=422,
            detail=str(e)
        )

    except HTTPException:
        raise

    except Exception as e:

        logger.error(
            f"Prediction failed: {e}",
            exc_info=True
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )