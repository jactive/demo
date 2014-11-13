class X:
   def __setitem__(self, k, v):
      print '%s.__setitem__ is invoked, k="%s", v="%s"' % (self, k, v)

   def __getitem__(self, k):
      print '%s.__getitem__ is invoked, k="%s"' % (self, k)
      return "__getitem__ always return this string"

   def __delitem__(self, k):
      print '%s.__delitem__ is invoked, k="%s"' % (self, k)
      # The return value is not visible in caller
      return "__delitem__ always return this string"

   def __len__(self):
      print '%s.__len__ is invoked. int must be returned' % self
      #! TypeError: __len__() should return an int
      #! return '__len__ always return 13'
      return 13

   def __str__(self):
      ret = object.__str__(self)
      print '# __str__ is invoked. %s will be returned' % ret
      return ret

   def __repr__(self):
      ret = object.__repr__(self)
      print '# __repr__ is invoked. %s will be returned' % ret
      return ret

   def __cmp__(self, other):
      print '%s.__cmp__ is invoked.' % self
      return 1

if '__main__' == __name__:
   x = X()
   x['my key'] = 'my val'
   print x['my key']
   print len(x)
   print x
   x2 = X()
   b = x == x2
   print b
   del x['my key1']
