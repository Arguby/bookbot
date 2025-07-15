def word_count(text):
    wordList = text.split()
    numWords = len(wordList)
    return numWords

def repeats(text):
    text = text.lower()
    dictRep = {}
    for char in text:
        if char in dictRep:
            dictRep[char] += 1 
        else:
            dictRep[char] = 1
    return dictRep

def sort_on(items):
    return items["num"]

def sortedList(dictRep):
    listDic = []
    for key, val in dictRep.items():
        listDic.append({"char": key, "num": val})
    listDic.sort(reverse=True, key=sort_on)
    return listDic