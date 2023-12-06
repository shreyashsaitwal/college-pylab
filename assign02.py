# The marks obtained by a student in 3 different subjects are input by the
# user. Python program should calculate the average marks obtained in 3
# subjects and display the grade. The student gets a grade as per the
# following rules:
# Average Grade
# 90-100  O
# 80-89   A
# 70-79   B
# 60-69   C
# 40-59   D
# 0-39    F

inp = input("Enter marks separated by space: ").split(" ")
marks = list(map(lambda x: int(x), inp))
avg = sum(marks) / len(marks)
print(f"Average: {avg}")

if avg >= 90:
    print("Grade: O")
elif avg >= 80:
    print("Grade: A")
elif avg >= 70:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
elif avg >= 40:
    print("Grade: D")
else:
    print("Grade: F")
