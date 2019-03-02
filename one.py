#!/usr/bin/python3
'''
	Uses the fact that dicts are hashed in python to store values of items as keys and their index as a value.

	Traverses the array and subtracts sum - current value. If that result is in the dict then it means we iterated over it already and we can print out the sum. 
'''
def hash_and_find(items, sum):
	hash = dict()
	for index, item in enumerate(items):
		operand = sum - item
		if operand in hash:
			print('{0} (index={3})+ {1} (index={4}) = {2}'.format(item, operand, sum, index, hash[operand]))

		hash[item] = index


items = [8, 7, 2, 5, 3, 1]
sum = 10
hash_and_find(items, sum)