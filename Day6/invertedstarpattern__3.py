def inverted_star_pattern(n):
    i=n
    for i in range(n,0,-1):
        print("*"*i)
n = int(input("Enter the value of n:\n"))
inverted_star_pattern(n)
'''
******
*****
****
***
**
*
'''