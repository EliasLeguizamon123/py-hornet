import argparse, sys, os
from ebooklib import epub
from book import readEpub

# Globals
bookTitle = ''
book = ''
path = ''

def generateArgs():
    # Create Arguments
    global book, bookTitle, path 
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--book",  help="Select a book to read")
    # Invalid Arguments any
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # Invalid argument more than 1 book
    elif len(sys.argv) > 3:
        print('You can only read one book at time')
        sys.exit(1) 
    # Read EPUB
    book = epub.read_epub(str(sys.argv[2]))
    # Get title
    book.get_metadata('DC', 'title')
    # Get path
    path = os.path.abspath(str(sys.argv[2]))
    print(path)

    return readEpub(book)

