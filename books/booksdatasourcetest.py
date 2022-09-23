from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_books_search(self):
        books = self.data_source.books("A")
        self.assertTrue(len(books) == 23)
        self.assertTrue(books[0].title == "All Clear")

    def test_author_search(self):
        authors = self.data_source.authors("J")
        self.assertTrue(len(authors) == 3)
        self.assertTrue(authors[0].surname == "Austen")

    def test_search_between_years(self):
        books = self.data_source.books_between_years(2000, None)
        self.assertTrue(len(books) == 9)



    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))
        self.assertTrue(authors[0].birth_year == 1948)
        self.assertTrue(authors[0].death_year == 2015)

    def test_commas_in_book_titles(self):
        title = self.data_source.books("Fine, Thanks")
        self.assertTrue(len(title) == 1)


if __name__ == '__main__':
    unittest.main()
