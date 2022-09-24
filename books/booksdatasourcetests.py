'''
   Written by Lucie Wolf and Yuelin Kuang 
   23 September 2022
   
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
         
    def test_commas(self):
        books = self.data_source.books('Fine, Thanks')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Fine, Thanks'))

    def test_unique_book(self):
        books = self.data_source.books('Omoo')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Omoo'))

    def test_author_search(self):
        authors = self.data_source.authors('J')
        self.assertTrue(len(authors) == 3)
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
        self.assertTrue(authors[1] == Author('Baldwin', 'James'))
        self.assertTrue(authors[2] == Author('Bujold', 'Lois McMaster')) 

    def test_book_search_titlesort(self):
        books = self.data_source.books('Al')
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0] == Book('All Clear'))
        self.assertTrue(books[1] == Book('If Beale Street Could Talk'))
        self.assertTrue(books[2] == Book('The Tenant of Wildfell Hall'))
    
    def test_book_search_yearsort(self):
        books = self.data_source.books('Al', sort_by = 'year')
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0] == Book('The Tenant of Wildfell Hall'))
        self.assertTrue(books[1] == Book('If Beale Street Could Talk'))
        self.assertTrue(books[2] == Book('All Clear'))
        
    def test_book_search_authorsort(self):
        books = self.data_source.books('Al', sort_by = 'author')
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0] == Book('If Beale Street Could Talk'))
        self.assertTrue(books[1] == Book('The Tenant of Wildfell Hall'))
        self.assertTrue(books[2] == Book('All Clear'))
    
    def test_range(self):
        years = self.data_source.books_between_years(2010,2016)
        self.assertTrue(len(years) == 3)
        self.assertTrue(years[0] == Book('All Clear')) #2010, comes first because tie broken by title
        self.assertTrue(years[1] == Book('Blackout')) #2010
        self.assertTrue(years[2] == Book('Girls and Sex')) #2016
      
    def test_all_authors(self):
        authors = self.data_source_tiny.authors()
        self.assertTrue(len(authors) == 3)
        self.assertTrue(authors[0] == Author('Lewis', 'Sinclair'))
        self.assertTrue(authors[1] == Author('Murakami', 'Haruki'))
        self.assertTrue(authors[2] == Author('Orenstein', 'Peggy'))
      
    def test_all_books(self):
        books = self.data_source_tiny.books()
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0] == Book('1Q84'))
        self.assertTrue(books[1] == Book('Elmer Gantry'))
        self.assertTrue(books[2] == Book('Schoolgirls'))
    
    def test_all_range(self):
        books = self.data_source_tiny.books_between_years()
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0] == Book('Elmer Gantry'))
        self.assertTrue(books[1] == Book('Schoolgirls'))
        self.assertTrue(books[2] == Book('1Q84'))

    def test_accented_letters(self):
        authors = self.data_source.authors('Marquez')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Márquez', 'Gabriel García'))
    
    def test_author_name_tie(self):
        authors = self.data_source.authors('Brontë')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Brontë', 'Ann'))
        self.assertTrue(authors[1] == Author('Brontë', 'Charlotte'))
        self.assertTrue(authors[2] == Author('Brontë', 'Emily'))
    
    def test_invalid_range(self):
        years = self.data_source.books_between_years(2050,2070)
        self.assertTrue(len(years) == 0)
    
    def test_invalid_book(self):
        books = self.data_source.books('dfhssfd')
        self.assertTrue(len(books) == 0)
         
    def test_invalid_author(self):
        authors = self.data_source.authors('dfhssfd')
        self.assertTrue(len(authors) == 0)
    

if __name__ == '__main__':
    unittest.main()
