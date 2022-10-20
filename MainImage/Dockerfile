FROM mainparentimage:latest
WORKDIR /opt
ARG TEST_CACHE=3
RUN git clone https://github.com/GemaSoftware/SeniorDesignStuff.git
WORKDIR /data
ENTRYPOINT ["/opt/SeniorDesignStuff/main.py"]
CMD [""]