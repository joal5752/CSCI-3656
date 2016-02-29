#Problem Set 4
#Numerical Computation CSCI 3656
#Gaussian Elimination
#Johnlee Alvarez and Matthew Albrecht

import sys
import math
import numpy
from numpy import linalg as LA

def backSub(A):
	buff = 0
	counter = 1
	x = 2
	while x >= 0:
		buff = 3 - x
		y = 2
		while y > counter:
			if buff > 1:
				A[x,3] -= A[x,y] * A[y,3]
				buff -= 1
				y -= 1
			elif A[x,y] != 0:
				A[x,3] = A[x,3]/A[x,y]
				y -= 1
			else:
				print 'There is no solution'
				return 0
		counter -= 1
		x -= 1
	X = numpy.matrix([[A[0,3]], [A[1,3]], [A[2,3]]])
	print 'solution vector is: '
	print X
	return A

def forwardElim(A):
	x = 1
	y = 0
	#liz = A[x-counter,y]
	while y < 2:
		x = 1 + y
		counter = 1
		while x < 3:

			y_temp = y
			coeff = (A[x,y]/A[x-counter,y])

			while y < 4:
				A[x,y] = A[x,y] - (coeff * A[x-counter,y])
				y += 1
			y = y_temp
			print A
			print '\n'

			counter += 1
			x += 1

		y += 1
	return A



def main(argv):
    A = numpy.matrix([[float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])], [float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8])], [float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12])]])
    B = numpy.matrix([[float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])], [float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])], [float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11])]])
    #print A
    #print 'top left number is: '+ str(A[0,0])
    #backSub(forwardElim(A))
    print LA.cond(B, numpy.inf)
    #print forwardElim(A)


if __name__ == "__main__":
    main(sys.argv[1:])
