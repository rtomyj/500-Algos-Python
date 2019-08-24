import random
from sys import path
path.append('libs')
from lists import swap_elements


def randomize(items):
	used = set()
	while len(used) + 1 < len(items):
		left, right = -1, -1
		while left == -1 and left not in used:
			left = random.randint(0, len(items) - 1)
		while right == -1 and right not in used:
			right = random.randint(0, len(items) - 1)

		used.add(left)
		used.add(right)
		swap_elements(items, left, right)

		return items

items = [ 1, 2, 3, 4, 5, 6 ]
print(randomize(items))







