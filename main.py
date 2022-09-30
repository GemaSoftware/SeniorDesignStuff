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
        process = subprocess.Popen(['../RsaCtfTool/RsaCtfTool.py', '-n 14641034851154010900546719241402474912998133209474218975103977449764205791710698412984067810848509509669017831054155506105922179074286929418416328797379636196613023210067141695123691351917498467761961980966631958692894027223505926821780581042313171803091956255639968110368314924456998367348008686435826036480738828760312467761150839006456972383', '-e 65537', '--uncipher 7102577393434866594929140550804968099111271800384955683330956013020579564684516163830573468073604865935034522944441894535695787080676107364035121171758895218132464499398807752144702697548021940878072503062685829101838944413876346837812265739970980202827485238414586892442822429233004808821082551675699702413952211939387589361654209039260795229', '--attack ecm2', '--timeout 60'])
        stdout, stderr = process.communicate()
        stdout, stderr
        conn.send(str.encode('Running RSA cracking\n'))
        conn.close()


    while True:

        conn, addr = s.accept()
        print('connected to: '+addr[0]+':'+str(addr[1]))

        start_new_thread(threaded_client,(conn,))