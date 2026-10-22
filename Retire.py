age = float( input("Age? "))
svc = float( input("Years of service? "))

if age >= 65:
  yn = "Yes"
elif age >= 62 and svc >= 20:
  yn = "Yes"
elif age+svc >=88:
  yn = "Yes"
else:
  yn= "No"
print(yn)
