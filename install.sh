#!/bin/bash

#Create required functions to create parent image and main image
createDockerImages () {
        #gets main directory of install script where folders located
        maindirname=$(dirname -- "$0";);
        echo $maindirname
        #build image1 which is the OS
        docker build --tag mainparentimage ${maindirname}/ParentImage
        #build image2 which contains code etc.
        docker build --tag mainrsacracking ${maindirname}/MainImage
}

checkforKube () {
        if [[ -x "$(which kubectl)" ]]; then
                return 0;
        else
                echo "LOG::::::KUBECTL NOT INSTALLED. TERMINATING"
                exit 1;
        fi
}



# Check if docker installed
if [[ -x "$(which docker)" ]]; then
        echo "LOG::::::Docker is installed"
        createDockerImages
        echo "LOG::::::Docker images built successful."
        docker run -d  -p 1234:1337 mainrsacracking
        echo "LOG::::::Docker instance created as test. Now trying connection and output"
        sleep 3s
        echo "run" | nc -q 2 localhost 1234
        checkforKube
        echo "LOG::::::Installing Skupper"
        curl https://skupper.io/install.sh | sh
        echo "LOG::::::SKUPPER INSTALLED"
else
        echo "ERROR::::::Docker not installed"
fi