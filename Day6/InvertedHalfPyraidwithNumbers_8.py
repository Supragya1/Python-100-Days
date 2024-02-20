def InvertedHalfPyraidwithNumbers(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end="")
        print()
n = int(input("Enter the value of rows:\n"))
InvertedHalfPyraidwithNumbers(n)
'''
12345
1234
123
12
1
'''