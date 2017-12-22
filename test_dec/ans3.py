class Polynomial:
 def __init__(self,a,coefficient=0,exponent=0):
  k=[]
  z=[]
  A=[]
  b=[]
  B=[]
  m=[]
  f=a.readlines()
  for t in f:
   k.append(t.strip().split('\n'))
  for i in k:
    r = filter(None,i)
    for w in r:
     l = str(filter(list,w))
     z.append(l)
  for v in z:
   v.split()
   (a,b) = v.split()
   a = int(filter(str.isdigit,str(a)))
   b=int(b)
   A.append(a)
   B.append(b)
  coefficient = A
  exponent = B
  self.coefficient = coefficient
  self.exponent = exponent
  

def __str__(self):
 return self.coefficient
 
p1=Polynomial("q2.txt")
print p1.coefficient()
