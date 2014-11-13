class A:
   def __init__(self):
      print "A init"
   def _p(self):
      print self, "in A"

class B(A):
   # the default __init__ will call the
   # supper class's __init__, i.e. A.__init__
   pass

class C(B):
   def __init__(self):
      print "C init"
      B.__init__(self);

   def _h(self):
      pass

   def g(self):
      print self, "in C"
      B._p(self)
      _h()

if __name__ == '__main__':
   c = C()
   c.g()
