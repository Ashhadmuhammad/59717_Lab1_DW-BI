def gradecov(grade):
    if grade >= 90 and grade <= 100:
        return 4.0
    elif grade >= 80 and grade < 90:
        return 4.0
    elif grade >= 75 and grade < 80:
        return 3.5
    elif grade >= 70 and grade < 75:
        return 3.0
    elif grade >= 65 and grade < 70:
        return 2.5
    elif grade >= 60 and grade < 65:
        return 2.0
    elif grade >= 55 and grade < 60:
        return 1.5
    elif grade >= 50 and grade < 55:
        return 1.0
    else:
        return 0.0


a = int(input("Enter your number of courses: "))

total_cr = 0
total_points = 0

for x in range(a):

    marks = int(input("Enter marks of course " + str(x + 1) + ": "))

    i = gradecov(marks)

    cr = int(input("Enter credit hours of course " + str(x + 1) + ": "))

    total_cr = total_cr + cr

    points = i * cr

    total_points = total_points + points

gpa = total_points / total_cr

print("Your GPA is:", gpa)

previous_cr = int(input("Enter previous total credit hours: "))
previous_points = float(input("Enter previous total points: "))

total_cr = previous_cr + total_cr
total_points = previous_points + total_points

cgpa = total_points / total_cr

print("Your CGPA is:", round(cgpa, 2))