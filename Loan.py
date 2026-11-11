def getsLoan(income, debt, house):
  hti = house / income
  dti = (debt + house) / income

  if hti <= 0.28 and dti <= 0.36:
    return true
  else: 
    return false
