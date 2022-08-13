FROM python:3.9

FROM jenkins/jenkins:lts-jdk17
USER root
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
      docker.io
USER jenkins

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN --mount=type=cache,target=/root/.cache/ pip install -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]