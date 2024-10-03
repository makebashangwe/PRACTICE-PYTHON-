name = input ("Please enter your name: ")
user_subjects = []
subjects = input("Please enter three subjects seperated by commas below: ")
if "," in subjects:
    subjects = subjects.split(",")
    for subject in subjects:
        user_subjects.append(subject.strip())

user_grades = []
grades = input("Please enter the three associated number grades in order seperated by commas below: ")
if "," in grades:
    grades = grades.split(",")
    for grade in grades:
        user_grades.append(float(grade.strip()))

total_sum = sum(user_grades)
average = total_sum/len(user_grades)

print(f"Student: {name}")
print(f"Average Grade: {average:.2f}")

if average >=90:
    final_grade = 'A'
elif average >=80:
    final_grade = 'B'
elif average >=70:
    final_grade = 'C'
elif average >=60:
    final_grade = 'D'
else:
    final_grade = 'F'

if final_grade == 'A':
    GPA = "4.0"
elif final_grade == 'B':
    GPA = "3.0"
elif final_grade == 'C':
    GPA = "2.0"
else:
    GPA = "1.0"
print(f"Final Grade: {final_grade}")
print(f"GPA: {GPA}")