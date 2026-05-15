# dsite/db.py

import json
from pathlib import Path


DB_FILE = Path("dsite_db.json")


# =========================
# QUERYSET
# =========================

class QuerySet:
    def __init__(self, data):
        self.data = data

    def all(self):
        return self.data

    def get(self, id):
        for obj in self.data:
            if getattr(obj, "id", None) == id:
                return obj
        return None


# =========================
# MODEL BASE
# =========================

class Model:
    _db = []
    _id_counter = 1

    def __init__(self):
        self.id = None

    # -------------------------
    # SAVE
    # -------------------------
    def save(self):
        if self.id is None:
            self.id = Model._id_counter
            Model._id_counter += 1

        # evita duplicati
        self.delete_from_memory()

        Model._db.append(self)
        self._save_to_disk()

    # -------------------------
    # DELETE
    # -------------------------
    def delete(self):
        self.delete_from_memory()
        self._save_to_disk()

    def delete_from_memory(self):
        cls = self.__class__
        cls._db = [obj for obj in cls._db if obj.id != self.id]

    # -------------------------
    # CLASS API
    # -------------------------
    @classmethod
    def objects(cls):
        return QuerySet(cls._db)

    # -------------------------
    # PERSISTENZA FILE
    # -------------------------
    @classmethod
    def _save_to_disk(cls):
        data = []

        for obj in cls._db:
            item = obj.__dict__.copy()
            data.append(item)

        DB_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def load_from_disk(cls):
        if not DB_FILE.exists():
            return

        try:
            data = json.loads(DB_FILE.read_text(encoding="utf-8"))

            for item in data:
                obj = cls()
                obj.__dict__.update(item)

                if obj.id and obj.id >= cls._id_counter:
                    cls._id_counter = obj.id + 1

                cls._db.append(obj)

        except:
            cls._db = []


# =========================
# FIELD SYSTEM (base)
# =========================

class Field:
    def __init__(self, label=""):
        self.label = label


class TextColumn(Field):
    def __init__(self, max_length=None, label=""):
        super().__init__(label)
        self.max_length = max_length
