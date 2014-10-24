import numpy as np
from scipy.optimize import leastsq
import pylab as pl


import pprint
import csv as csv
csvfile = file('data.csv')
reader = csv.reader(csvfile)
for i in range(6):
   reader.next()

series = []
for line in reader:
   try:
      series.append(float(line[1]))
   except Exception, e:
      if line is not None and len(line[1]) > 0 :
         print "error: ", line
series = np.array(series)
coordinates = np.array(range(len(series)))



# Fitting a curve via lesss square http://en.wikipedia.org/wiki/Least_squares
# Find the F via series,
#import numpy as np
#from scipy.optimize import leastsq
#import pylab as pl
 
def fitting_curve(x, params):
   """
   Latency curve function
      F  :   a*x + b*x^2 + c*x^3   + d*sin(2*pi*e*x+f) +
             g*arctan(h*x + i)
      F' :   a   + 2*b*x + 3*c*x^2 + (2*pi*e)*d*cos(2*pi*e*x+f) +
             g*h/(1+(h*x+i)^2)
   By looing into lots of pmet graphes, it's deemed empirically that the
   above F could cover all the latency curve.
   """
   a, b, c, d, e, f, g, h, i = params
   return a*x + b*x*x + c*x*x*x + d*np.sin(2*np.pi*e*x + f) + g * np.arctan(h*x + i)
 
residual = lambda p, y, x: y - fitting_curve(x, p)

init_params = [0.1, 0.1, 0.1,
           0.001, 10, 0,
           0.5, 2, 1]
 
retobj = leastsq(residual, init_params, args=(series, coordinates))
real_params = retobj[0]
pprint.pprint(retobj)
print "The parameters of the fitting curve are: ", real_params 
 
pl.plot(coordinates, series, label="real")
pl.plot(coordinates, fitting_curve(coordinates, retobj[0]), label="my")
pl.legend()
pl.savefig('/home/local/ANT/haifengw/local/httpd/htdocs/images/fitting_curve.png')
# pl.show()


# Definite Integrals of the Fitting curve.
from scipy.integrate import quad
retobj = quad(fitting_curve, coordinates[0], coordinates[-1], args=(real_params)) 
pprint.pprint(retobj)
area = retobj[0]
print 'quad       area', area
print 'avg        area', np.mean(series) * (coordinates[-1] - coordinates[0])

more_coords = np.linspace(1, len(coordinates), len(coordinates)*100)
more_series = fitting_curve(more_coords, real_params)
print 'curve mean area', np.mean(more_series) * (coordinates[-1] - coordinates[0])

def derivative_of_fc(x, params):
   """
   The fitting curve derivative. See curve_fitting for F' definition
   """
   a, b, c, d, e, f, g, h, i = params
   # a*x + b*x*x + c*x*x*x + d*np.sin(2*np.pi*e*x + f) + g * np.arctan(h*x + i)
   return a + 2*b*x + 3*c*x*x + (2*np.pi*e)*d*np.cos(2*np.pi*e*x+f) + g*h/(1+(h*x+i)*(h*x+i))

derivatives = derivative_of_fc(coordinates, real_params)
print np.sum(derivatives), len(coordinates)/5

