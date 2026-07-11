# ------------------------
# Stage 1: Builder
# ------------------------

FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir \
    -r requirements.txt

# ------------------------
# Stage 2: Runtime
# ------------------------

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder \
    /usr/local/lib/python3.11/site-packages \
    /usr/local/lib/python3.11/site-packages

COPY --from=builder \
    /usr/local/bin \
    /usr/local/bin

COPY src ./src
COPY models ./models

COPY .env.example .

EXPOSE 8000

ENV MODEL_PATH=/app/models/my_classifier_model.h5
ENV LOG_LEVEL=INFO

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]