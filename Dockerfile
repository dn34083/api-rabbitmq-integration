# set base image (host OS)
FROM python:3.10

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# criar path para aplicação
RUN mkdir /opt/rabbitFiles

COPY / .

EXPOSE 5055
# command to run on container start
CMD [ "python", "./src/Controller.py" ]
