import math
from differential import shooting_method

func1 = lambda x,y,z:z
func2  = lambda x,y,z:z+1

out=shooting_method(func1,func2,0,1,1.3,0.8,1,2*(math.exp(1)-1),0.02)
print(out)