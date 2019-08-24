def getIndexOfZeroForMaxOnes(items):
	maxOnesFound = maxZeroSubstitutePos = indexOfLastZero = -1
	itemsSize = len(items)
	sequenceStart = -2

	for (ind, item) in enumerate(items):
		if item == 0:
			if ind != itemsSize -1 and items[ind + 1] == 1:
				sequenceStart = indexOfLastZero
			elif sequenceStart != -2:
				numOnesInBetween = ind - (sequenceStart + 1)

				if numOnesInBetween > maxOnesFound:
					maxOnesFound = numOnesInBetween
					maxZeroSubstitutePos = indexOfLastZero

				sequenceStart = -2
			else:
				numOnesInBetween = ind - (indexOfLastZero + 1)
				if numOnesInBetween > maxOnesFound:
					maxOnesFound = numOnesInBetween
					maxZeroSubstitutePos = ind

			indexOfLastZero = ind

	if sequenceStart != -2:
		numOnesInBetween = itemsSize - (sequenceStart + 1)
	else:
		numOnesInBetween = itemsSize - (indexOfLastZero)
	if numOnesInBetween > maxOnesFound:
		maxZeroSubstitutePos = indexOfLastZero


	return maxZeroSubstitutePos

items = [0]#11 = size
print( "Index of 0 to replace: {0}".format(getIndexOfZeroForMaxOnes(items)) )
