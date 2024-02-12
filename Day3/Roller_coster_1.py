print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?\n"))
if height > 120:
    print("Pay price of Rs 150")
    can_pay = (input("Can you Pay\n"))
    if can_pay == "True" or can_pay == "Yes" or can_pay == "yes" or can_pay == "true":
        print("Rs 150 deducted .....\nBalance Unlimited\n")
        print("Welcome to the rollercoaster ride!")
    else:
        print("Sorry, you can't enter without paying")
else:
    print("Sorry, you can't enter because your height is below the required.")
