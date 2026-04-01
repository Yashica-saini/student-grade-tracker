# Raw student data given in the assignment
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# looping through each student in the raw data
for student in raw_students:

    # cleaning the name
    # strip() removes extra spaces and title() fixes the casing
    clean_name = student["name"].strip().title()
    # converting roll number from string to integer
    roll_no = int(student["roll"])


    # converting marks string into list of integers
    marks_split = student["marks_str"].split(",")
    marks = []
    for m in marks_split:
        marks.append(int(m))   # converting each mark into integer

    # checking if the name is valid
    # a valid name should contain only alphabets
    words = clean_name.split()
    valid_name = True


    for w in words:
        if not w.isalpha():
            valid_name = False
            break


    # printing validation result
    if valid_name:
        print("Valid name")
    else:
        print("Invalid name")

    # printing formatted student profile card
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {roll_no}")
    print(f"Marks   : {marks}")
    print("================================")
# after processing all students
# find the student with roll number 103

for student in raw_students:

    roll_no = int(student["roll"])

    if roll_no == 103:

        name = student["name"].strip().title()

        print("\nName for Roll 103 in different formats:")
        print(name.upper())   # all caps
        print(name.lower())   # lowercase