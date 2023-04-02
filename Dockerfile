# Use the official Python base image
FROM python:3.9
# Set the working directory
WORKDIR /app

# Install the dependencies with --no-cache-dir so it wont download the flask app here  ~/.cache/pip
RUN pip install flask
RUN pip install Selenium
# Copy the Flask app and the Utils.py file into the container,
# IF YOU WILL CHECK THE docker-compose.yml file you will see that in the build:(block) > context:
# i told Docker that my main directory will be ../   so it will go one folder behind the folder where this files are located, so in the main folder which is WoG
# And thats why here in COPY i said Scores/Mainscores.py   because now docker see all my main folder and subfolders
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "MainScores.py"]