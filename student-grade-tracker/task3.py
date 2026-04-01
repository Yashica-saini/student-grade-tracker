# class data given in the assignment
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# printing report header
print("Name              | Average | Status")
print("----------------------------------------")

# variables to track results
pass_count = 0
fail_count = 0
total_average_sum = 0
topper_name = ""
topper_average = 0

# loop through all students
for student in class_data:
    name = student[0]
    marks = student[1]

    # calculating average marks
    avg = sum(marks) / len(marks)
    avg = round(avg, 2)
    total_average_sum += avg

    # deciding pass or fail
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    # checking for class topper
    if avg > topper_average:
        topper_average = avg
        topper_name = name

    # printing the row in table format
    print(f"{name:<18} | {avg:6.2f} | {status}")

# summary information
print("\nStudents Passed:", pass_count)
print("Students Failed:", fail_count)
print("Class Topper:", topper_name, "-", topper_average)
class_average = total_average_sum / len(class_data)
print("Class Average:", round(class_average, 2))