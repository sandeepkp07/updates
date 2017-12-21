k=[]
z=[]
f=open("q1.txt").readlines()
for t in f:
 k.append(t.strip().split('\n'))
for i in k:
 r = filter(None,i)
 for w in r:
  l = list(filter(str.isdigit,str(w)))
  v = ''.join(l)
  z.append(v)
z=[int(x) for x in z]
z.sort()
print z
