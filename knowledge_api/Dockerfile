FROM python:3.11-alpine3.18

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apk --no-cache add musl-dev linux-headers g++ openblas-dev && apk add libffi-dev

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]