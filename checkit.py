import sys
import time
import ipaddress
import paramiko
import socket


with open("ipaddresslist.txt", 'r') as fh:
    for line in fh.readlines():
        try:
                lines = str(line.strip('\n'))
                s = socket.create_connection((lines, 22), timeout=10.50000)
                s.settimeout(10.50000)

                msg = paramiko.message.Message()
                t = paramiko.transport.Transport(s)
                t.start_client()

                msg.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
                t._send_message(msg)
                c = t.open_session(timeout=10.50000)
                s.close()
                print("SUCCESS !!! ip %s has version %s" % (ip))

        except (socket.timeout, socket.error) as e:
                print(e)
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


