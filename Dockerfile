# Simple test for a Dockerfile.
# As I haven't been able to install Docker (not supported on Windows 7), I haven't been able to test it

FROM python:3

# Working directory (creation and setting)
RUN mkdir /app
WORKDIR /app

# Add our current directory to the working directory.
ADD . /app/

# NB : normally, this should'nt be necessary as ADD moves requirements as well.
COPY requirements.txt ./

ENV PORT=8000
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD [ "python", "./manage.py runserver"]
