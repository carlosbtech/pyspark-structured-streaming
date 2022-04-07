A simple project developed for a demo of Apache Spark using the Structured Streaming API

- Dependencies \
[Docker](https://www.docker.com/products/docker-desktop/) \
[Docker Compose](https://docs.docker.com/compose/install/) 
```sh
# check versions
docker --version
Docker version 20.10.13, build a224086

docker-compose version
Docker Compose version v2.3.3

# enable services
docker-compose up -d

# expected output
[+] Running 1/1
 ⠿ Container spark-structured-streaming  Started                                                                   1.8s

# check services
docker-compose ps

# expected output
NAME                         COMMAND                  SERVICE             STATUS              PORTS
spark-structured-streaming   "tini -g -- start.sh…"   webapp              running             0.0.0.0:8888->8888/tcp

# in terminal notebook
nc -lk 9999

# run spark-structured-streaming
spark-submit main.py localhost:9999
```
