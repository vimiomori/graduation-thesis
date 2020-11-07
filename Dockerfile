FROM ubuntu:18.04

COPY ./training /
RUN chmod +x /setup.sh
RUN chmod +x /run.sh