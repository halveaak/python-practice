cdy = float(input("Cloud cover? "))

if cdy == 0:
  print("Clear")
elif cdy < 25:
  print("Few Clouds")
elif cdy < 50:
  print("Scattered Clouds")
elif cdy < 75:
  print("Broken Clouds")
else:
  print("Overcast")