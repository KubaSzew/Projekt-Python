from book import Book
import csv

class Library:
    def __init__(self, books=None):
        self.books = [Book.from_dict(b) for b in books] if books else []

    def add_book(self, title, author, year, genre):
        book = Book(title, author, year, genre)
        self.books.append(book)
        print(f"✅ Dodano książkę: {title}")

    def list_books(self):
        for b in self.books:
            print(f"[{b.id[:8]}] {b.title} - {b.author} ({b.year}) [{b.genre}]")

    def search_books(self, keyword):
        found = [b for b in self.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]
        if found:
            for b in found:
                print(f"[{b.id[:8]}] {b.title} - {b.author} ({b.year})")
        else:
            print("🔍 Nic nie znaleziono.")

    def remove_book(self, book_id):
        before = len(self.books)
        self.books = [b for b in self.books if not b.id.startswith(book_id)]
        if len(self.books) < before:
            print("🗑️ Książka usunięta.")
        else:
            print("❌ Nie znaleziono książki.")

    def edit_book(self, book_id):
        for b in self.books:
            if b.id.startswith(book_id):
                b.title = input(f"Tytuł [{b.title}]: ") or b.title
                b.author = input(f"Autor [{b.author}]: ") or b.author
                b.year = input(f"Rok [{b.year}]: ") or b.year
                b.genre = input(f"Gatunek [{b.genre}]: ") or b.genre
                print("✅ Zaktualizowano.")
                return
        print("❌ Nie znaleziono książki.")

    def export_csv(self, filename):
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "author", "year", "genre"])
            writer.writeheader()
            for b in self.books:
                writer.writerow(b.to_dict())
