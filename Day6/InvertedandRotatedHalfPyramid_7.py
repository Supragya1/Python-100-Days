def inverted_and_rotated_half_pyramid(n):
    for i in range(n):
        for j in range(i+1,n):
            print(" ",end="")
        for j in range(n-i-1,n):
            print("*",end="")
        print("")
n = int(input("Enter the value of rows:\n"))
inverted_and_rotated_half_pyramid(n)
'''
    *
   **
  ***
 ****
*****   
'''