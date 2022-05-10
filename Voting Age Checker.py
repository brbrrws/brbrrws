voting = 18
age = int(input("Enter your age:"))
if age >= 18:
  print("You're able to vote! GO DO SO!")
else:
  remain = voting - age
  if remain <= 1:
      print("You're not able to vote yet... try again in approximately" ,remain, "year.")
  else:
    print("You're not able to vote yet... try again in approximately" ,remain, "years.")
