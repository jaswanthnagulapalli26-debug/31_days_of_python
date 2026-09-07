python_marks = int(input("Enter Python marks: "))
dbms_marks = int(input("Enter DBMS marks: "))
java_marks = int(input("Enter Java marks: "))
total = python_marks + dbms_marks + java_marks
average = total / 3
print("Total:", total)
print("Average:", average)
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")