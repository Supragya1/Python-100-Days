n = int(input("Enter value of n till where you want to print Fizz Buzz: \n"))
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)