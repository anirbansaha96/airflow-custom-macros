# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port on which the Flask app will run
EXPOSE 5001

# Define the command to run your application
CMD ["python", "app.py"]
