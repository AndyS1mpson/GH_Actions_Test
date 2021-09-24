FROM python:latest

COPY . ./core
WORKDIR /core

RUN pip install --no-cache-dir -r ./requirements/requirements.txt

ENTRYPOINT [ "pytest", "./tests", "-v" ]