FROM python:3.8
RUN mkdir /code
WORKDIR /code
ADD requirements /code/requirements
ENV PIP_NO_CACHE_DIR=1
RUN ln -sf /usr/share/zoneinfo/CET /etc/localtime

RUN pip3 install --use-deprecated=legacy-resolver -r requirements/docker.txt
ADD . /code