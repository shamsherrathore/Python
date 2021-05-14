student_name = str(input("enter the student name:"))
print('<<<<<<<<<wecome to the RANA group of college>>>>>>>>>')
n = int(input("enter the the subjects:"))
total_marks = 0
print("enter marks")
for i in range (1, n+1):
    marks = float(input("subject"+str(i)+":"))
    assert marks>=0 and marks<=100
    total_marks += marks
print('*******************************************************************')
print('student name:', student_name,'                        total marks scored:',total_marks)
percentages = total_marks/n
print("total percentage of student is:",percentages)
if percentages>90 and percentages<=100:
    prize = "ferrari"
    print("congrats you won:",prize)
elif percentages>80 and percentages<=90:
    prize = "audi"
    print("congrats you won:",prize)
elif percentages >50 and percentages<=80:
    prize = "bullet"
    print("congrats you won:",prize)
else:
    print("congrats you won: auto")
print("\n>>>>>end of the result<<<<<")
