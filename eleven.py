x = [0, 2, 0, 3, 0, 5, 6, 0, 0]
y = [1, 8, 9, 10, 15]

emptyCells = []
xInd = 0
yInd = 0

while yInd < len(y):
	if xInd == len(x):
		x[emptyCells[0]] = y[yInd]
		emptyCells = emptyCells[1:]
		yInd += 1
		continue

	xEle = x[xInd]
	yEle = y[yInd]

	if xEle == 0:
		emptyCells.append(xInd)
		xInd += 1
	else:
		if xEle > yEle:
			if len(emptyCells) > 0:
				x[emptyCells[0]] = yEle
				emptyCells = emptyCells[1:]
				yInd += 1
			else:
				x[xInd] = yEle
				y[yInd] = xEle
				xInd += 1
		else:
			if len(emptyCells) > 0:
				x[emptyCells[0]] = xEle
				x[xInd] = 0
				emptyCells = emptyCells[1:]
				emptyCells.append(xInd)
			xInd += 1


print(x)