from sys import path
path.append('libs')
from lists import swap_elements

'''
	Sorts an array partially by swapping a desired element with an index not yet sorted.
	Ideally to sort an array this method will be called multiple times.
	If there are n possible values for an element then this method should be called n-1 times.
'''
def swap_sort(items, lookingFor, unsortedInd):
	for ind in range(unsortedInd, len(items)):
		'''
			Swaps current value with the value at the unsorted index if current value is the current wanted value.
		'''
		if lookingFor == items[ind]:
			swap_elements(items, unsortedInd, ind)
			unsortedInd += 1	# array is partially sorted, increment index to get to new unsorted index

	return unsortedInd


'''
	Sorts an array that contains 0's, 1's and 2's.
	Sorting should use constant space and be done in linear time.
'''
def sort(items, asc=True):
	'''
		Default values for ascending sort.
	'''
	if asc:
		leftMostValue = 0
		increment = 1
	else:
		'''
			Changes values for descending sort.
		'''
		leftMostValue = 2
		increment = -1

	unsortedInd = swap_sort(items, leftMostValue, 0)	# partially sorts array (either 0 (asc) or 2 (desc) are all sorted)
	swap_sort(items, (leftMostValue + increment), unsortedInd)	# array is sorted


'''
	Main functionality
	Completes algorithm 9.
'''
items = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]

sort(items)	# sorts 0's, 1's and 2's in ascending order
print(items)

sort(items, asc=False)	# sorts 0's, 1's and 2's in descending order
print(items)