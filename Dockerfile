FROM python:3.10-slim

WORKDIR /app

# We use the CPU-specific link to keep the container lightweight and stable
COPY requirements.txt .
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

COPY . .

# Gradio default port
EXPOSE 7860

CMD ["python", "demo.py"]