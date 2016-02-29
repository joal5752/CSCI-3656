#Problem Set 5
#Numerical Computation CSCI 3656
#Multivariate Newton
#Worked with Matthew Albrecht

import math
import sys
import numpy
from numpy import linalg as np


def F(x0):
	u = x0[0,0]
	v = x0[1,0]
	w = x0[2,0]
	return numpy.matrix([[2*u**2 - 4*u + v**2 + 3*w**2 + 6*w + 2], [u**2 + v**2 - 2*v + 2*w**2 - 5], [3*u**2 - 12*u + v**2 + 3*w**2 + 8]])

def DF(x0):
	u = x0[0,0]
	v = x0[1,0]
	w = x0[2,0]
	f11 = 4*u - 4
	f12 = 2*v
	f13 = 6*w + 6
	f21 = 2*u
	f22 = 2*v - 2
	f23 = 4*w
	f31 = 6*u - 12
	f32 = 2*v
	f33 = 6*w
	return numpy.matrix([[f11, f12, f13], [f21, f22, f23], [f31, f32, f33]])


def main(argv):
	x0 = numpy.matrix([[float(sys.argv[1])], [float(sys.argv[2])], [float(sys.argv[3])]])
	print str("step").rjust(5), str("|").rjust(2) , str("u").rjust(10) , str("|").rjust(2) , str("").rjust(2) , str("v").rjust(17) , str("|").rjust(5) , str("").rjust(5) , str("w").rjust(17)
	print str("--------------------------------------------------------------------------------")
	print repr(0).rjust(5) , str("|").rjust(2) ,  repr(x0[0,0]).rjust(17) , str("|").rjust(2) , str("").rjust(2) , repr(x0[1,0]).rjust(17) , str("|").rjust(2) , str("").rjust(2) , repr(x0[2,0]).rjust(17)
	x=0

	while x < 15:
		s = np.linalg.solve(DF(x0), (-1)*F(x0))
		x1 = s + x0

		x0=x1
		x+=1
		print repr(x).rjust(5) , str("|").rjust(2) ,  repr(x1[0,0]).rjust(17) , str("|").rjust(2) , str("").rjust(2) , repr(x1[1,0]).rjust(17) , str("|").rjust(2) , str("").rjust(2) , repr(x1[2,0]).rjust(17)
	print repr(x).rjust(5) , str("|").rjust(2) ,  repr(x1[0,0]).rjust(17) , str("|").rjust(2) , str("").rjust(2) , repr(x1[1,0]).rjust(17) , str("|").rjust(2) , str("").rjust(2) , repr(x1[2,0]).rjust(17)


    #B = numpy.matrix([[float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])], [float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])], [float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11])]])
    #print A
    #print 'top left number is: '+ str(A[0,0])
    #backSub(forwardElim(A))
    #print LA.cond(B, numpy.inf)
    #print forwardElim(A)


if __name__ == "__main__":
    main(sys.argv[1:])
