class Polynomial:
 def __init__(self,f):
  f = open(f).readlines()
  self.f=f

 def __str__(self):
  G={}
  u=[]
  for (a,b) in zip(self.coefficient,self.exponent):
   b=str(b)
   total=G.get(b,0) + a
   G[b]=total
  for h in reversed(sorted(G.items())):
    d = "%sx^%s" % (h[1],h[0])
    u.append(d)
  print '+'.join(u)  
 def coefficient(self):
  k=[]
  z=[]
  A=[]
  b=[]
  B=[]
  m=[]
  a = self.f
  for t in a:
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
   self.coefficient = A
  return self.coefficient


 def exponent(self):
  k=[]
  z=[]
  A=[]
  b=[]
  B=[]
  m=[]
  a = self.f
  for t in a:
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
   self.exponent = B
  return self.exponent



p1=Polynomial("q2.txt")  
print p1.coefficient()
print p1.exponent() 
print p1                 
