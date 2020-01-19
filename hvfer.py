# HVF IEEE 2019-20 localization algorithm simulation
import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('-x',required=True ,type=float)
parser.add_argument('-y',required=True ,type=float)
parser.add_argument('-z',required=True ,type=float)
parser.add_argument('-a',required=True ,type=float)
parser.add_argument('-s',required=True ,type=int)

args=parser.parse_args()

x=args.x
y=args.y
z=args.z
a=args.a # half the distance between a pair of mics
s=args.s
#print(x,y,z)

# delays for each pair of mics
del1=(math.sqrt((x+a)**2 + (y-a)**2 + z**2)-math.sqrt((x-a)**2 + (y-a)**2 + z**2))/340 
del2=(math.sqrt((x-a)**2 + (y-a)**2 + z**2)-math.sqrt((x-a)**2 + (y+a)**2 + z**2))/340
del3=(math.sqrt((x-a)**2 + (y+a)**2 + z**2)-math.sqrt((x+a)**2 + (y+a)**2 + z**2))/340
del4=(math.sqrt((x+a)**2 + (y+a)**2 + z**2)-math.sqrt((x+a)**2 + (y-a)**2 + z**2))/340

#'''
dl1=round(del1*s)
dl2=round(del2*s)
dl3=round(del3*s)
dl4=round(del4*s)
'''
dl1=(del1*s)
dl2=(del2*s)
dl3=(del3*s)
dl4=(del4*s)
'''
# delays in terms of sample time 


#computng tanthetas
t1=math.tan(math.acos((dl1*340/s)/(2*a)))
t2=math.tan(math.acos((dl2*340/s)/(2*a)))
t3=math.tan(math.acos((dl3*340/s)/(2*a)))
t4=math.tan(math.acos((dl4*340/s)/(2*a)))


# finally computing X and Y 
X=(4*a)/((((t3**2 -t1**2)**2)*(t4**2 - t2**2))**(1./3.))
Y=(4*a)/((((t4**2 -t2**2)**2)*(t3**2 - t1**2))**(1./3.))

print(X,"\n")
print(Y)