import argparse
import sys
import ebooklib
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
    
    # Read EPUB
    book = epub.read_epub(str(sys.argv[2]))

    readEpub(book)
