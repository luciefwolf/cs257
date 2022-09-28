#!/usr/bin/env python3

#Written by Yuelin Kuang & Lucie Wolf

import booksdatasource as bds
import sys

def run_command(args, source):
    if len(args) < 2:
        return 'Help'
    
    if args[1] == 'author':
        return run_author_command(args, source)
    
    if args[1] == 'title':
        return run_title_command(args, source)
        
    if args[1] == 'range':
        return run_range_command(args, source)

    return 'Help' #else, return help

def run_author_command(args, source):
    if len(args) == 2 or (len(args) == 3 and args[2][0] == '_'):
        return source.authors()
    if len(args) == 3:
        return source.authors(args[2])
    return 'Help'

def run_title_command(args, source):
    if len(args) == 2:
        return source.books()
    if len(args) == 3:
        if args[2][0] == '-':
            if args[2] == '-y' or args[2] == '--year':
                return source.books(sort_by = 'year')
            return source.books()
        if args[2] == '_':
            return source.books()
        return source.books(args[2])
    
    if len(args) == 4:
        if args[3][0] == '-':
            if args[3] == '-y' or args[3] == '--year':
                if args[2] == '_':
                    return source.books(sort_by = 'year')
                return source.books(args[2], sort_by = 'year')
            if args[2] == '_':
                return source.books()
            return source.books(args[2])
    
    return 'Help'

def run_range_command(args, source):
    if len(args) == 2:
        return source.books_between_years()
        
    if len(args) == 3:
        if args[2] == '_':
            return source.books_between_years()
        try: 
            return source.books_between_years(start_year = int(args[2]))
        except:
            return 'Help'

    if len(args) == 4:
        if args[2] == '_':
            if args[3] == '_':
                return source.books_between_years()
            try:
                return source.books_between_years(end_year = int(args[3]))
            except:
                return 'Help'
        if args[3] == '_':
            try:
                return source.books_between_years(start_year = int(args[2]))
            except:
                return 'Help'
        else:
            try:
                return source.books_between_years(start_year = int(args[2]), end_year = int(args[3]))
            except:
                return 'Help'
    return 'Help'

                
def print_output(output):
    print('\n\n')

    if output == 'Help':
        usage = open('usage.txt', 'r')
        print(usage.read())
        usage.close()

    elif output == []:
        print('Nothing found.')
    
    elif isinstance(output[0], bds.Author):
        for author in output:
            print(f'{author.given_name} {author.surname} ({author.birth_year}-{author.death_year})')
            for book in author.books:
                print(f'   {book.title}, published in {book.publication_year}.')
    
    else:
        for book in output:
            author_string = ''
            for author in book.authors:
                author_string += f'{author.given_name} {author.surname} and '

            print(f'{book.title}, published in {book.publication_year}, written by {author_string[:-5]}.')
    print('\n\n')







def main(args):
    source = bds.BooksDataSource('books1.csv')
    output = run_command(args, source)
    print_output(output)
    


if __name__ == '__main__':
    main(sys.argv)