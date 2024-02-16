def head_tail():
    choice=input("What is your choice?\n")
    import Head_Tails
    if choice.lower() == "head" and Head_Tails.a == 0:
        print("You Win")
    elif choice.lower() == "tail" and Head_Tails.a == 1:
        print("You Win")
    else:
        print("You Lose")

import random
a = random.randint(1,20)
print("A random integer between 1 and 20 is", a)
b = random.random() # random float between 0 and 1 not including 1
print("A random float between 0 and 1 is", b)
print("A random float between 0 and 100 is", b*100) # random float between 0 and 100 and not including 100
x = int(input("Enter the lower limit: "))
y = int(input("Enter the upper limit: "))
print(f"A random float between {x}and {y} = ", random.uniform(x,y)) # random float between x and y not including y

print("Wanna Play Head and Tail? (Y or N)")
play=input()
if play.lower() == "y":
    head_tail()
else:
    print("Okay, Bye!")

