class P:
   def __init__(self):
      print "In P __init__"

class C(P):
   def __init__(self):
      P.__init__(self)
      print "In C __init__"
      # You can call it any times as you wish
      P.__init__(self)

class D(P):
  pass
C()
print
D()
