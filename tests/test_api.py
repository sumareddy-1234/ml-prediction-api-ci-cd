from fastapi.testclient import TestClient

from src.main import app

from unittest.mock import patch

import io

from PIL import Image


client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "ok"


@patch("src.main.predict_image")
@patch("src.main.preprocess_image")
def test_predict_success(
    mock_preprocess,
    mock_predict
):

    mock_preprocess.return_value = "image"

    mock_predict.return_value = {
        "class_label": "5",
        "probabilities": [0.1] * 10
    }

    image = Image.new(
        "RGB",
        (28, 28)
    )

    buffer = io.BytesIO()

    image.save(
        buffer,
        format="PNG"
    )

    buffer.seek(0)

    response = client.post(
        "/predict",
        files={
            "file":
            (
                "digit.png",
                buffer,
                "image/png"
            )
        }
    )

    assert response.status_code == 200


def test_invalid_file():

    response = client.post(
        "/predict",
        files={
            "file":
            (
                "test.txt",
                b"text file",
                "text/plain"
            )
        }
    )

    assert response.status_code == 400


def test_missing_file():

    response = client.post(
        "/predict"
    )

    assert response.status_code == 422