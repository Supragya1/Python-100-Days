import random
print("Welcome to the Password Generator!")
print("This program will generate a password for you.")
n = int(input("How many letters you want in your password?\n"))
sym = int(input("How many symbols you want in your password?\n"))
num = int(input("How many numbers you want in your password?\n"))
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','(',')','_','+']
password = []
for i in range(n):
    password.append(random.choice(alpha))
for i in range(sym):
    password.append(random.choice(symbol))
for i in range(num):
    password.append(random.choice(number))
random.shuffle(password)
password = ''.join(password)
print(password)