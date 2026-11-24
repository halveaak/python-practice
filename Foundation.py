def howLong(invest, rate):
  goal = invest * 2
  years = 0
  while invest < goal:
    invest = invest + (invest * (rate / 100))
    years = years +1
  return years
