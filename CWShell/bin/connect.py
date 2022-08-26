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
    
import socket as s
from ipaddress import ip_address
def REPL():
    server = input(keyword("connect to: "))
    if (server):
      try :
          IP = ip_address(server)
      except ValueError as VE:
         cwLog("err", "INVALID IPV4 ADDRESS")
         REPL()
      else:
        return server
    else:
        cwLog("wr","Please enter a valid IPV4 address")
        REPL()
PORT = 5050
SERVER = REPL()
ADDRESS = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
isConnected = True

client = s.socket(s.AF_INET, s.SOCK_STREAM)
try :
 client.connect(ADDRESS)
 STATUS = int(client.recv(1024).decode("utf-8"))
 if(STATUS == 403):
     cwLog("err", f"CWSHELL@{SERVER} denied connection with your device")
     isConnected = False
 elif (STATUS == 202):
     cwLog(text=f"Successfully connected to CWSHELL@{SERVER}")
except Exception as e:
    cwLog("err", e)
def send(msg) :
    try:
        client.send(bytes(msg, "utf-8"))
    except Exception as e:
        cwLog("err", e)
        send("-")
        exit(0)


while isConnected :
    try:
        command = input(keyword(">>> "))
        
        if (command.strip() == "exit") :
            send("-")
            cwLog("err", "You Disconnected")
            exit(0)
        else :
            send(command)
    except KeyboardInterrupt as KI:
        cwLog("wr", "If you want to disconnect please use the standard method", "\n")    
    