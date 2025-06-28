import uuid

class Book:
    def __init__(self, title, author, year, genre, id=None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["year"], data["genre"], data["id"])
