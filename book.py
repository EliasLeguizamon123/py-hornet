import ebooklib
from bs4 import BeautifulSoup
import textwrap

def readEpub(book): 
    chapters = []
    items = list(book.get_items())
    output = []
    chapters = getContent(items)
    for chapter in chapters :
        soup = BeautifulSoup(chapter, 'html.parser')
        text = soup.get_text()
        output.append(text)
    return output
    
def getContent(items):
    chapters = []
    for item in items:
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

def createPages(output, size):
    columns = size[1]
    rows = size[0]
    pages = []
    for chapter in output:
        lines = textwrap.wrap(chapter, width=columns)
        for i in range(0, len(lines), rows):
            pages.append('\n'.join(lines[i:min(i + rows, len(lines))]))
    return pages