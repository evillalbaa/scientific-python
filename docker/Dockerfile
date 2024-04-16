# base layer, a python setup
FROM python:3.9

# setup a working directory
WORKDIR /code

# Next we will install within the docker image, the requirements file
COPY ./requirements.txt /code/requirements.txt

# We will install the requirements 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy our application
COPY ./app /code/app

# Finally run the API server with uvicorn, each command with a a new element 
# in the list

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
