# Use Python image
FROM python:3.9-slim

# Install system packages and chrome (Using single RUN command to reduce layers and image size)
RUN apt-get update \
    && apt-get install -y wget unzip \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all application files (including requirements.txt)
COPY . .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the score service
EXPOSE 5000

# Finally, run the WoG application (with the score server)
CMD ["python", "MainScores.py"]