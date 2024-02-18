import random
names = input("Enter the names of the people separated by commas: ")
name_list = names.split(",")
choose = random.randint(0,len(name_list)-1)
print(name_list[choose],"is going to buy the meal today!")