print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want pepperoni? Y or N") 
extra_cheese = input("Do you want extra cheese? Y or N") 
sum=0
if size == "S":
  sum+=15
  if add_pepperoni == "Y" or add_pepperoni =="y":
    sum+=2
elif size == "M":
  sum+=20
  if add_pepperoni =="y" or add_pepperoni =="Y":
    sum+=3
elif size == "L":
  sum+=25
  if add_pepperoni =="y" or add_pepperoni =="Y":
    sum+=3
else:
  print("We have only large , medium and small pizzas")
if extra_cheese =="Y" or extra_cheese == "y":
  sum+=1
print(f"Your final bill is: ${sum}")