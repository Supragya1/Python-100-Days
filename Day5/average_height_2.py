student_heights = input("Enter the heights of studnets\n").split() # when you use split() it will split the string into a list of strings
sum = 0
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
    sum += student_heights[i]
print("Total height =",sum)
print("number of students =",len(student_heights))
print("average height =",round(sum/len(student_heights)))