FROM python:3.9-alpine

# Setup folder kerja
WORKDIR /app

# Install dependensi
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY app.py .

# Command default
CMD ["python", "app.py"]