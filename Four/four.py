items = [1, 0, 1, 0, 1, 0, 0, 1]
leftMostValue = 1	# determines whether sorted binray list starts with a 1 or 0
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
print(leftMostItems)
