#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None, books=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year
        self.books = books

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        books = []
        authors = []

        with open(books_csv_file_name) as books_csv:
            books_csv = csv.reader(books_csv, delimiter=',')

            for row in books_csv:
                title = row[0]
                year = row[1]
                book = 0
                book = Book(title=title, publication_year=year, authors=[])

                authors_in_book = row[2].split(' and ')
                for i in range(len(authors_in_book)):
                    authors_in_book[i] = authors_in_book[i].split(' ')

                for author in authors_in_book:

                    surname = author[-2]
                    list_of_given_names = [name for name in author[:-2]]
                    given_name = ' '.join(list_of_given_names)

                    already_in_list = False
                    for other_author in authors:
                        if Author(surname = surname, given_name = given_name) == other_author:
                            already_in_list = True
                            other_author.books.append(book)

                            book.authors.append(other_author)

                    if not already_in_list:
                        years = author[-1][1:-1].split('-')
                        if years[0] == '':
                            birth_year = None
                        else:
                            birth_year = int(years[0])
                        if years[1] == '':
                            death_year = None
                        else:
                            death_year = int(years[1])

                        author_object = Author(surname=surname, given_name=given_name, birth_year=birth_year, death_year=death_year, books=[book])
                        authors.append(author_object)
                        book.authors.append(author_object)
            
            
                books.append(book)
                
                


    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        return []

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        return []

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        return []


def main():
    b = BooksDataSource('books1.csv')

if __name__ == '__main__':
    main()
