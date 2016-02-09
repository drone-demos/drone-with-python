FROM python:3.5.1-alpine
MAINTAINER Greg Taylor <gtaylor@gc-taylor.com>

RUN pip install --upgrade pip setuptools wheel
COPY wheeldir /opt/app/wheeldir
# These are copied and installed first in order to take maximum advantage
# of Docker layer caching (if enabled).
COPY *requirements.txt /opt/app/src/
RUN pip install --use-wheel --no-index --find-links=/opt/app/wheeldir \
    -r /opt/app/src/requirements.txt
RUN pip install --use-wheel --no-index --find-links=/opt/app/wheeldir \
    -r /opt/app/src/test-requirements.txt

COPY . /opt/app/src/
WORKDIR /opt/app/src
RUN python setup.py install

EXPOSE 5000
CMD dronedemo
