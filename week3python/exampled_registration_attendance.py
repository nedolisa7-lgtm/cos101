# Matric Number: VUG/SEN/26/17164
print("Registration and Attendance")
registration_status=input("Registration complete? Enter yes or no: ")
if registration_status=="no":
    print("please register")
elif registration_status=="":
    print("error")
elif registration_status=="yes":
    attendance=float(input("Enter your attendance percentage: "))
    if attendance<0 or attendance>100:
        print("error, wrong value inputed")
    else:
        if attendance<75:
            print("Low attendance, you may not participate in the practical assessment")
        else:
            print("you may participate in the practical assessment")
else:
    print("error!")
