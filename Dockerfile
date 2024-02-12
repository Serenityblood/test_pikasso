FROM ubuntu:latest
LABEL authors="mirac"

ENTRYPOINT ["top", "-b"]