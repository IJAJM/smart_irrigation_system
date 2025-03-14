# Gunakan image Python
FROM python:3.9

# Set direktori kerja di dalam container
WORKDIR /app

# Salin semua file proyek ke dalam container
COPY . .

# Instal dependensi yang diperlukan
RUN pip install -r requirements.txt

# Jalankan script utama
CMD ["python", "main.py"]
