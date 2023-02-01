import ebooklib, re
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
        lines = []
        chapter = re.sub(r'\n(?=\n)', '', chapter)
        textLines = chapter.split('\n')
        wrapedLines = [textwrap.wrap(line, width=columns - 4, replace_whitespace=False) if line != '' else [""] for line in textLines]
        for w in wrapedLines :
            for line in w:
                lines.append(line)
        # lines = textwrap.wrap(chapter, width=columns - 4, replace_whitespace=False, break_long_words=False)
        for i in range(0, len(lines), rows - 5):
            # pages.append('\n'.join(lines[i:min(i + rows - 5, len(lines))]))
            pages.append(lines[i:min(i + rows - 5, len(lines))])
    return pages