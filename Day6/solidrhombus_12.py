def solidrhombus(n):
    for i in range(n):
        for j in range(1,n-i):
            print(" ",end="")
        for j in range(n):
            print("*",end="")
        print("")
n = int(input("Enter the value of rows:\n"))
solidrhombus(n)
'''
    *****
   *****
  *****
 *****
*****
'''