import math

from differential import RK4

f1 = lambda x,y,z : -z-x
f2 = lambda x,y,z : -z+1-x

out = RK4(f1,f2,0,2,1,5,0.02)

print(f'y = {out}')

'''
OUTPUT

y = -7.0464402584840515

'''