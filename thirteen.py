'''
	The problem is very simple.
	Multiplying two positive numbers result in a positive number.
	Multiplying two negative numbers result in a positive number.
	If we sort the array given we can compare the multiples of the two largest negative and positive numbers.
'''
def findMaxMult(items):
	'''
		default values for min and max elements of array
	'''
	min = [0, 0]
	max = [0, 0]

	size = len(items)

	'''
		Handles arrays with sizes less than 2
	'''
	if size < 2:
		if size == 0:	return [0, 0]

		return [1, items[0]]

	'''
		Cycles through array. Finds the max two elements and the min two elements.
		We don't need to sort the array since we only need one traversal (O(n)) to find the min/max elements.
	'''
	for item in items:
		if item < min[0]:
			min[1] = min[0]
			min[0] = item
		elif item < min[1]:	min[1] = item
		if item > max[1]:
			max[1] = max[0]
			max[1] = item
		elif item > max[0]:	max[0] = item

	'''
		Compares the multiples of both the min elements and max elements to see which multiple is bigger.
		Returns the biggest.
	'''
	return max if min[0] * min[1] < max[0] * max[1] else min

items = [-10, -3, 5, 6, -2, 0]
print( findMaxMult(items) )