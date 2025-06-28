import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book("Test Title", "Author", "2000", "Drama")

    def test_add_book(self):
        self.assertEqual(len(self.lib.books), 1)

    def test_search_books(self):
        result = [b for b in self.lib.books if "Test" in b.title]
        self.assertEqual(len(result), 1)

    def test_remove_book(self):
        book_id = self.lib.books[0].id[:8]
        self.lib.remove_book(book_id)
        self.assertEqual(len(self.lib.books), 0)

if __name__ == "__main__":
    unittest.main()
