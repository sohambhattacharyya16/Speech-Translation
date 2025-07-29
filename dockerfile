# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install required system packages (including ffmpeg)
RUN apt-get update && \
    apt-get install -y ffmpeg git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio's default port
EXPOSE 7860

# Command to run your app
CMD ["python", "main.py"]
