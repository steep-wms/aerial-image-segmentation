FROM node:18-slim

COPY . /tile-service
WORKDIR /tile-service
RUN npm ci

ENTRYPOINT ["node", "./tile.js"]
