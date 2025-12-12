#!/bin/sh

docker rm -f frontend-dev

docker container run \
-dit \
--name frontend-dev \
-p 3000:3000 \
-v "$(pwd)/my-app:/app" \
--workdir /app \
node:22-alpine \
sh -c "if [ ! -f 'package.json' ]; then \
       echo 'Cleaning directory...'; \
       rm -rf * .[!.].*; \
       npx --yes create-vite@5.5.0 . --template react && npm install; \
       fi && npm run dev -- --host --port 3000"