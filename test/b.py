import sys
class Complex:
 ""
def add_mul(a,b):
 c=add(a,b)
 d=multiply(a,b)
 print (c.real,c.imag)
 return d.real,d.imag

def add(self,other):
 c=complex(self.real+other.real,self.imag+other.imag)
 return c

def multiply(self,other):
 d=complex(self.real*other.real,self.imag*other.imag)
 return d


a=complex(1,2)
b=complex(3,4)
print add_mul(a,b)
