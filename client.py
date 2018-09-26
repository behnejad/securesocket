import ssl
import socket
import threading
import pprint



server_addr = ('127.0.0.1', 8443)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = False

print(ssl.get_server_certificate(('127.0.0.1', 8443), ssl_version=ssl.PROTOCOL_TLS))

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# context.load_verify_locations('cert.pem')
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
#     with context.wrap_socket(sock, server_hostname="127.0.0.1") as ssock:
#         print(ssock.version())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname="127.0.0.1")
ssl_sock.connect(('127.0.0.1', 8443))
pprint.pprint(ssl_sock.getpeercert())

print(ssl_sock.recv(100))
ssl_sock.send(b"Hi 2 U!")



