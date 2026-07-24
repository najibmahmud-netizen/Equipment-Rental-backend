FROM python:3.12-slim

# Prevent Python from writing .pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files during the image build
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Run migrations, then start Gunicorn
CMD sh -c "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}"