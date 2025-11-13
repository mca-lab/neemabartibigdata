# Use Ubuntu-based JDK (supports apt-get)
FROM eclipse-temurin:21-jdk-jammy

# Install Python + pip
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir pyspark requests

# Set working directory
WORKDIR /app

# Install dependencies (if you have any)
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt || true

# Copy your source code
COPY src/ /app/src/

# Default command: RUN CLEAN SCRIPT
CMD ["python3", "src/clean.py"]





