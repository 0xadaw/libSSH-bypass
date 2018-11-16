import sys
import time
import ipaddress
import paramiko
import socket

class colors:
    timeout ="\033[1;31m"

def checkthis(ip):
    try:
        sock = socket.create_connection((ip, 22), timeout=0.5000)
        sock.settimeout(0.5000)
        banner = str(sock.recv(1024))
        if banner.find("libssh-0.6"):
            sock.close()
            f.write("%s\n" % (ip))
        return print("SUCCESS !!! ip %s has version %s" % (ip, banner))
    except (socket.timeout,socket.error) as e:
        return print("{timeout}[*] {ipadd} has timed out".format(timeout=colors.timeout, ipadd=ip))


f = open("ipaddresslist.txt", "w+")

for ip in ipaddress.IPv4Network(sys.argv[1]):
    ip = str(ip)
    checkthis(ip)
f.close()
#message = paramiko.message.Message()

#transport = paramiko.transport.Transport(socket)
#transport.start_client()

#message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)

#transport._send_message(message)

#command = transport.open_session(timeout=1.50000)
# command.exec_command("id")
# out = command.makefile("rb", 2048)
# output = out.read()
# print(output)


