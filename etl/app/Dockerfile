# Use official Python image as base
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Copy the requirements.txt first, to leverage Docker cache
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the ETL process
CMD ["python", "etl.py"]