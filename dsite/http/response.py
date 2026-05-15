class Response:
    def __init__(self, content, status=200, headers=None):
        self.content = content
        self.status = status
        self.headers = headers or {}

    def to_http(self):
        return self.content
