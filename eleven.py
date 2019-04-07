x = [0, 2, 0, 3, 0, 5, 6, 0, 0]
y = [1, 8, 9, 10, 15]

yInd = 0
emptyCells = []
for xInd, xEle in enumerate(x):
	if xEle == 0:
		emptyCells.append(xInd)
	else:
		if xEle > y[yInd]:
			if len(emptyCells) == 0:
				temp = x[xInd]
				x[xInd] = y[yInd]
				y[yInd] = temp
			# if there are no empty slots traversed previously but the xEle > yEle, swap the two elements
			else:
				x[emptyCells[0]] = y[yInd]
				yInd += 1
		else:
			x[emptyCells[0]] = xEle
			emptyCells.append(xInd)

		emptyCells = emptyCells[1:]

for yInd in range(yInd, len(y)):
	x[emptyCells[0]] = y[yInd]
	emptyCells = emptyCells[1:]


print(x)