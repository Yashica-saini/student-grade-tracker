# data given in the assignment
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]


# printing subject marks and grade
print("Student :", student_name)
print()


for i in range(len(subjects)):

    subject = subjects[i]
    mark = marks[i]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subject, ":", mark, "-", grade)
# total marks
total = sum(marks)
print("\nTotal Marks :", total)

# average marks
average = total / len(marks)
print("Average Marks :", round(average, 2))


# highest subject
highest_mark = max(marks)
index = marks.index(highest_mark)
highest_subject = subjects[index]

print("Highest Scoring Subject :", highest_subject, "-", highest_mark)


# lowest subject
lowest_mark = min(marks)
index = marks.index(lowest_mark)
lowest_subject = subjects[index]

print("Lowest Scoring Subject :", lowest_subject, "-", lowest_mark)


# marks entry system
print("\nAdd new subjects (type 'done' to stop)")

new_subjects = 0

while True:

    subject = input("Enter subject name: ")
    if subject.lower() == "done":
        break
    mark_input = input("Enter marks (0-100): ")
    try:

        mark = int(mark_input)
        if mark < 0 or mark > 100:
            print("Invalid marks. Enter between 0 and 100.")
            continue
    except:
        print("Invalid input. Please enter a number.")
        continue

    subjects.append(subject)
    marks.append(mark)

    new_subjects += 1

    print("Subject added successfully.\n")

print("\nNew subjects added:", new_subjects)
updated_total = sum(marks)
updated_average = updated_total / len(marks)
print("Updated Average Marks:", round(updated_average, 2))