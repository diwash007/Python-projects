year = int(input("Which year do you want to check? "))

if year%4==0:
  if(year%100!=0):
    print("leap year!!")
  else:
    if year%400==0:
      print("leap year")
    else:
      print("Not a leap year!!")
else:
  print("Not a leap year!!")

