items = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]

from sys import path
path.append('libs')
from lists import swap_elements

def swap_sort(items, lookingFor, unsortedInd):
	for ind in range(unsortedInd, len(items)):
		if lookingFor == items[ind]:
			swap_elements(items, unsortedInd, ind)
			unsortedInd += 1

	return unsortedInd

def sort(items, asc=True):
	if asc:
		leftMostValue = 0
		increment = 1
	else:
		leftMostValue = 2
		increment = -1

	unsortedInd = swap_sort(items, leftMostValue, 0)
	swap_sort(items, leftMostValue + increment, unsortedInd)

sort(items)
print(items)

sort(items, asc=False)
print(items)

