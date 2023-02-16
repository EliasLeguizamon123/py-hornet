import os, json
from pathlib import Path

def checkIfDirectoryExistAndCreated() :
    # global output
    fileName = str(Path.home()) +'/hornet/saveData.json'
    if not os.path.exists(fileName) :
        os.system('cp ~/Desktop/work/epub/saveData.json ~/hornet/saveData.json')
        print('File created')
    elif not os.path.exists(str(Path.home()) + '/hornet') :
        os.system('mkdir ~/hornet/')
        print("directory created ok")
    else:
        print('All exist')

def saveBookInData(pathBook, bookTitle, actualPage, pagesLength) :
    checkIfDirectoryExistAndCreated()
    os.chdir(str(Path.home()) + '/hornet')
    # fileSavedData = open('saveData.json')
    # savedBooks = json.load(fileSavedData)['books']
    with open('saveData.json', 'r') as fileSavedData :
        savedBooks = json.load(fileSavedData)

    actualBook = { "bookTitle": bookTitle, "actualPage": actualPage, "pagesLength": pagesLength, "pathBook": pathBook }
    
    if len(savedBooks) < 1 :
        savedBooks.append(actualBook)
                
    for book in savedBooks :
        # Save actualPage
        if book['bookTitle'] == bookTitle :
            if book['actualPage'] != actualPage :
                book['actualPage'] = actualPage
        # Save new book
        elif book['bookTitle'] != bookTitle : 
            savedBooks.append(actualBook)
            break
        
    with open ('saveData.json', 'w+') as jsonFile: 
        jsonFile.write(json.dumps(savedBooks, indent=4))
        jsonFile.close()

