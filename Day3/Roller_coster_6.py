print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?\n"))
bill=0
if height > 120:
    age = int(input("Enter your age\n"))
    if age<=12 :
        print("Ticket price of Rs 100")
        can_pay = (input("Can you Pay? (Y or N) \n"))
        if can_pay == "Y" or can_pay == "y":
            bill+=100
            print("Rs 100 deducted .....\nBalance Unlimited")
        else:
            print("Sorry, you can't enter without paying")
    elif age >12 and age<=18:
        bill+=150
        print("Ticket price of Rs 150")
        can_pay = (input("Can you Pay? (Y or N) \n"))
        if can_pay == "Y" or can_pay == "y":
            print("Rs 150 deducted .....\nBalance Unlimited")
        else:
            print("Sorry, you can't enter without paying")
    else:
        print("Ticket price of Rs 200")
        can_pay = (input("Can you Pay? (Y or N) \n"))
        if can_pay == "Y" or can_pay == "y":
            bill+=200
            print("Rs 200 deducted .....\nBalance Unlimited")
    pic = input("Do you want a photo taken for Rs 50? (Y or N)\n")
    if pic == "y" or pic =="Y":
        bill+=50
        print("Rs 50 deducted .....\nBalance Unlimited")
        print("Welcome to the rollercoaster ride!")
else:
    print("Sorry, you can't enter because your height is below the required.")
print("Your total spenditure = ",bill)