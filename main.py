import ebooklib
import sys
import argparse
from ebooklib import epub
from bs4 import BeautifulSoup
import argparse

def main() -> None:
    # Create Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--book",  help="Select a book to read")
    
    #? Show help if no pass anything or pass more than one book
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif len(sys.argv) > 2:
        print('You can only read one book at time')
        sys.exit(1)
    
    # Read EPUB
    book = epub.read_epub(str(sys.argv[2]))
    items = list(book.get_items())
    for item in items:
        getContent(item)

def getContent(item):
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            pages = soup.find_all('p')
            
            #print paragraph
            for page in pages:
                print(page.text)


if __name__ == "__main__":
  main()