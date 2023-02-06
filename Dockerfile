FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/album

COPY ./req.txt /url/src/req.txt
RUN pip install -r /url/src/req.txt


COPY . /usr/src/album


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

