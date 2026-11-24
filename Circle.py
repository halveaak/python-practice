def leibniz(n):
  total = 0
  denom = 1
  sign = 1
  count = 0
  while count < n:
    total = total + (sign * (1 / denom))
    denom = denom + 2
    sign = sign * -1
    count = count + 1
  return total * 4
  