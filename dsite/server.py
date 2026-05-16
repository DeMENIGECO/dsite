# dsite/server.py

import socket
from dsite.http.request import Request
from dsite.urls import urlpatterns


def resolve(path):

    for route, view in urlpatterns:
        if route == path:
            return view

    return None


def handle(client):

    raw = client.recv(4096).decode()

    if not raw:
        client.close()
        return

    parts = raw.split("\r\n")

    method, full_path, _ = parts[0].split()

    path = full_path.split("?")[0]

    headers = {}
    i = 1

    while i < len(parts) and parts[i] != "":
        k, v = parts[i].split(": ", 1)
        headers[k] = v
        i += 1

    body = ""

    if "\r\n\r\n" in raw:
        body = raw.split("\r\n\r\n", 1)[1]

    request = Request(method, full_path, headers, body)

    view = resolve(path)

    if view:

        response = view(request)

        http_response = (
            f"HTTP/1.1 {response.status} OK\r\n"
            f"Content-Type: text/html\r\n\r\n"
            f"{response.to_http()}"
        )

        client.send(http_response.encode())

    else:

        client.send(b"HTTP/1.1 404 Not Found\r\n\r\n404 Not Found")

    client.close()


def run():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8000))
    server.listen(5)

    print("[DSite] Server attivo su http://127.0.0.1:8000")

    while True:
        client, addr = server.accept()
        handle(client)
