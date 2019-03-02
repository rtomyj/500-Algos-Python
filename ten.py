def swap_element(x, xInd, y):
	temp = x[xInd]
	x[xInd] = y[0]
	y[0] = temp

'''
	Uses thefact that y is always sorted to keep both x and y sorted.
	If x[index] is greater than y[0] then we swap. After which we resort the array.
'''
def dual_sort(x, y):
	for index in range(0, len(x)):
		if x[index] > y[0]:
			swap_element(x, index, y)
			y.sort()

x = [1, 4, 7, 8, 10]
y = [2, 3, 9]

dual_sort(x, y)
print(x)
print(y)