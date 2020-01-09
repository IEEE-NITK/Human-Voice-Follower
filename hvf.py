import sympy
from sympy import symbols, solve, Eq
import math
from math import*

# theta values
t1 = float(input("Give theta1 value"))
t2 = float(input("Give theta2 value"))
t3 = float(input("Give theta3 value"))
t4 = float(input("Give theta4 value"))
c1 = tan(t1)
c2 = tan(t2)
c3 = tan(t3)
c4 = tan(t4)
k1 = c1**2 - c3**2
k2 = c2**2 - c4**2
# value of a
a = 0.7


x, y, z = symbols('x y z', real = True)


#trigonometric equations

'''e1= Eq((x**2)*(c1**2) - (y + a)**2 - z**2,0)
e2= Eq((x**2)*(c3**2) - (y - a)**2 - z**2,0)
e3= Eq((y**2)*(c2**2) - (x + a)**2 - z**2,0)
e4= Eq((y**2)*(c4**2) - (x - a)**2 - z**2, 0)
ans = solve((e1,e2,e3,e4),(x,y,z))'''

e1 = Eq(k1*(x**2) -  4*a*y, 0)
e2 = Eq(k2*(y**2) - 4*a*x, 0)
ans = solve((e1,e2),(x,y))
(x1,y1) = (0,0)
for (x,y) in ans:
    if(x,y) != 0:
        (x1,y1) = (x,y)
z = sympy.sqrt((c1**2)*(x1**2) - (y1 + a)**2)
print(ans,z)
print(c1)

