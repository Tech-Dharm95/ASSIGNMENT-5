students_marks = {'Alice': 85, 'Deepak': 45, 'Joe': 75}
stud_name=input("Enter the student's name: ")
if stud_name in students_marks:
    print(f"{stud_name}'s marks:{students_marks[stud_name]}")
else:
    print(f"{stud_name}'s,students not found")

