act = int(input("ACT Score? "))
gpa = float(input("GPA? "))
subj = int(input("Years of core subjects? "))

rai = 3 * (act) + 30 * (gpa) + 5 * (subj)



if (rai) >= 245:
  print("Yes")
elif (rai) < 245:
  print("No")