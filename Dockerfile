# pull official base image
FROM python:3.9-alpine

#set the WORKDIR
WORKDIR /app
ENV PORT=8000

# Copy the local app in the /app container
ADD . /app

# Install specific requirements
RUN pip install -r requirements.txt
EXPOSE 8000
# Run the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
