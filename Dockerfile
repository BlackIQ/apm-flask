FROM tiangolo/uwsgi-nginx-flask:python3.7
WORKDIR /app
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
COPY . /app
CMD ["python3", "wsgi.py"]