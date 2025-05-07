![alt text](https://github.com/Nacom-sys/Netpreter/blob/main/NetpreterLogo.png?raw=true)<br>
![alt text](https://github.com/Nacom-sys/Netpreter/blob/main/NetpreterAscii.png?raw=true)<br>
<br>
#**Simple Python LAN backdoor using flask**
**Explanation:**
<br>
Reverse shell on private network:
<br>
Using Server.py you will host a flask server, to which the infected computers will connect.
<br>
By using Shell.cmd (which just helps make the usage of the Shell easier) you can specify the target and what you would like to do:
<br>
**Current Features:**
<br>
*-Encrypt:*
<br>
Uses XOR to encrypt files, specify a file (any file you want), then the script will calculate the hash code using hashlib and then use the Hash as the Key to encrypt the files using XOR.

