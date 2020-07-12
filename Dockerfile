# base image to be used
FROM python:3.8-slim-buster
# The environment variable ensures that the python output is set 
#straight to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
WORKDIR /current
# reminder to edit the requirements.txt file
COPY requirements.txt /current/ 
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /current

#set environment vars to be used
ENV AUTHOR="ShanmukhaS"
#port from the container to expose to host
EXPOSE 8008
#Tell image what to do when it starts as a container
CMD /current/start_server.sh