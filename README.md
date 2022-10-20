# SeniorDesignStuff
LCB Stuff

To test the Docker image creation and testing the RSA cracking tool. You will need to run the following.

git clone this Repository into any space and ensure you have Docker installed.

```
cd SeniorDesignStuff/ParentImage/
docker build --tag "mainparentimage" .
<This will take a while>
cd ../MainImage/
docker build --tag "seniordesign" .
docker run -d -p 1234:1337 seniordesign:latest
```
Once the docker container is running, go and test it out. Open a terminal and open a netcat session to port 1234 on localhost. When creating the nc command you may not see any output. you will only see output when you type in run and hit enter.

```
nc localhost 1234
run
```
