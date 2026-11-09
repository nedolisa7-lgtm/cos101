# Matric Number: VUG/SEN/26/17164
print("Result Checker")
student=input("Name: ")
course_score=float(input("Coursework: "))
exam_score=float(input("Examination: "))
if course_score>30 or course_score<0:
    print("error")
elif exam_score>70 or exam_score<0:
    print("error")
else:
    print(f"Name: {student}")
    print(f"Coursework: {course_score}/30")
    print(f"Examination: {exam_score}/70")
    total=course_score+exam_score
    print(f"Total: {total}/100")
    if total>=72:
        print("Decision: pass")
        print("Grade: A")
    elif total>=62:
        print("Decision: pass")
        print("Grade: B")
    elif total>=50:
        print("Decision: pass")
        print("Grade: C")
    elif total>=49:
        print("Decision: Resit Required")
        print("Grade: D")
    else:
        print("Decision: Resit Required")
        print("Grade: F")
