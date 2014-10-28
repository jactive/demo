import matplotlib
matplotlib.use('Agg')

THREAHOLD_SLOPE=0.17632698070846498 # slope=10 degree. np.tan(np.pi*1/18)
RECENT_SERIES_SIZE = 7


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
 
def fit_latency_curve(x, params):
   """
   Fit the latency curve function F 
      F  :   a*x + b*x^2 + c*x^3 + d*arctan(e*x + f) + g
      F' :   a   + 2*b*x + 3*c*x^2 + d*e/(1+(e*x+f)^2)
      integral(F) : (a/2)*x^2 + (b/3)*x^3 + (c/4)*x^4 +
                    (1/e)*(u*arctan(u) - 0.5*ln(1+u^2)) + g*x
                    u = e*x + f
   By looing into lots of pmet graphes, it's deemed empirically that the
   above F could cover all the latency curve.
   https://improvement-ninjas.amazon.com/s3files/s3get.cgi/integral_arctan.png
   """
   a, b, c, d, e, f, g = params
   return a*x + b*x*x + c*x*x*x + d * np.arctan(e*x + f) + g
 
residual = lambda p, y, x: y - fit_latency_curve(x, p)

init_params = [0.1, 0.1, 0.1,
               0.5, 2, 1,
               0]
 
retobj = leastsq(residual, init_params, args=(series, coordinates))
real_params = retobj[0]
pprint.pprint(retobj)
print "The parameters of the fitting curve are: ", real_params 
latency_curve_func = lambda x: fit_latency_curve(x, real_params)
 
pl.plot(coordinates, series, label="real")
fined = np.linspace(coordinates[0], coordinates[-1], len(coordinates)*100)
pl.plot(coordinates, latency_curve_func(coordinates), label="my")
pl.legend()
pl.savefig('/home/local/ANT/haifengw/local/httpd/htdocs/images/fitting_curve.png')
# pl.show()


# Definite integrals of the latency curve.
from scipy.integrate import quad
# test purpose only. make the integral forumula manually if needed
retobj = quad(latency_curve_func, coordinates[0], coordinates[-1]) 
pprint.pprint(retobj)
area = retobj[0]
print 'quad       area', area
print 'avg        area', np.mean(series) * (coordinates[-1] - coordinates[0])

def integral_of_lc_with_params(x, params):
   """
   The latency curve integral. See fit_latency_curve for F's integral definition
   a*x + b*x^2 + c*x^3 + d*arctan(e*x + f) + g
   """
   a, b, c, d, e, f, g = params
   u = e*x + f
   return  (a/float(2))*x*x + (b/float(3))*x*x*x + (c/float(4))*x*x*x*x + \
           float(d)*(u*np.arctan(u) - 0.5*np.log(1+u*u))/e + g*x

integral_of_lc = lambda x: integral_of_lc_with_params(x, real_params)
print 'manual     area', integral_of_lc(coordinates[-1]) - integral_of_lc(coordinates[0])

more_coords=  np.linspace(coordinates[0], coordinates[-1], len(coordinates)*100)
more_coords = np.linspace(1, len(coordinates), len(coordinates)*100)
more_series = latency_curve_func(more_coords)
print 'curve mean area', np.mean(more_series) * (coordinates[-1] - coordinates[0])










def derivative_of_lc_with_params(x, params):
   """
   The latency curve function's derivative. See fit_latency_curve for F' definition
   """
   a, b, c, d, e, f, g = params
   return  a + 2*b*x + 3*c*x*x + d*e/(1+(e*x+f)*(e*x+f))

derivative_of_lc = lambda x: derivative_of_lc_with_params(x, real_params)

fg_coords =  np.linspace(coordinates[0], coordinates[-1], len(coordinates)*100) # fined grained
fg_series = derivative_of_lc(coordinates)
print 
print "tan10      sum, ", np.tan(np.pi/18) * len(coordinates)*100
print "derivative sum, ", np.sum(fg_series)
print "tan40      sum, ", np.tan(np.pi*8/18) * len(coordinates)*100





class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError("No such enum %s" % name)

Monotonicity = Enum(['INCREASING', 'DECREASING', 'CONSTANT'])
# TrendCD = Enum('Convergent', 'Divergent')

class CurveSection(object):
   """
   A section of the latency curve, where it has the same monotonicity.
   """
   def __init__(self, mon, istart, iend=None):
      """
      mon, the monotonicity
      istart, the start coordnate index
      iend,   the end coordnate index
      """
      self._mon    = mon
      self._istart = istart
      self._iend   = iend

   @property
   def monotonicity(self):
      return self._mon

   @property
   def istart(self):
      return self._istart

   @property
   def iend(self):
      return self._iend

   @iend.setter
   def iend(self, iend):
      self._iend = iend

   def __str__(self):
      return "CurveSection[%d, %d], monotonicity: %s" % (self._istart, self._iend, self._mon)


def cut_curve_by_inflections(coordinates, dfunc):
   """
   Cut the latency curve into sections by the tunning points.
   http://goo.gl/5brPIL cl263
   coords is short for coordinates
   dfunc is short for derivative function.
   """
   coords, sections = enumerate(coordinates), [] 
   decide_mon = lambda x: x>0 and Monotonicity.INCREASING \
         or (x<0 and Monotonicity.DECREASING or Monotonicity.CONSTANT)

   # current curve section that starts from the most recently found tunning point
   ccs = None

   for i,c in coords:
      m = decide_mon(dfunc(c))
      if Monotonicity.CONSTANT != m:
         if ccs is None:
            # Find the first non-zero derivative to decide
            # the first section monotonicity of the curve
            ccs = CurveSection(m, i)
            sections.append(ccs)
         elif Monotonicity.CONSTANT != m and ccs.monotonicity != m:
            # Set the previous section end coordinate index
            ccs.iend = i - 1

            # At coordinate c, the curve monotonicity turns
            # to the opposite monotonicity
            ccs = CurveSection(m, i)
            sections.append(ccs)

      # The curve is not a constant line.
      if ccs is not None:
         ccs .iend = len(coordinates) - 1

   return sections 

sections = cut_curve_by_inflections(fg_coords,  derivative_of_lc)
for sec in sections:
   print sec; 


class TrendArea:
   def __init__(self, ifunc, atfunc, lcfunc):
      """
        ifunc  is the integral function. It can provides the curve area.
        atfunc is a area threshold function. It provides the area threshold.
      """
      self._ifunc, self._atfunc, self._lcfunc  = ifunc, atfunc, lcfunc


   def calc(self, start_coord, end_coord, mon):
      """
      Get the trend area of the curve section. Trend area(ta) is definied by
        + if mon is DECREASING, ta = a(section) - ra(section)
        + if mon is INCREASING and a = area(section) - atfunc(section)
            * a < 0 then ta = 0
            * a > 0 then ta = a
      rafunc is the function to get the reactangle area, which is defined by
         rafunc = min(lcfunc(start_coord), lcfunc(end_coord) * (end_coord - start_coord)
      atfunc is a area threshold function. It provides the area threshold.
      """
      # ta is the trend area
      ta = 0
      # sa is the a(section) in above, i.e. the area of the curve section
      sa = abs(self._ifunc(end_coord) - self._ifunc(start_coord))
      if mon == Monotonicity.DECREASING:
         ys, ye = self._lcfunc(start_coord), self._lcfunc(end_coord)
         ra = (end_coord-start_coord)*(ys>ye and ye or ys)
         ta = ra - sa # a minus value
      else:
         a =  sa - self._atfunc(start_coord, end_coord)
         ta = a > 0 and a or 0

      return ta

def make_area_threshold_func(lcfunc):
   """
   Take the right-angle ladder-shaped area as the area threshold.
   The ladder-shaped angle tangent value is THREAHOLD_SLOPE.
   For a monotone increasing section, it will be considered as
   upwards trends when the section area is above the threshold
   area.
   """
   # ra is reactangle area.
   ra = lambda s,e,ys,ye: (e-s)*(ys>ye and ye or ys)
   # ta is triangle area.
   ta = lambda s,e: 0.5 * (e-s) * THREAHOLD_SLOPE*(e-s)

   def atfunc(s, e):
      """
      ladder-shaped area = triangle area + reactangle area
      """
      ys, ye = lcfunc(s), lcfunc(e) 
      return ra(s,e,ys,ye) + ta(s,e)

   return atfunc

atfunc = make_area_threshold_func(latency_curve_func)
ta = TrendArea(integral_of_lc, atfunc, latency_curve_func)

def accumulate_area(sections):
   """
   Get the sum of the trend area of the sections. 
   Each section must have the same monotonicity.
   """
   # acc_area is the accumulated trend area
   # fpa_sec is the first section which area is plus.
   acc_area, fpa_sec = 0, None
   for sec in sections:
      a = ta.calc(fg_coords[sec.istart], fg_coords[sec.iend], sec.monotonicity)
      acc_area += a

      if a > 0 and fpa_sec is None:
         fpa_sec = sec
   
   if acc_area <=0:
      return None
   else:
      return (fpa_sec, acc_area)

retobj = accumulate_area(sections)
if retobj is None:
   print "Conclusion: Not a upward trend"
else:
   print "Conclusion: A upward trend detected: %s, and the acc_area %d" % retobj
   print "Start from the coordinate: %d" % int(round(fg_coords[retobj[0].istart]))




def mediate(array):
   array.sort()
   l = len(array)
   if l < 1:
      raise ValueError("Cannot get the mediate value of an empty array")
   if 0 == l%2:
      half = l/2
      return (array[half] + array[half+1]) / 2
   else:
      return array[int(round(float(l)/2))]

def get_area_mean(coords, i, j, ifunc):
   """
   Get the mean value in domain [i,j] by area.
   As the perspective of geometry, the mean is
   the reactangle height, where it width is
   (j - i)
   ifunc: the integral function. 
   """
   return (ifunc(coords[j])-ifunc(coords[i])) / (coords[j]-coords[i])

area_mean = get_area_mean(coordinates, 0, -1, integral_of_lc)
series_mean, series_mediate = np.mean(series), mediate(series)

trend_mean = min(area_mean, series_mean, series_mediate)
print "area mean: %f, series mean: %f, series mediate: %f. trend mean[min of them]: %s" % (area_mean, series_mean, series_mediate, trend_mean)

recent_series = series[-RECENT_SERIES_SIZE:]
recent_mean, recent_mediate = np.mean(recent_series),  mediate(recent_series)
recent_area_mean = get_area_mean(coordinates, -RECENT_SERIES_SIZE, -1, integral_of_lc)
recent_trend_mean = max(recent_mean, recent_mediate, recent_area_mean)
print "recent area mean: %f, recent series mean: %f, recent series mediate: %f, recent trend mean[min of them]: %f" % (recent_area_mean, recent_mean, recent_mediate, recent_trend_mean)

guardline = trend_mean * (1-THREAHOLD_SLOPE)
recent_latency_delta = trend_mean*(1-THREAHOLD_SLOPE) - recent_trend_mean 
print "SLOPE: %f, guardline: %f, recent trend delta: %f" % (THREAHOLD_SLOPE, guardline, recent_latency_delta)

if retobj is not None:
   if recent_latency_delta < 0:
      print "Conclusion: Latency increases around %f[%f]" % (-recent_latency_delta, -float(recent_latency_delta)/guardline)
   else:
      # How much was increased
      print "Conclusion: It is cooling down[%f] recently although it a precarious upward trends." % float(recent_trend_mean)/trend_mean

# TBD: Much more friendly. Top N big sections.
# Make sure big sectinon swallows smallers to avoid temporary/short
# decreasing section affected TBD
