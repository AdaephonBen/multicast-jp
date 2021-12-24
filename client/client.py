import socket
import time

MCAST_GRP = '224.3.29.71'
MCAST_PORT = 5007
MULTICAST_TTL = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
emergency_info = {
    "location": "60N 70W",
    "metadata": "Person falling"
}

time.sleep(3)

sock.sendto(bytes(str(emergency_info), 'utf-8'), (MCAST_GRP, MCAST_PORT))
print("Emergency reported at time {}".format(time.time_ns()))
