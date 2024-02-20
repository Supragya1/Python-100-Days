def FloydsTriangle(n):
    k=1
    for i in range(n):
        for j in range(i+1):
            print(f"{k}",end=" ")
            k+=1
        print("")
n = int(input("Enter the value of rows:\n"))
FloydsTriangle(n)
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''