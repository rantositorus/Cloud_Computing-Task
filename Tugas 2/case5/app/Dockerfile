# Gunakan image Python yang ringan
FROM python:3.9-alpine

# Set folder kerja
WORKDIR /code

# Copy requirements dan install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy sisa kode
COPY . .

# Jalankan aplikasi
CMD ["python", "app.py"]