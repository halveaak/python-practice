def orderStatus(reg, large, pastries):
  reg = (reg) * 95
  large = (large) * 150
  amount = reg + large

  if amount >= 300:
    return "Switch to decaf"
  elif amount < 400 and pastries > "1":
    return "Serve coffee"
  elif amount > 400:
    return "Switch to decaf"
  else:
    return "Serve coffee"