# membership operators - in, not in

# directory
grades = {"Min":"A",
          "Mac":"B",
          "Aeli":"C"}

student_name = input("Enter student name: ")
if student_name in grades:
    print(f"{student_name} got grade {grades[student_name]}")
else:
    print('not found')


#########

#string
word = "APPLE"

letter = input("Guess a letter in the secret word:")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")

#########

# array
students = {"Min", "Mac", "Aeli"}
student = input("Enter a student name: ")

if student in students:
    print(f"Student {student} is found")
else:
    print(f"Student {student} is not found")