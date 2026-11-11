def carFee(days, start, end):
  miles = (end - start) * 0.28
  time = days * 40
  total = miles + time
  return total