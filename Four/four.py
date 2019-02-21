'''
	leftMostValue is the starting value of sorted array - 0 or 1
'''
def method_one(item, leftMostValue = 0):
	leftMostItems, rightMostItems = [], []

	for value in items:
		if value == leftMostValue:
			leftMostItems.append(value)
		else:
			rightMostItems.append(value)

	'''
		extend() is faster than iterating and adding the values individually in test cases
	'''
	leftMostItems.extend(rightMostItems)

	return leftMostItems


def method_two(items, leftMostValue = False):
	total = 0

	for value in items:
		if value == leftMostValue:
			total += 1

	sortedItems = [int(leftMostValue)] * total
	sortedItems.extend([int(not leftMostValue)] * (len(items) - total))
	
	return sortedItems


items = [1, 0, 1, 0, 1, 0, 0, 1] * 80000
#sortedItems = method_one(items)
sortedItems = method_two(items) # fastest method

print(sortedItems)