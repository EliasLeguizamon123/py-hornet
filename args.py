import argparse, sys, os
from ebooklib import epub
from book import readEpub

def generateArgs():
    # Create Arguments
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

    book = epub.read_epub(str(sys.argv[2]))
    bookTitle = book.get_metadata('DC', 'title')
    bookPath = os.path.abspath(str(sys.argv[2]))
    return {"content": readEpub(book), "bookPath": bookPath, "bookTitle": bookTitle }
