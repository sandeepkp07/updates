import sys
def anagram(x):
 d = {}
 for line in x:
  r = line.strip().lower()
  t = list(r)
  t.sort()
  t = ''.join(t)
  if t not in d:
   d[t] = [r]
  else:
   d[t].append(r)
 t=[]
 for v in d.values():
  if len(v) > 1:
   t.append((len(v), v))
   t.sort()
 for x in t:
  print x
a=open('anagram.txt')
print anagram(a)
