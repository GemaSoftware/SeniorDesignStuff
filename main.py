#!/usr/bin/env python3
#This python code will mainly be used for calling RsaCTFTool to run a predetermined RSA 'crack'

#Will make it so that It will listen on a port to 
from re import sub
import socket
import sys
from _thread import *
import subprocess

if __name__ == "__main__":
    host = ''
    port = 1337
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((host, port))
        print("Successfully Binded to port 1337")
    except socket.error as e:
        print("Could not bind:", str(e))

    s.listen(5)
    print('Waiting for a connection.')
    def threaded_client(conn):
        string_data = ''
        while string_data != "run\n":
            data = conn.recv(2048)
            string_data = data.decode('utf-8')

        conn.send(str.encode('Will now run the RSA stuff.\n'))
        strOut = subprocess.check_output(['/opt/RsaCtfTool/RsaCtfTool.py', '--key', '/opt/RsaCtfTool/examples/masked.pem', '--attack', 'partial_q'])
        
        #stdout, stderr

        conn.send(str.encode('Running RSA cracking\n'))
        conn.send(str.encode("Finished running on Docker\n"))
        conn.send(strOut)
        conn.send(str.encode("Error:\n"))
        conn.send(str.encode(y))
        conn.close()


    while True:

        conn, addr = s.accept()
        print('connected to: '+addr[0]+':'+str(addr[1]))

        start_new_thread(threaded_client,(conn,))