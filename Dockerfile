# pull official base image
FROM python:3.9-alpine

#set the WORKDIR
WORKDIR /app

# Copy the local app in the /app container
ADD . /app

# Install specific requirements
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
