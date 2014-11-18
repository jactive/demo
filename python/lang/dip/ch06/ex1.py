import sys

f = None
try:
   f = open('/nonexistent')
except IOError:
   print "Hit except 1"


extype = lambda: IOError
try:
   f = open('/nonexistent')
except extype():
   print "Hit except 2"

try:
   f = open('/nonexistent')
except (IOError):
   print "Hit except 3"

extypes  = lambda: (IOError, NameError, AttributeError)

try:
   f = open('/nonexistent')
except extypes(), e:
   print "Hit except 4"

try:
   x = 1
except NameError as e:
   print "Never hit this except"
else:
   print "Hit else 1"
finally:
   print "finally always got run"

try:
   x = zz
except NameError as e:
   print "Hit except 5: %s" % e
else:
   print "Never this else"
finally:
   print "finally always got run"

print "Exit. See `pydoc try`"
