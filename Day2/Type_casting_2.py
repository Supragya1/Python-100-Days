num = len(input("What is your name?\n"))
num = str(num)
print("Your name has " + num + " characters.")

a = 123
print(type(a))
a = str(a)
print(type(a))
a = float(a)
print(f"{a} {type(a)}")
a = bool(a)
print(f"{a} {type(a)}")

print(100+int("100"))
print(str(100)+str(100))

two_digit_number = int(input("Type a two digit number: "))
sum=0
sum += int(str(two_digit_number)[0])
sum += int(str(two_digit_number)[1])
print(f"Sum of digits: {sum}")