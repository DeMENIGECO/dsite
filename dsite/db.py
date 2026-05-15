# dsite/db.py

class QuerySet(list):
    def all(self):
        return self

    def get(self, id):
        for obj in self:
            if getattr(obj, "id", None) == id:
                return obj
        return None


class Model:
    _db = QuerySet()
    _id_counter = 1

    def save(self):
        if not hasattr(self, "id"):
            self.id = Model._id_counter
            Model._id_counter += 1

        Model._db.append(self)

    @classmethod
    def objects(cls):
        return cls._db


class TextColumn:
    def __init__(self, max_length=None):
        self.max_length = max_length
