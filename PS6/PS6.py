#Problem Set 6
#Numerical Computation CSCI 3656
#Linear Interpolation
#Worked with Matthew Albrecht

import sys
import math

def interpolate(x0,y0,x1,y1,x):
    inter = (((x1 - x) * y0) + ((x - x0) * y1))/(x1 - x0)
    print inter

def lagrange(x1,y1,x2,y2,x3,y3,x):
    lag = (y1*((x - x2)*(x - x3))/((x1 - x2)*(x1 - x3))) + (y2*((x - x1)*(x - x3))/((x2 - x1)*(x2 - x3))) + (y3*((x - x1)*(x - x2))/((x3 - x1)*(x3 - x2)))
    print lag

def main(argv):
    #interpolate(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]))
    lagrange(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))

if __name__ == "__main__":
    main(sys.argv[1:])
