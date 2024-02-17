list1 = [1, 3, 5, 7, 100]
list2= ['hello']*5
# append
print(list1)
list1.append(50)
list1.append(100)
print(list1)

# insert
print("\nInserting element at a specific index")
list1.insert(1, 200)
print(list1)

# extend
print("\nExtending list")
list1.extend([300, 400, 500])
print(list1)
list1.extend(list2)
print(list1)

# remove 
print("\nRemoving element from list")
list1.remove(3) # removes the first occurence of 3
print(list1)
# if element is not present, it throws an error

# pop
print("\nPopping element from list")
list1.pop() # removes the last element
print(list1)
list1.pop(0) # removes the element at index 1 
print(list1)

# index
print("\nIndex of element")
print(list1.index(7))
print(list1.index(100, 1, 4)) # value, start, end

# count
print("\nCount of element")
print(list1.count(100))
print(list1.count(300))

# sort It throws an error if the list contains elements of different types
list3 = [9, 20, 3, 4, 5, 6, 7, 8, 1, 2]
print("\nSorting list")
list3.sort()
print(list3)
list3.sort(reverse=True) # descending order
print(list3)

# reverse
print("\nReversing list")
list1.reverse()
print(list1)

# copy
print("\nCopying list")
list4 = list3.copy()
print(list4)

# list slicing
print("\nList slicing")
print(list4[0:3])
print(list4[:3])
print(list4[3:])
print(list4[:])

# clear
print("\nClearing list")
list1.clear()
print(list1)