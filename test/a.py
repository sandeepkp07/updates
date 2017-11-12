import math
import sys
def my_sine(x):
 s = 0
 k=85
 for i in range(k):
  u = math.factorial(2*i+1)
  g = x**(2*i+1) 
  if i % 2 == 0:
   s +=g/u
  else:
   s-=g/u
 return s
a=my_sine(1.2)
print a
