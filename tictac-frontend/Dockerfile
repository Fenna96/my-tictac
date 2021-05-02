FROM node:10.16.3-alpine

WORKDIR /app/
RUN ln -sf /usr/share/zoneinfo/CET /etc/localtime

COPY ./package.json /app/
COPY ./yarn.lock /app/
RUN yarn install --network-timeout=300000
RUN yarn global add serve

COPY . /app/

EXPOSE 3000