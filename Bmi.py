def getCategory(weight, height, inches):
  inc = (height * 12) + inches
  bmi = (weight * 703) / (inc ** 2)
  
  if bmi < 18.5:
    return "underweight"
  elif bmi < 25: 
    return "normal"
  elif bmi < 30:
    return "overweight"
  else:
    return "obese"
    