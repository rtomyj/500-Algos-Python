#!/usr/bin/python3

numbers = [8, 7, 2, 5, 3, 1]
numbers.sort()
halfList = int(len(numbers) / 2)
size = len(numbers)
sumsUsed = []

def sumFound(a, indexA, b, indexB):
	if not [a,b] in sumsUsed:
		print('Sum found using numbers {0} found at position {2} and {1} found in position {3}'.format(a, b, indexA, indexB))
		sumsUsed.append([a,b])
		sumsUsed.append([b,a])


def firstHalf(posA, numA, sum):
	for posB, numB in enumerate(numbers[0:halfList]):
		other = sum - numA
		if numB == other and posA != posB:
			sumFound(numA, posA, numB, posB)

def secondHalf(posA, numA, sum):
	for posB, numB in enumerate(numbers[halfList:size]):
		other = sum - numA
		posB = halfList + posB
		if numB == other and posA != posB:
			sumFound(numA, posA, numB, posB)


sum = 10

for posA, numA in enumerate(numbers):
	other = sum - numA
	if numbers[halfList] == other and posA != halfList:
		sumFound(numA, posA, numbers[halfList], halfList)
	elif numbers[halfList] > other:
		firstHalf(posA, numA, sum)
	else:
		secondHalf(posA, numA, sum)
