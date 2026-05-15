# dsite/http/request.py

from urllib.parse import parse_qs

class Request:
    """
    Oggetto Request di DSite.
    Contiene dati HTTP (GET, POST, headers).
    """

    def __init__(self, method, path, headers, body):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body

        self.GET = self._parse_get()
        self.POST = self._parse_post()

    def _parse_get(self):
        if "?" not in self.path:
            return {}

        query_string = self.path.split("?")[1]
        return {k: v[0] for k, v in parse_qs(query_string).items()}

    def _parse_post(self):
        if self.method != "POST":
            return {}

        try:
            return {k: v[0] for k, v in parse_qs(self.body).items()}
        except:
            return {}
