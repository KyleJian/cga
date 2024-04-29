# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY your_script.py .

# Install the required packages using pip
RUN pip install google-generativeai

# Command to run the Python script
CMD ["python", "cga2.py"]
