import re
import ebooklib
from bs4 import BeautifulSoup
import os

def readEpub(book): 
    chapters = []
    items = list(book.get_items())
    output = []
    
    chapters = getContent(items)
    
    for chapter in chapters :
        soup = BeautifulSoup(chapter, 'html.parser')
        # text = soup.find_all(text = True)
        text = soup.get_text()
        output.append(text)
    #     chapterText = []
    #     for t in text :
    #         if t.parent.name not in ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script'] :
    #             chapterText.append(str(t))
    #     output.append(''.join(chapterText))
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
        page = []
        chapter = re.sub(r'\n(?=\n)', '', chapter)
        for y in range(rows - 3):
            if y * columns >= len(chapter):
                break
            line = ''
            for x in range(columns):
                index = y * columns + x
                
                if index >= len(chapter):
                    break
                line += chapter[index]
                
            page.append(line)
        pages.append('\n'.join(page))
    
    return pages