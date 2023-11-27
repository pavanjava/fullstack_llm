FROM python:3.11-alpine3.18

WORKDIR /code/src

COPY ./requirements.txt /code/requirements.txt

RUN apk --no-cache add musl-dev linux-headers g++ openblas-dev

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/src

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]