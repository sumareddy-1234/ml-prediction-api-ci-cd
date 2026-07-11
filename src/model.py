import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

MODEL = None

IMAGE_SIZE = (28, 28)

CLASS_LABELS = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]


def load_model(model_path=None):
    """
    Load the keras model only once.
    """

    global MODEL

    if MODEL is None:

        if model_path:
            path = model_path
        else:
            path = os.environ.get(
                "MODEL_PATH",
                "models/my_classifier_model.h5"
            )

        if not os.path.exists(path):
            raise FileNotFoundError(
                f"Model not found at {path}"
            )

        MODEL = tf.keras.models.load_model(path)

    return MODEL


def preprocess_image(image_bytes):

    try:

        image = Image.open(
            io.BytesIO(image_bytes)
        )

        image = image.convert("L")

        image = image.resize((28,28))

        image = np.array(image)

        image = image.astype("float32")

        image = image / 255.0

        image = np.expand_dims(
            image,
            axis=-1
        )

        image = np.expand_dims(
            image,
            axis=0
        )

        return image

    except Exception as e:

        raise ValueError(
            f"Image preprocessing failed: {e}"
        )


def predict_image(preprocessed_image):

    model = load_model()

    prediction = model.predict(
        preprocessed_image,
        verbose=0
    )

    predicted_index = int(
        np.argmax(prediction)
    )

    probabilities = prediction[0].tolist()

    return {
        "class_label":
            CLASS_LABELS[predicted_index],
        "probabilities":
            probabilities
    }