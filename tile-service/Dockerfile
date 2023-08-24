FROM node:18-slim

COPY . /tile-service
WORKDIR /tile-service
RUN npm ci

ENTRYPOINT "./tile.js"
