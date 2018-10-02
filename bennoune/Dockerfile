FROM django

COPY ./requirements requirements
RUN pip install -r requirements.txt


ADD . /app
WORKDIR /app

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]