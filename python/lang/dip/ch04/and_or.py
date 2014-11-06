def make(t, v):
   def x():
      print "%s=%s; " % (str(t), str(v)),
      return v
   return x

def pit(expr):
   print expr
   print "\n%s\n" % eval(expr)

pit("""make('p1', [])() and make ('p2', 1)() or make('p3', 3)() and make('p4', 4)() and make('p5', None)()""")
pit("""make('p1', [])() and make ('p2', 1)() or make('p3', 3)() or make('p4', 4)() and make('p5', None)()""")
pit("""make('p1', [])() and make ('p2', 1)() or make('p3', 3)() and make('p4', None)() or make('p5', 1)()""")
