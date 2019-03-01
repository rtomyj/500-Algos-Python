def isXGreaterThanY(xInd):
	if x[xInd] > y[0]:
		return True


def reSort(items):
	for i in range(1, len(items)):
		if items[i - 1] > items[i]:
			temp = items[i - 1]
			items[i - 1] = items[i]
			items[i] = temp
		else:
			break


def swap(x, xInd, y):
	temp = x[xInd]
	x[xInd] = y[0]
	y[0] = temp

	reSort(y)





x = [1, 4, 7, 8, 10]
y = [2, 3, 9]
xInd = 0

while True:
	if isXGreaterThanY(xInd):
		swap(x, xInd, y)

	xInd += 1

	if xInd == len(x):
		break


print(x, y)