import ebooklib
from bs4 import BeautifulSoup

def readEpub(book): 
    chapters = []
    items = list(book.get_items())
    output = []
    
    chapters = getContent(items)
    
    for chapter in chapters :
        soup = BeautifulSoup(chapter, 'html.parser')
        text = soup.find_all(text = True)
        chapterText = []
        for t in text :
            if t.parent.name not in ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script'] :
                chapterText.append(str(t))
        output.append(''.join(chapterText))
    return output
    
def getContent(items):
    chapters = []
    for item in items:
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters