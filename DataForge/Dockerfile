FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Expose the port where the app runs on
EXPOSE 8002

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]



# Add as much features, automations and settings as needed and as possible to leverage what Dockerfile can do to manage tasks by its own to enhance the power of it for a better and secure deployment of the entire app, but just those that are really neccesary.