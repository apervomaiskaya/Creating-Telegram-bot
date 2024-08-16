# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы в рабочую директорию
COPY . .

# Указываем команду для запуска
CMD ["python", "bot.py"]
