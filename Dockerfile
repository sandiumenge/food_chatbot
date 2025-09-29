FROM python:3.12.4-slim-bullseye  
 
WORKDIR /app
 
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 

RUN apt-get update && \
    apt-get install -y build-essential \
    libpq-dev

COPY requirements.txt .
 
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . .
 
ENV DJANGO_SETTINGS_MODULE=favfoods.settings
ENV PYTHONUNBUFFERED=1
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "favfoods.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]