# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE_PATH="sqlite:////app/data/vehiclemanager.sqlite" \
    TEMPLATES_DIR="./templates" \
    STATIC_DIR="./static"

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Create directory for SQLite database file (separate from code)
RUN mkdir -p /app/data

# Change working directory to app subdirectory where main.py is located
WORKDIR /app/app

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "-c", "import uvicorn; from main import app; uvicorn.run(app, host='0.0.0.0', port=8000)"]
