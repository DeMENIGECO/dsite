from urllib.parse import parse_qs


class Request:
    def __init__(self, method, path, headers, body):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body

        self.GET = self._get()
        self.POST = self._post()

    def _get(self):
        if "?" not in self.path:
            return {}

        query = self.path.split("?")[1]
        return {k: v[0] for k, v in parse_qs(query).items()}

    def _post(self):
        if self.method != "POST":
            return {}

        return {k: v[0] for k, v in parse_qs(self.body).items()}
