# base image to be used
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /current
# reminder to edit the requirements.txt file
COPY requirements.txt /current/ 
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /current

# set environment vars to be used
ENV AUTHOR="ShanmukhaS"
# port from the container to expose to host
EXPOSE 8008
# CMD /current/start_server.sh

FROM python:3.8

RUN pip install numpy 

RUN wget https://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz/download && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr && \
  make && \
  make install

RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz