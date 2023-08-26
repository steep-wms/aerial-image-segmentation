FROM node:18-slim

COPY . /tiling-service
WORKDIR /tiling-service
RUN npm ci

ENTRYPOINT ["node", "./tile.js"]
