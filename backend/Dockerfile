FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

# Collect static at build time optional (skipped by default)
# RUN python manage.py collectstatic --noinput || true

EXPOSE 8000
CMD ["gunicorn", "newjinsproject.wsgi:application", "-c", "gunicorn.conf.py"]
