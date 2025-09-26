FROM python:3.12.4-slim-bullseye  
 
WORKDIR /app
 
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

COPY requirements.txt .
 
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . .
 
EXPOSE 8000
 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]