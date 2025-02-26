# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Use gunicorn as the production WSGI HTTP Server
CMD ["python", "app.py"]