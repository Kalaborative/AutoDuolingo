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
