student_scores = input("Enter the marks of studnets\n").split()
max = float('-inf')
for i in range(0,len(student_scores)):
    student_scores[i] = int(student_scores[i])
    if(max<student_scores[i]):
        max = student_scores[i]
print("The highest score in the class is:",max)