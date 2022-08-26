# importing modules
import os

# for Mac or Linux
os.system("clear")
# for DOS
os.system("cls")

import socket as s
import threading as t
from termcolor import colored
import socket as s
import json as j

def cwLog(type="suc", text="default text",pp=""):
    color = ""
    c2 = ""
    if (type == "suc"):
        color = "green"
        c2 = "cyan"
    elif (type == "err") :
        color = "red"
        c2 = "red"
    elif (type == "wr"):
        color = "yellow"
        c2 = "yellow"
        
    print(colored(f"{pp}[CWSHELL]", color, attrs=["bold"]), colored(text, c2, attrs=["bold"]))      

def whoami() : return s.gethostbyname(s.gethostname())

def ip(ipstring):
    return colored(ipstring, "cyan") 

def keyword(keywstring): 
    return colored(keywstring, "blue")


def detectWhitelistedIP(ip):
    CONFIG = j.loads(open("cwshell.config.json").read())["whitelist"]
    if (ip in CONFIG):
        return True
    else :
        return False
    
ips = ["192.168.43.70","192.168.43.133","192.168.43.202","192.168.43.50"]


def send(client: s.socket, message, en="utf-8"):
    client.send(bytes(message, "utf-8"))
    
# initailzing server information
PORT = 5050
SERVER = s.gethostbyname(s.gethostname())
ADDRESS = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT = "-"
# creating a socket
server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(c: s.socket, a):
    cwLog("suc", "New connection {a}")
    connected = True
    exeBash = False
    while connected:
        try:
            message = c.recv(1024).decode("utf-8")
            if (message.__len__() > 0):
                if (message == DISCONNECT):
                    cwLog("err", f"{a[0]} disconnected")
                    connected = False
                    break
                if (message.lower() == "$bash"):
                    exeBash = True
                    print(f"{ip(a[0])} switched to {keyword('bash mode')}")
                if (exeBash == True):
                    os.system(message)
                else:
                    print(f"{ip(a[0])} says {message}")
                if (message.lower() == "$std"):
                    print(f"{ip(a[0])} switched to {keyword('standard mode')}")
                    exeBash = False
                pass
            pass
        except:
            cwLog("err", f"Failed to recive from {a[0]}")
            pass
        pass
    c.close()
    pass


def start():
    server.listen()
    running = True
    while running:
       try:
        conn, addr = server.accept()
        if (detectWhitelistedIP(addr[0])):
            connection = t.Thread(target=handle_client, args=(conn, addr))
            connection.start()
            send(conn, "202")
            cwLog("suc", f"Active connections: {t.active_count() - 1}")
        else:
            send(conn, "403")
            cwLog("err", f"Unauthorized client detected {addr[0]}")
            cwLog("err", f"Disconnecting {addr[0]}")
            try:
                conn.close()
            except Exception as e:
                cwLog(
                    "err", f"Failed to disconnect {addr[0]} due to the following error: \n{e} \nclosing the server to prevent further damage")
                exit(0)
       except KeyboardInterrupt as KI:
         server.close()



cwLog("suc", f"Starting server at {SERVER}:{PORT}")
start()
