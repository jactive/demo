def info(obj, spacing=17, collapse=True):
   # an for attribute name
   methodNames = [an for an in dir(obj) if callable(getattr(obj, an))]
   format_doc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
   # mn for method name
   return "\n".join(["%s %s" % (mn.ljust(spacing), format_doc(str(getattr(obj, mn).__doc__))) for mn in methodNames])

if __name__ == '__main__':
   print info(__builtins__)
