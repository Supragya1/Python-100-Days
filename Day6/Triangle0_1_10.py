def Triangle0_1(n):
    for i in range(n):
        for j in range(i+1):
            if((i+j)%2==0):
                print("1",end="")
            else:
                print("0",end="")
        print()

n = int(input("Enter the value of rows:\n"))
Triangle0_1(n)
'''
1
01
101
0101
10101
'''