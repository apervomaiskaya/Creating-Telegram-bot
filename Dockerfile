# Используем официальный образ Python как базовый
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY requirements.txt .
COPY bot.py .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Определяем команду для запуска приложения
CMD ["python", "bot.py"]
