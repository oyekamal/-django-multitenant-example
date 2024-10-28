# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install netcat and PostgreSQL client
RUN apt-get update && \
    apt-get install -y netcat-openbsd postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entrypoint script and ensure it has the right permissions
COPY --chmod=0755 entrypoint.sh /app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Use the entrypoint script as the container's entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

