def hollow_rectangle(n,m):
    for i in range(n):
        for j in range(m):
            if(i==0 or j==0 or i== n-1 or j==m-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()
n = int(input("Enter the value of rows:\n"))
m = int(input("Enter the value of columns:\n"))
hollow_rectangle(n, m)
'''
******
*    *
*    *
*    *
******
'''