#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import unittest

class X(object):
   def f(self):
      pass

class T(unittest.TestCase):
   def setUp(self):
      self.x = X()

   def test_f(self):
      self.assertEqual(None, self.x.f())

if __name__ == '__main__':
   r = unittest.TextTestRunner()
   # unittest.main()
   r.run(T())
