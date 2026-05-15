class Model:
    _db = []

    def save(self):
        self._db.append(self)


class TextColumn:
    def __init__(self, max_length=None):
        self.max_length = max_length
        self.value = None
