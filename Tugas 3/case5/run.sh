docker rm -f python-web redis-db
docker network rm my-net

docker network create my-net

docker run -d \
    --name redis-db \
    --network my-net \
    redis:alpine

docker run -d \
    --name python-web \
    --network my-net \
    -p 8000:5000 \
    mypythonapp:1.0