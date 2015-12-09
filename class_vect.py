# -*- coding: cp1251 -*-
from math import hypot


class Vector(object):
   def __init__(self, a, b):
      self._a = a
      self._b = b

   def __repr__(self):
      return "Vector({},{})".format(self.a, self.b)
   
   def __add__(self,other):
      if not isinstance(other,Vector):
         return NotImplemented   # якщо б інший вектор був стрічкою або 2-а числа інтеджер 
      return Vector(self.a + other.a, self.b + other.b)

   def __eq__(self,other):
      if not isinstance(other,Vector):
         return NotImplemented   
      return self.a == self.b and self.a == self.b

   def __neg__(self):
      return Vector(-self.a, -self.b)

#   def __sub__(self,other):
#     return Vector(self.a - other.a, self.b - other.b)
    
   def __mul__(self,other):
       if not isinstance(other,(int, float)):
         return NotImplemented   
       return Vector(self.a * other, self.b * other)

   def __rmul__(self,other):
       return self * other 

   def __abs__(self):
       return hypot(self.a , self.b)
        #return (self.a **2, self.b ** 2)**0.5# корінь то треба **0.5
      

   @property
   def a(self):
      return self._a

   @property
   def b(self):
      return self._b
      
    
v1 = Vector(3,4)
v2 = Vector(8,-5)
v3 = Vector (0, 4)
s = v1 + v2
print s
s1 = s + v3
print s1
print v1 + -v1
print v1 * 5
print 5 * v1
print abs(v1) 
print v1.a, v1.b



