FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--log-file", "/app/logs/app.log"]


# Here we are using the built-in logging configuration of uvicorn to directly output logs to a file

# When running the container, map the /app/logs directory to a directory on the host machine:

# docker run -d -p 8000:8000 /app/logging_config : /app/logs fastapi-user-management

