FROM node:20-slim

COPY . /tile-service
WORKDIR /tile-service
RUN npm ci

ENTRYPOINT "./tile.js"
