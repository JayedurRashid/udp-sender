# A simple program to send udp packet to given destination but fixed port:5004.

import socket
import time
import sys

LOCAL_IP = "0.0.0.0"
UDP_PORT = 5004
MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((LOCAL_IP, 50004))

def send_infinitely(destaddress):
	while True:
		sock.sendto(MESSAGE, (destaddress, UDP_PORT))
		print("A packet has been sent!")
		time.sleep(1.0)


if __name__ == '__main__':
        print(sys.argv)
        
	if len(sys.argv) < 2:
		print('no destination address is provided.')
		exit()
	elif len(sys.argv[1]) == 0:
		print('no destination address is provided.')
		exit()

	dest = sys.argv[1]
	send_infinitely(dest)
