# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir pandas==2.0.3 numpy==1.24.4 Flask==2.2.3 scikit-learn==1.2.2 gunicorn==20.1.0 werkzeug==2.2.3
COPY random_forest_model.pkl random_forest_model.pkl
# Make port 8008 available to the world outside this container
EXPOSE 8008

# CMD to run the server script
CMD ["gunicorn", "--bind", "0.0.0.0:8008", "serve:app"]
