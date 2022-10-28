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

#Checks if kubernetes installed.
checkforKube () {
        if [[ -x "$(which kubectl)" ]]; then
                return 0;
        else
                echo "LOG::::::KUBECTL NOT INSTALLED. TERMINATING"
                exit 1;
        fi
}

checkforSkupper () {
        if [[ -f "$(eval echo ~$user)/bin/skupper" ]]; then
                echo "LOG:::::::SKUPPER ALREADY INSTALLED, SKIPPING"
                return 0;
        else
                echo "LOG::::::SKUPPER NOT INSTALLED. INSTALLING SKUPPER"
                curl https://skupper.io/install.sh | sh
                #adds skupper location to PATH
                export PATH="$(eval echo ~$user)/bin:$PATH"
                return 0;
        fi
}



# Check if docker installed
if [[ -x "$(which docker)" ]]; then
        echo "LOG::::::Docker is installed"
        createDockerImages
        echo "LOG::::::Docker images built successful."
        docker run -d  -p 1234:1337 mainrsacracking
        echo "LOG::::::Docker instance created as test. Now trying connection and output"
        sleep 3
        echo "run" | nc -w 2 localhost 1234
        checkforKube
        echo "LOG::::::Installing Skupper"
        checkforSkupper
        echo "LOG::::::SKUPPER INSTALLED"
else
        echo "ERROR::::::Docker not installed"
fi