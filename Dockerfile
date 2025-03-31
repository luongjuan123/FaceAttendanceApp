# Sử dụng image Python chính thức làm base
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Cài đặt các phụ thuộc hệ thống trước khi cài Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpython3-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libqt6gui6 \
    cmake \
    libpng-dev \
    libjpeg-dev \
    libopenexr-dev \
    libtiff-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Sao chép file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các thư viện Python
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Mở cổng (nếu cần, tùy ứng dụng)
EXPOSE 5000

# Lệnh chạy ứng dụng (thay main.py bằng file chính của bạn nếu khác)
CMD ["python", "main.py"]