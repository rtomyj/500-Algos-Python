def swap_elements(x, aInd, bInd, y=None):
	if y == None:
		temp = x[aInd]
		x[aInd] = x[bInd]
		x[bInd] = temp
	else:
		temp = x[aInd]
		x[aInd] = y[bInd]
		y[bInd] = temp
