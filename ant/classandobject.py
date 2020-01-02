from classStudent import Student

student1 = Student("amien kurniawan","Computer Engineering",3.4,False)
student2 = Student("Arief Nur Prakoso","Computer Engineering",3.79,True)

print(student1.name,student1.gpa)
print(student2.name,student2.gpa)

print(student1.on_honor())