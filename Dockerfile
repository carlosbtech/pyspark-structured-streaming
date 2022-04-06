# get image from jupyter/pyspark-notebook
# https://hub.docker.com/r/jupyter/pyspark-notebook/tags?page=1&name=3.1.2
ARG VERSION_SPARK=spark-3.1.2
FROM jupyter/pyspark-notebook:${VERSION_SPARK}

USER root:root

# create the directory that will store the spark jobs
RUN mkdir -p /app

# copy spark jobs local to image
COPY ./app /app

# default directory spark jobs
WORKDIR /app