# Matric Number: VUG/SEN/26/17164
student_name=input("Student: ")
daily_transport_cost=int(input("Daily transport cost: "))
daily_feeding_cost=int(input("Daily feeding cost: "))
numbers_of_days=int(input("Days on campus: "))
if numbers_of_days<=-1:
    print("error, try again:(")
else:
    other_expesnses=int(input("Other expenses:"))
    transporttotal=daily_transport_cost*numbers_of_days
    feedingtotal=daily_feeding_cost*numbers_of_days
    weeklytotal=transporttotal+feedingtotal+other_expesnses
    weekly_budget=int(input("Weekly Budget: "))
    print(f"Student name: {student_name}")
    print(f"Transport total: NGN{transporttotal:.2F}")
    print(f"Feeding total: NGN{feedingtotal:.2F}")
    print(f"Other expenses: NGN{other_expesnses:.2F}")
    print(f"Weekly total: NGN{weeklytotal:.2F}")
    print(f"Weekly Budget: NGN{weekly_budget:.2F}")
    if weeklytotal==weekly_budget:
        print(" YOU ARE EXACTLY ON BUDGET")
    elif weeklytotal<weekly_budget:
        print("YOU ARE WITHIN BUDGET")
    elif weeklytotal>weekly_budget:
        print("YOU ARE OVER BUDGET")





