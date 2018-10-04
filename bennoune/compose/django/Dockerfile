FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN groupadd -r django \
    && useradd -r -g django django

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r requirements/requirements.txt \
    && rm -rf /requirements

COPY . /app

RUN chown -R django /app

USER django

WORKDIR /app

