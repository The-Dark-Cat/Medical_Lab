FROM python:3.10.0

RUN mkdir /code
WORKDIR /code
ENV PATH="/code:${PATH}"
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/