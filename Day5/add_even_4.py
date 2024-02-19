n = int(input("Enter the number till where you want to find even sum\n")) 
sum = 0
for i in range(n+1):
    if(i%2==0):
        sum+=i
print(sum)
sum = 0
for i in range(0,n+1,2):
    sum+=i
print(sum)
