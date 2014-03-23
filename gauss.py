#!/usr/bin/env python
from fractions import Fraction
import sys

matrix = []
trys = 0
spaceNums = 5

def fillMatrix(fName):
	cMatrix = []
	for line in file(fName, "r").readlines():
		cMatrix.append(line.split())
	r = 0
	for row in cMatrix:
		matrix.append([])
		for char in row:
			if "/" in char:
				n, d = char.split("/")
				cur = Fraction(int(n), int(d))
			else:
				cur = Fraction(int(char), 1)
			matrix[r].append(cur)
		r += 1
			
def gauss():
	begRow = 0
	for col in range(len(matrix[0])-1):
		for row in xrange(begRow+1, len(matrix)):
			gaussRow(begRow, row)
		begRow += 1
		
			

def gaussRow(rowsrc, rowdst):
	global trys
	global spaceNums
	col = rowsrc
	if not matrix[rowsrc][col] and trys < len(matrix) - 1: # starting recursive function call, in case rows are lineary dependent
		putRowOnEnd(rowsrc)
		trys += 1
		gaussRow(rowsrc, rowdst)

	trys = 0
	try:
		fac = -1 * matrix[rowdst][col] / matrix[rowsrc][col]
		for i in xrange(0, len(matrix[0])):
			matrix[rowdst][i] = matrix[rowdst][i] + matrix[rowsrc][i] * fac
			sLen = len(str(matrix[rowdst][i].numerator) + str(matrix[rowdst][i].denominator)) + 2
			if sLen > spaceNums:
				spaceNums = sLen
	except ZeroDivisionError, e: # in case somebody has a 0 in its matrix
		pass

def putRowOnEnd(row):
	tmpRow = matrix[len(matrix)-1]
	matrix[len(matrix)-1] = matrix[row]
	matrix[row] = tmpRow

def main():
	if len(sys.argv) < 2:
		print "Usage: %s [ACSII-File]" % sys.argv[0]
		sys.exit(1)

	fillMatrix(sys.argv[1])
	gauss()
	mString = None

	print "upper triangular matrix:"
	for row in matrix:
		for num in row:
			if num.denominator == 1:
				mString = str(num.numerator)
			else:
				mString = str(num.numerator) + "/" + str(num.denominator)
			print ("%-" + str(spaceNums) + "s") % mString,
		print


if __name__ == '__main__':
	main()