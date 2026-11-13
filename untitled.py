def shopDiscount(hours, certificate):
    
  if hours < 10:
    amount = 10
  elif hours < 20: 
    amount = 20
  else:
    amount = 30

  if certificate == "y":
    discount = 15
  else: 
    discount = 0
    
  total = amount + discount
  return total
