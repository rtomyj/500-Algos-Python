'''
	Uses a dict to keep track of number occurrences. If dict has a key then it means the value was seen before in items array (dup).
'''
def hash_and_grab(items):
	values = dict()
	for item in items:
		if item in values:
			print('dup value is ', item)
			return
		values[item] = 1


'''
	Array is sorted. After which the adjacent elements are checked. Sorted adjacent elements are either dups or not.
'''
def sort_and_find(items):
	items.sort()
	for index, val in enumerate(items):
		if index == 0: continue
		if val == items[index -1]:	print('dup value is ', val)

items = [1, 2, 3, 4, 2]
hash_and_grab(items)
sort_and_find(items)