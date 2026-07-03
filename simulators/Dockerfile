# Use a lightweight official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your dependency file and install required AWS packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your simulator Python file into the container
COPY pressure_sim.py .

# Run your script when the container launches
CMD ["python", "-u", "simulator.py"]

