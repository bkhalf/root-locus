# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import math

zeros=[]
real=[0,-25,-50,-50]
imag=[0,0,10,-10]
real=np.array(real)
zeros=np.array(zeros)
number_poles=len(real)
number_zeros=len(zeros)

size=number_poles-number_zeros
centre=0
for n1 in range(0,4):
    centre+=real[n1]
centre=centre/size


a = math.pi / size

fig = plt.figure()


p = fig.add_subplot(111)


x = np.linspace(-25, 25, 1000)


p.plot(x+centre, x*math.tan(a), label='linear',color='black')
p.plot(x+centre, x*math.tan(-a), label='second',color='black')
for n1 in range(0,number_poles):
    p.scatter(real[n1],imag[n1],marker='x',color='red')
x = np.linspace(0, -25, 1000)
p.plot(x,x-x, label='third',color='blue')

plt.legend()

plt.show()


