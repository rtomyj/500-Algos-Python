'''
	Loops through bin array. If leftMostValue is spotted it is added to the left side of the array. To keep track of where on the left we want it leftMostCount is used.

	After the first loop is done, the left side of the array is sorted. To sort the right side we use the second loop to add elements equal to len - leftMostCount to push the opposite of leftMostValue.
'''
def fill_and_add(items, leftMostValue = 0):
	leftMostCount = 0
	size = len(items)

	for item in items:
		if item == leftMostValue:
			items[leftMostCount] = leftMostValue
			leftMostCount += 1

	for index in range(leftMostCount, size):
		items[index] = int(not leftMostValue)


'''
	Creates two arrays. One with the left side of the sorted array, and the other with the right side. Both are then merged and returned as a new array.
'''
def sort_and_merge_two_bin_arrays(items, leftMostValue = False):
	leftMostCount = items.count(leftMostValue)

	sortedItems = [int(leftMostValue)] * leftMostCount
	sortedItems.extend([int(not leftMostValue)] * (len(items) - leftMostCount))
	
	return sortedItems


items = [1, 0, 1, 0, 1, 0, 0, 1]
fill_and_add(items, leftMostValue=1)
print(items)
sortedItems = sort_and_merge_two_bin_arrays(items) # fastest method
print(sortedItems)