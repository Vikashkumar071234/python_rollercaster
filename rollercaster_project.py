print("Welcome to the rollercaster!")
height=int(input("What is your height in cm?"))

if height >=120:
  print("you can ride the rollercaster")
  age=int(input("How old are you?"))
  if age>=18:
    bill= 12
    print("your bill is $12")
  elif age >=12:
    bill=10
    print("your bill is $10")
  else:
    bill=5
    print("your bill is $5")
  picture=(input("you need picture? Y or N."))
  if picture =="y":
    bill +=3
    print(f"your final bill is ${bill}")
  else:
    print(f"your final bill is ${bill}")
else:
  print("you can't ride the rollercaster")
