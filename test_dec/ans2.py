m=[]
k=[]
z=[]
G={}
f=open("q2.txt").readlines()
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
   total=G.get(b,0) + a
   G[b]=total
for h in reversed(sorted(G.items())):
   d = "%sx^%s" % (h[1],h[0])
   m.append(d)
print '+'.join(m)

