def my_function():
    print("You are calling a function")

my_function()

def add(a, b):
    return a + b

print(add(3, 4))

def list_sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(list_sum([1, 2, 3, 4, 5]))