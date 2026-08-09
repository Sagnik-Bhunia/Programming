s1 = float(input("Enter marks for subject 1: "))
s2 = float(input("Enter marks for subject 2: "))
s3 = float(input("Enter marks for subject 3: "))
average = (s1 + s2 + s3) / 3
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Average:", average, "%")
print("Grade:", grade)
