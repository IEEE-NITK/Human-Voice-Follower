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
dl1=round(del1*s) # in actual program , delay will be obtained by cross correlation
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

if(dl1>=0 and dl2<=0): 	#1st quadrant
	d1=dl1
	d2=dl2
	d3=dl3
	d4=dl4
	q=1
	xsign=1
	ysign=1
if(dl1>=0 and dl2>=0):  #4th quadrant
	d1=dl2
	d2=dl3
	d3=dl4
	d4=dl1
	q=4
	xsign=1
	ysign=-1
if(dl1<=0 and dl2>=0): 	#3rd quadrant
	d1=dl3
	d2=dl4
	d3=dl1
	d4=dl2
	q=3
	xsign=-1
	ysign=-1
if(dl1<=0 and dl2<=0): 	#2nd quadrant
	d1=dl4
	d2=dl1
	d3=dl2
	d4=dl3
	q=2
	xsign=-1
	ysign=1





#computng tanthetas
t1=math.tan(math.acos((d1*340/s)/(2*a)))
t2=math.tan(math.acos((d2*340/s)/(2*a)))
t3=math.tan(math.acos((d3*340/s)/(2*a)))
t4=math.tan(math.acos((d4*340/s)/(2*a)))


# finally computing X and Y 
X=(4*a)/((((t3**2 -t1**2)**2)*(t4**2 - t2**2))**(1./3.))*xsign
Y=(4*a)/((((t4**2 -t2**2)**2)*(t3**2 - t1**2))**(1./3.))*ysign

if(q==2 or q==4):
	X=-1*X
	Y=-1*Y
	t=X
	X=Y
	Y=t


print(X,"\n")
print(Y)
