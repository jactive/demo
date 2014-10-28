# See http://en.wikipedia.org/wiki/Simple_linear_regression
class SimpleLinearRegression
  attr_reader :series
  attr_reader :coordinates

  def initialize(series, coordinates=nil)
    @coordinates, @series = coordinates, series
    @coordinates = (1..@series.length).to_a unless @coordinates

    if @coordinates.length != @series.length
      errmsg = "Timeline mismatch time series data points number.(#{@coordinates.length}!=#{@series.length}"
      raise ArgumentError.new(errmsg)
    end
  end

  # Fitting the regression line
  def estimateTrend
    # see http://goo.gl/0yT4tA the following variable meaning
    s_x  = sum(@coordinates)
    s_y  = sum(@series)
    s_xx = sum(@coordinates) { |x| x * x }
    s_yy = sum(@series) { |y| y * y }
    s_xy = sum_product(@coordinates, @series)

    n = series.length
    # Calculate the slope, i.e. beta^ at http://goo.gl/ZDBEX8
    (n*s_xy - s_x*s_y).to_f/(n*s_xx - s_x*s_x)
  end

  private
  def sum(sequence)
    sequence.inject(0) do |total, elem|
      elem = yield elem if block_given?
      total + elem
    end
  end

  def sum_product(seq1, seq2)
    total = 0
    seq1.each_index { |i| total += seq1[i] * seq2[i] }
    return total
  end
end

if __FILE__ == $0
  slr = SimpleLinearRegression.new([1,2,3,4,5,6])
  print slr.estimateTrend, "\n"

  coordinates = [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
  series = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]
  slr = SimpleLinearRegression.new(series, coordinates)
  # http://goo.gl/abQUSL
  print slr.estimateTrend, "\n"
end
