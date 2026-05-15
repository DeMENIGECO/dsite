# dsite/server.py

import socket
from dsite.http.request import Request
from dsite.urls import urlpatterns


def find_view(path):
    for url, view in urlpatterns:
        if url == path:
            return view
    return None


def handle_request(client_socket):
    request_data = client_socket.recv(4096).decode()

    if not request_data:
        return

    lines = request_data.split("\r\n")

    method, full_path, _ = lines[0].split()

    headers = {}
    i = 1
    while lines[i] != "":
        key, value = lines[i].split(": ", 1)
        headers[key] = value
        i += 1

    body = lines[-1]

    request = Request(method, full_path, headers, body)

    path = full_path.split("?")[0]

    view = find_view(path)

    if view:
        response = view(request)
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n404 Not Found"

    client_socket.send(response.encode())
    client_socket.close()


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8000))
    server.listen(5)

    print("[DSite] Server avviato su http://127.0.0.1:8000")

    while True:
        client_socket, addr = server.accept()
        handle_request(client_socket)
