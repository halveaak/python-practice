def cellBill(time, texts):
  total = 8.00

  if time > 90:
    total = total + (time - 90) * 0.20

  if texts > 60:
    total = total +(texts - 60) * 0.10

  total = total + 0.72
  end_total = total * 1.07

  return round(end_total, 2)