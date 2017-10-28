import os
def walk(updates):
 for name in os.listdir(updates):
  path = os.path.join(updates, name)
  if os.path.isfile(path):
   print path
  else:
   walk(path)
walk('/home/sandeep/updates')
<<<<<<< HEAD

=======
>>>>>>> 6cce2e8e81106a4ccbe850879e0955b88cbe07a5
