import ebooklib
from ebooklib import epub
import sys
from bs4 import BeautifulSoup

def readEpub(book): 

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