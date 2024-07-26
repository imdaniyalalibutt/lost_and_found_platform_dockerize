# Use the official Python 3.9 image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /docker-app

# Copy the requirements file into the container
COPY ./requirements.txt /docker-app/requirements.txt

# Install the required dependencies
RUN pip install --no-cache-dir --upgrade -r /docker-app/requirements.txt

# Copy the application code into the container
COPY ./app /docker-app/app

# Expose the port the app runs on
EXPOSE 80

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
