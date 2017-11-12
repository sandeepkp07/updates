import sys
class Complex:
 def __init__(self,real,image):
  self.real=real
  self.image=image
 
 def __str__(self):
  return str(self.real)+ '+i' + str(self.image)

 def add(self,other):
  real=self.real+other.real
  image = self.image+other.image
  c=Complex(real,image)
  return c



 def multiply(self,other):
  real=self.real*other.real
  image=self.image*other.image
  d=Complex(real,image)
  return d




a=Complex(1,2)
b=Complex(3,4)
c=a.add(b)
d=a.multiply(b)
print c
print d
