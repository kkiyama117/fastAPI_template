FROM python:latest as base

# ---- compile image -----------------------------------------------
FROM base AS compile-image
#RUN apk add linux-headers
RUN apt-get update \
  && apt-get install -y --no-install-recommends apt-utils \
  && apt-get install -y --no-install-recommends \
  build-essential \
  gcc

ADD . /app
RUN python -m venv /app/env
ENV PATH="/app/env/bin:$PATH"

WORKDIR /app
RUN pip install --upgrade pip setuptools wheel
# pip install is fast here (while slow without the venv) :
RUN python setup.py install

# ---- build image -----------------------------------------------
FROM base AS build-image
COPY --from=compile-image /app/env /app/env

# Make sure we use the virtualenv:
ENV PATH="/app/env/bin:$PATH"
COPY . /app
WORKDIR /app
EXPOSE 8000
