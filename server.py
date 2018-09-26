import ssl
import socket
import threading
from typing import TypeVar, Iterable, Tuple, Sequence

server_addr = ('127.0.0.1', 8443)

# def test(ip: str, port: int) -> socket.AddressInfo:
#     pass
#
# def test2(ip, port): ...
#
# def sumList(l: Sequence[int]):
#     pass
#
# print(test.__annotations__)
# print(test2.__annotations__)
# print(sumList.__annotations__)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain('cert.pem', 'key.pem')
# context.verify_mode = ssl.CERT_REQUIRED
# context.check_hostname = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8443))
s.listen(10)
# ssl_sock = context.wrap_socket(s, do_handshake_on_connect=True, server_side=True)

# with context.wrap_socket(s, server_side=True) as ssock:
#     conn, addr = ssock.accept()
#
#     while 1:
#         client, add = ssock.accept()
#         client.send(b"Hello World!")
#         print(client.recv(100))

while True:
    newsocket, fromaddr = s.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        connstream.send(b"Hello World!")
        print(connstream.recv(100))
    finally:
        # connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()


