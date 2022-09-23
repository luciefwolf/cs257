'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')
        self.data_source_tiny = BooksDataSource('tiny.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    def test_unique_book(self):
        books = self.data_source.books('Omoo')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Omoo'))

    def test_author_search(self):
        authors = self.data_source.authors('J')
        self.assertTrue(len(authors) == 3)
        self.assertTrue(authors[0] == Author('Austen, Jane'))
        self.assertTrue(authors[1] == Author('Baldwin, James'))
        self.assertTrue(authors[2] == Author('Bujold, Lois McMaster'))

    def test_book_search(self):
        books = self.data_source.books('J')

if __name__ == '__main__':
    unittest.main()
