def inverted_and_rotated_half_pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i,i,-1):
            print("*"*j)
n = int(input("Enter the value of rows:\n"))
inverted_and_rotated_half_pyramid(n)
'''
    *
   **
  ***
 ****
*****   
'''