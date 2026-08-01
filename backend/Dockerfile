# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose Flask Port
EXPOSE 5000

# Environment Variables
ENV PYTHONUNBUFFERED=1

# Start Application
CMD ["python", "run.py"]