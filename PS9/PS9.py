#Problem Set 9
#Numerical Computation CSCI 3656
#3D Interpolation
#Johnlee Alvarez and Matthew Albrecht

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import scipy
import numpy as np
import sys
import math

def Lag(X,Y,x):
    p1=Y[0]*(((x-X[1])*(x-X[2])*(x-X[3])) / ((X[0]-X[1])*(X[0]-X[2])*(X[0]-X[3])))
    p2=Y[1]*(((x-X[0])*(x-X[2])*(x-X[3])) / ((X[1]-X[0])*(X[1]-X[2])*(X[1]-X[3])))
    p3=Y[2]*(((x-X[0])*(x-X[1])*(x-X[3])) / ((X[2]-X[0])*(X[2]-X[1])*(X[2]-X[3])))
    p4=Y[3]*(((x-X[0])*(x-X[1])*(x-X[2])) / ((X[3]-X[0])*(X[3]-X[1])*(X[3]-X[2])))
    lag = p1+p2+p3+p4
    return lag

def main(argv):
    c = sys.argv[1] #unused
    x = [33.44, 8.81, 15.62, 40.16, 61.45, 58.81, 36.97, 64.71, 89.11, 67.24, 65.90, 76.55]
    y = [87.93, 84.07, 34.83, 38.71, 67.07, 91.44, 63.29, 42.38, 46.49, 18.32, 31.93, 44.51]
    z = [105.88, 103.11, 105.98, 108.13, 108.12, 107.72, 107.14, 109.07, 109.93, 109.99, 109.51, 109.91]

    ax=[]
    ay=[]
    bx=[]
    by=[]
    cx=[]
    cy=[]
    dx=[]
    dy=[]
    az=[110,110,110,110]
    bz=[107,107,107,107]
    cz=[105,105,105,105]
    dz=[103,103,103,103]

    ################################################################
    temp = Lag([z[11],z[10],z[9],z[8]], [x[11],x[10],x[9],x[8]],110)
    ax.append(temp)
    temp = Lag([z[7],z[10],z[9],z[8]], [x[7],x[10],x[9],x[8]],110)
    ax.append(temp)
    temp = Lag([z[7],z[4],z[9],z[8]], [x[7],x[4],x[9],x[8]],110)
    ax.append(temp)
    temp = Lag([z[7],z[4],z[3],z[8]], [x[7],x[4],x[3],x[8]],110)
    ax.append(temp)


    temp = Lag([z[11],z[10],z[9],z[8]], [y[11],y[10],y[9],y[8]],110)
    ay.append(temp)
    temp = Lag([z[7],z[10],z[9],z[8]], [y[7],y[10],y[9],y[8]],110)
    ay.append(temp)
    temp = Lag([z[7],z[4],z[9],z[8]], [y[7],y[4],y[9],y[8]],110)
    ay.append(temp)
    temp = Lag([z[7],z[4],z[3],z[8]], [y[7],y[4],y[3],y[8]],110)
    ay.append(temp)


    ################################################################
    temp = Lag([z[6],z[5],z[4],z[3]], [x[6],x[5],x[4],x[3]],107)
    bx.append(temp)
    temp = Lag([z[5],z[4],z[3],z[2]], [x[5],x[4],x[3],x[2]],107)
    bx.append(temp)
    temp = Lag([z[4],z[3],z[2],z[7]], [x[4],x[3],x[2],x[7]],107)
    bx.append(temp)
    temp = Lag([z[3],z[2],z[7],z[0]], [x[3],x[2],x[7],x[0]],107)
    bx.append(temp)


    temp = Lag([z[6],z[5],z[4],z[3]], [y[6],y[5],y[4],y[3]],107)
    by.append(temp)
    temp = Lag([z[5],z[4],z[3],z[2]], [y[5],y[4],y[3],y[2]],107)
    by.append(temp)
    temp = Lag([z[4],z[3],z[2],z[7]], [y[4],y[3],y[2],y[7]],107)
    by.append(temp)
    temp = Lag([z[3],z[2],z[7],z[0]], [y[3],y[2],y[7],y[0]],107)
    by.append(temp)


    ################################################################
    temp = Lag([z[0],z[2],z[1],z[6]], [x[0],x[2],x[1],x[6]],105)
    cx.append(temp)
    temp = Lag([z[5],z[2],z[1],z[6]], [x[5],x[2],x[1],x[6]],105)
    cx.append(temp)
    temp = Lag([z[5],z[3],z[1],z[6]], [x[5],x[3],x[1],x[6]],105)
    cx.append(temp)
    temp = Lag([z[5],z[3],z[4],z[6]], [x[5],x[3],x[4],x[6]],105)
    cx.append(temp)


    temp = Lag([z[0],z[2],z[1],z[6]], [y[0],y[2],y[1],y[6]],105)
    cy.append(temp)
    temp = Lag([z[5],z[2],z[1],z[6]], [y[5],y[2],y[1],y[6]],105)
    cy.append(temp)
    temp = Lag([z[5],z[3],z[1],z[6]], [y[5],y[3],y[1],y[6]],105)
    cy.append(temp)
    temp = Lag([z[5],z[3],z[4],z[6]], [y[5],y[3],y[4],y[6]],105)
    cy.append(temp)


    ################################################################
    temp = Lag([z[0],z[2],z[1],z[6]], [x[0],x[2],x[1],x[6]],103)
    dx.append(temp)
    temp = Lag([z[5],z[2],z[1],z[6]], [x[5],x[2],x[1],x[6]],103)
    dx.append(temp)
    temp = Lag([z[5],z[3],z[1],z[6]], [x[5],x[3],x[1],x[6]],103)
    dx.append(temp)
    temp = Lag([z[5],z[3],z[4],z[6]], [x[5],x[3],x[4],x[6]],103)
    dx.append(temp)


    temp = Lag([z[0],z[2],z[1],z[6]], [y[0],y[2],y[1],y[6]],103)
    dy.append(temp)
    temp = Lag([z[5],z[2],z[1],z[6]], [y[5],y[2],y[1],y[6]],103)
    dy.append(temp)
    temp = Lag([z[5],z[3],z[1],z[6]], [y[5],y[3],y[1],y[6]],103)
    dy.append(temp)
    temp = Lag([z[5],z[3],z[4],z[6]], [y[5],y[3],y[4],y[6]],103)
    dy.append(temp)


    ################################################################
    xplane = np.linspace(103,110,10)
    zplane = np.linspace(8.81,76.55,10)

    aprime = []
    bprime = []
    cprime = []
    dprime = []

    xfinal = []
    yfinal = []
    zfinal = []

    for i in range (0,9):
        aprime.append(Lag(ax,ay, zplane[i]))
        bprime.append(Lag(bx,by, zplane[i]))
        cprime.append(Lag(cx,cy, zplane[i]))
        dprime.append(Lag(dx,dy, zplane[i]))
        for t in range (0,9):
            xfinal.append(zplane[i])


    for j in range (0,9):
        for s in range (0,9):
            yfinal.append(Lag([aprime[j],bprime[j],cprime[j],dprime[j]],[110,107,105,103],xplane[s]))
            zfinal.append(xplane[s])
    print zfinal
    fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    ax = fig.gca(projection='3d')

    ax.plot_trisurf(xfinal, yfinal, zfinal, color=(.2,.1,.5,.9))


    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
