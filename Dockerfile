# Use a base image with Python and libraries you need
FROM python:3.8-slim

WORKDIR /app

COPY model.pkl .

# Install necessary libraries
RUN pip install scikit-learn flask gunicorn

# Copy your inference script
COPY serve.py .

CMD ["gunicorn", "-w 4", "serve:app"]
