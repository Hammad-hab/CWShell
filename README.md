# CWshell v1.0
## A shell for everyone
CW Shell is a remote shell made for controlling a computer through out the local Network. This is a complete tutorial.
### starting the server
On mac open the `Connecter.app`. On windows open `Connecter.exe`. After that wait until it gives you the ip address on which the server has been started.
Then on the client computer open `connect.app`/`connect.exe` and when it asks you for the IPV4 address, enter the IPV4 address of the server.
You are now successfully connected to the server. 
PS. 
The server may deny connection with your computer. Following is the procedure to solve that problem.
### CH: 1 Allowing Ip addresses

If the server denys connection with your computer you may recive an error. To solve this problem go to the `cwshell.config.json`.
In the array named whitelist, enter the ipv4 address of your client computer. After this you will be able to connect to the machine on which the server is running.
```
{
"whiteList": [
  ...
  "your_ipv4_address" <-
]
}

```
<b>cwshell.config.json</b>

### CH: 2 Settings and commands
CWShell allows you to run commands on the server. By default all the commands are treated as strings. To prevent this change your execution mode so that the server program considers your commands more than just standard strings. 
To change you execution mode to bash type $bash.
```
>>> echo Hello
>>> $bash
>>> echo Hello

```
<b>Client</b>



```
[CWSHELL] Active connections 1
127.0.0.1 says echo Hello
127.0.0.1 switched to bash mode
Hello
```
<b>Server</b>

<b>Note: In CWShell all commands begining with `$` sign are considerd as modes</b>
#### Other

`exit`: This command breaks the connection, it is equal to typing `-`


