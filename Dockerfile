FROM python:3.12-slim

WORKDIR /app

# Копіюємо файли залежностей першими — для кращого кешування шарів
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо вихідний код
COPY src/ ./src/
COPY main.py .

# Запускаємо демонстрацію за замовчуванням
CMD ["python", "main.py"]
