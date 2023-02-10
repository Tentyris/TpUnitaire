import unittest

from Library import *

class BookTests(unittest.TestCase):
    def setUp(self):
        self.book = Book("To Kill a Mockingbird", "Harper Lee")

    def test_check_out(self):
        self.book.check_out()
        self.assertTrue(self.book.is_checked_out)

    def test_check_in(self):
        self.book.check_in()
        self.assertFalse(self.book.is_checked_out)

class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book)

    def test_add_book(self):
        self.assertIn(self.book, self.library.books)

    def test_check_out_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.assertTrue(self.book.is_checked_out)

    def test_check_in_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.library.check_in_book("To Kill a Mockingbird")
        self.assertFalse(self.book.is_checked_out)

class ClientTests(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book)
        self.client = Client("John Doe")

    def test_check_out_book(self):
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertIn(self.book, self.client.checked_out_books)

    def test_check_in_book(self):
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.client.check_in_book(self.library, "To Kill a Mockingbird")
        self.assertNotIn(self.book, self.client.checked_out_books)

if __name__ == '__main__':
    unittest.main()