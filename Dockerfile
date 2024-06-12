# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y git

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput
# make migrations
RUN python manage.py makemigrations
# migrate
RUN python manage.py migrate

# Expose the port server will listen on
EXPOSE 8000

# Command to run the server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]
