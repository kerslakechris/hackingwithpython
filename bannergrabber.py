import socket

Target_IP = input("Target IP: ")
Target_port = input("Target port: ")

print("Target IP: " + Target_IP)
print("Target Port: " + Target_port)


socket.setdefaulttimeout(2)
s = socket.socket()
s.connect((Target_IP, Target_port))
ans = s.recv(1024)
print(ans)
