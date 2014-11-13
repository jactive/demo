class X:
   ca = "class variable"
   def i(self):
      print "%s in instance method" % X.ca

   @classmethod
   def c(cls):
      print "%s in class method" % cls.ca

   @staticmethod
   def s():
      print "%s in static method" % X.ca

if __name__ == "__main__":
   X().i()
   X.c()
   X.s()
