print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
name2 = input("What is your partner name?\n")
combine = name1.lower()+name2.lower()
first_digit = combine.count("t")+combine.count("r")+combine.count("u")+combine.count("e")
first_digit1 = 0 
if first_digit >=10:
  first_digit1+= int(str(first_digit)[0])+int(str(first_digit)[1])
else:
    first_digit1= first_digit
second_digit = combine.count("l")+combine.count("o")+combine.count("v")+combine.count("e")
second_digit1 = 0 
if second_digit >=10:
  second_digit1+= int(str(second_digit)[0])+int(str(second_digit)[1])
else:
    second_digit1 = second_digit
result = first_digit1*10+second_digit1

if result < 10 or result > 90:
  print(f"Your score is {result}%, you go together like coke and mentos.")
elif result > 40 and result < 50:
  print(f"Your score is {result}%, you are alright together.")
else:
  print(f"Your score is {result}%, you are good together.")