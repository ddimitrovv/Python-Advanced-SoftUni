# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines,
# you will be receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade,
# formatted to the second decimal point in the format:
# "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

n = int(input())

book = dict()

for _ in range(n):
    info = input()
    student, grade = info.split()

    if student not in book:
        book[student] = list()
    book[student].append(float(grade))

for student, grades in book.items():
    average = sum(grades) / len(grades)
    formatted_grades = " ".join(f"{grade:.2f}" for grade in grades)
    print(f'{student} -> {formatted_grades} (avg: {average:.2f})')
