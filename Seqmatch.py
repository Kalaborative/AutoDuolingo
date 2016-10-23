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
            foundApos = inpList.index(q)
            AposSliced = slice(inpList.index(q), (inpList.index(q) + 2))
            tText = inpList[AposSliced]
            AposWord = "".join(inpList[AposSliced])
            newList = [q for q in inpList if q not in tText]
            newList.insert(foundApos, AposWord)
            inpList = newList
    return inpList
