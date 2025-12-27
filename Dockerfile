FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Рабочая директория
WORKDIR /app

# Утилиты + Chrome зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libxdamage1 \
    libxfixes3 \
    libxshmfence1 \
    libpangocairo-1.0-0 \
 && rm -rf /var/lib/apt/lists/*

# Ключ Google Chrome
RUN mkdir -p /usr/share/keyrings \
 && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
 | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg

# Репозиторий Chrome
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
 > /etc/apt/sources.list.d/google-chrome.list

# Установка Chrome
RUN apt-get update && apt-get install -y --no-install-recommends \
    google-chrome-stable \
 && rm -rf /var/lib/apt/lists/*

# Папка для Allure
RUN mkdir -p /allure-results

# Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Проект
COPY . .

# Запуск тестов
CMD ["pytest", "--alluredir=/allure-results"]
