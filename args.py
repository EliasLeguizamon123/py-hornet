import argparse, sys, os
from ebooklib import epub
from book import readEpub

def generateArgs():
    # Create Arguments
    parser = argparse.ArgumentParser('Hornet is a cli/terminal epub reader made in python')
    parser.add_argument("-b", "--book", help="Select one book to read", required=False, nargs='+', type=str)
    args = parser.parse_args()
    print(args)
    if args.book is not None:
        try :
            book = epub.read_epub(args.book)
            bookTitle = book.get_metadata('DC', 'title')
            bookPath = os.path.abspath(str(sys.argv[2]))
            return {"content": readEpub(book), "bookPath": bookPath, "bookTitle": bookTitle[0][0] }
        except :
            print('This is not a epub file')
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)
    
generateArgs()
