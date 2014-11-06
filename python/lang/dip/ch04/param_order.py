def f(a, b='b default', c='c default'):
   print "a=%s, b=%s, c=%s" % (str(a), str(b), str(c))

if __name__ == "__main__":
   f("a1 param")
   f("a2 param", "c param")
   f(b="b param", a="a3 param")

