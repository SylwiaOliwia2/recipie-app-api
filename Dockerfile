FROM python:3.7-alpine
MAINTAINER London App Developer Ltd.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
# install postgres. No cache to keep the app as light
RUN apk add --update --no-cache postgresql-client
# --virtual - to keep th epackages temporary for the installment, remove them once they are no longer needed
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user
