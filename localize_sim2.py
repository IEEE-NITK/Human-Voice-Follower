# HVF IEEE 2019-20 localization algorithm simulation
import argparse
import math
parser = argparse.ArgumentParser()

parser.add_argument('-x',required=True ,type=float)
parser.add_argument('-y',required=True ,type=float)
#parser.add_argument('-z',required=True ,type=float)
parser.add_argument('-d',required=True ,type=float)
parser.add_argument('-s',required=True ,type=int)

args=parser.parse_args()

x=args.x
y=args.y
#z=args.z
d=args.d # half the distance between a pair of mics
s=args.s
#print(x,y,z)

ax=0
ay=d/2

bx=0
by=-d/2

cx=-d/2
cy=0

dx=d/2
dy=0

# delays for each pair of mics
del2=abs((math.sqrt((x-ax)**2 + (y-ay)**2 )-math.sqrt((x-bx)**2 + (y-by)**2 ))/340)
print(del2*340)
del1=abs((math.sqrt((x-cx)**2 + (y-cy)**2 )-math.sqrt((x-dx)**2 + (y-dy)**2 ))/340)
print(del1*340)


#'''
dl1=round(del1*s)*340/s
dl2=round(del2*s)*340/s
print(dl1," ",dl2)


'''
print(math.degrees(math.acos((dl1*340/s)/a)))
print(math.degrees(math.acos((dl2*340/s)/a)))
m1=math.tan(math.radians(120)-math.acos((dl1*340/s)/a))
m2=math.tan(math.radians(60)+math.acos((dl2*340/s)/a))
print(math.degrees(math.atan(m1)))
print(math.degrees(math.atan(m2)))
'''
a1=1/(dl1/2)**2
a2=1/(dl2/2)**2
b1=1/((d**2/4)-a1**2)
b2=1/((d**2/4)-a2**2)

import numpy as np

# Solving following system of linear equation
# 1a + 1b = 35
# 2a + 4b = 94

a = np.array([[a1, b1],[a2,b2]])
b = np.array([1, 1])

x,y=np.linalg.solve(a,b)
print(math.sqrt(abs(x)))
print(math.sqrt(abs(y)))
