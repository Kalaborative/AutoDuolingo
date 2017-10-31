from difflib import SequenceMatcher


def similarity(sing, itr):
    queue = {}
    a, b, c = itr
    compareA = SequenceMatcher(None, sing, a).ratio()
    compareB = SequenceMatcher(None, sing, b).ratio()
    compareC = SequenceMatcher(None, sing, c).ratio()
    queue[a] = compareA
    queue[b] = compareB
    queue[c] = compareC
    return max(queue, key=queue.get)


def apostrophe_checker(inpList):
    inpList = list(inpList)
    for q in inpList:
        if "'" in q:
            apostrophe_index = inpList.index(q)
            AposSliced = slice(apostrophe_index, (apostrophe_index + 2))
            tText = inpList[AposSliced]
            # Apos Word is the word found and concatenated with apostrophe in it.
            AposWord = "".join(inpList[AposSliced])
            # New List is the original list with the apostrophe word left out
            newList = [q for q in inpList if q not in tText]
            newList.insert(apostrophe_index, AposWord)
            # replace the working list with the new one
            inpList = newList
    return inpList
  

