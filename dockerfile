# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TRANSFORMERS_CACHE=/app/hf_cache

# Create cache dir for Hugging Face
RUN mkdir -p /app/hf_cache && chmod -R 777 /app/hf_cache

# Install required system packages
RUN apt-get update && \
    apt-get install -y ffmpeg git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio port
EXPOSE 7860

# Optional OpenShift health check
HEALTHCHECK CMD curl --fail http://localhost:7860 || exit 1

# Run as non-root user (optional for OpenShift)
USER 1001

# Start app
CMD ["python", "main.py"]

