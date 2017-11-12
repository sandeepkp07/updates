import sys
class Base:
 def fun(self):
  print 'hallo base'
class derived(Base):
 def fun2(self):
  print 'halo derived'
a=derived()
a.fun()
a.fun2()
