import random
def random_word(x):
 t=[]
 for g in x:
  t.append((len(g),random.random(),g))
 t.sort(reverse=True)
 res = []
 for length, _,g in t:
  res.append(g)
 return res
n=int(input("enter num of elements\t:"))
a=[0 for i in range(n)]
for i in range(n):
 a[i]=raw_input("enter elements")
print random_word(a)
