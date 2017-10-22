import os
def walk(updates):
 for root,f,name in os.walk(updates):
  for fn in f:
   print os.path.join(name,root,fn)
  else:
   return 1
def walk1(updates):
 for name in os.listdir(updates):
  path = os.path.join(updates, name)
  if os.path.isfile(path):
   print path
  else:
   walk(path)
walk('/home/sandeep/updates')
walk1('/home/sandeep/updates')

