# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8008 available to the world outside this container
EXPOSE 8008

# CMD to run the server script
CMD ["gunicorn", "--bind", "0.0.0.0:8008", "serve:app"]
