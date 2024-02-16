# a list stores a sequence of elements which can be of different types
print("List with integers")
list1 = [1, 3, 5, 7, 100]
print(list1)

print("\nList with strings")
list2= ['hello']*5
print(list2)

print("\nList with integers and strings")
list3 = list1 + list2
print(list3)
print(len(list3))

print("\nList with mixed types")
list4 = [1,3.2, 'hello', True]
print(list4)
print("\nPrinting list using for loop")
for i in range(len(list4)):
    print(list4[i])

print("\nPrinting list with list as an element")
list5 = [1, 2 , 3.2 , list4 , "hello"]
print(list5)
print("\nPrinting outer list only")
for i in range(len(list5)):
    print(list5[i])

print("\nprinting inner list too")
for i in range(len(list5)):
    if isinstance(list5[i],list):
        for j in range(len(list5[i])):
            print(list5[i][j])
    else:
        print(list5[i])

print("\nPrinting list elements using index")
print(list5[0])
print(list5[3][2])
print(list5[3][3])
