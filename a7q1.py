import math


from differential import euler
from differential import predictor
func = lambda y,x: y*(math.log(y))/x

out = euler(func,2.71828,2,20,0.02,'data1.txt') 


print(f'solution for 1st equation = {out}')
 
from differential import euler
from differential import predictor
func2 = lambda y,x: 6-2*y/x
out2 = euler(func2,1,3,20,0.02,'data2.txt')

print(f'solution for 2nd equation= {out2}')

'''
OUTPUT
solution for 1st equation = 3.3165277515741716
solution for 2nd equation= 2.9165116934347703

'''

