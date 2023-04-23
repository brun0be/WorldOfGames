# Use the official Python base image
FROM python:3.9
# Set the working directory
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8777

# Start the Flask app
CMD ["python", "MainScores.py"]
#CMD ["python", "MainScores.py", "python", "MainGame.py"]