'''
	This challange has a lot of solutions from the website it was pulled from.
	However I beleive the solution below is the simplest and easiest to grasp.
'''

def method_one(items):
	values = set()
	for item in items:
		if item in values:
			print('dup value is ', item)
			return
		values.add(item)

items = [1, 2, 2, 3, 4]
method_one(items)