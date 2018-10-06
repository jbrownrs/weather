# Based on the upstream Python 3.7 Alpine image
FROM python:3.7.0-alpine3.7

WORKDIR /usr/src/app

# Copy the requirements to the container and install them
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD [ "python", "weather.py" ]

