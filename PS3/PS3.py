#Problem Set 3
#Numerical Computation CSCI 3656
#Bisection, Secant, and Newton root finder methods

#adapted from http://thelivingpearl.com/code-for-bisection-method-in-python/

#1 iterations : 3
#2 iterations : 7

import sys
import math

def f(x):
    return (x-2)**3
 
def fprime(x):
    return 3*x**2 - 6*x

def newton(a, tol):
    if a == 0:
        return a
    b = a - (f(a)/fprime(a))
    counter = 1
    while math.fabs(f(b)) > tol:
        a = b
        counter += 1
        b = a - (f(a)/fprime(a))
    print 'The number of iterations is: ' + str(counter)
    print 'The root is: ',    
    return b

def secant(a,b,tol):
    c = a - f(a)*((b-a)/(f(b)-f(a)))
    counter = 1
    while math.fabs(f(c)) > tol:
        if f(c) == 0:
            return c
        b = a
        a = c
        counter += 1
        c = a - f(a)*((b-a)/(f(b)-f(a)))
    print 'The number of iterations is: ' + str(counter)
    print 'The root is: ',    
    return c

def bisection(a,b,tol):
    if (f(a)*f(b)) > 0:
        sys.exit('ERROR BITCH') 
    c = (a+b)/2.0
    counter = 1
    #root = -0.252624
    while math.fabs((b-a)/2.0) > tol:
        #error = math.fabs(c - root)
        #print error
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            counter += 1
            b = c
        else :
            counter += 1
            a = c
        c = (a+b)/2.0
    print 'The number of iterations is: ' + str(counter)
    print 'The root is: ',    
    return c
    
def main(argv):
    if sys.argv[3] == 'newton':
        print newton(float(sys.argv[1]),float(sys.argv[2]))
    elif sys.argv[4] == 'bisection':
        print bisection(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
    elif sys.argv[4] == 'secant':    
        print secant(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]))
      

if __name__ == "__main__":
    main(sys.argv[1:])