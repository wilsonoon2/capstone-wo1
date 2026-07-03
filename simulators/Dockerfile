FROM python:3.11-slim

WORKDIR /app

# Install AWS IoT SDK + any other dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your simulator code
COPY pressure_sim.py .

CMD ["python", "pressure_sim.py"]

