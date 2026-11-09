# Matric Number: VUG/SEN/26/17164
days=int(input("Number Of Days: "))
total=0
greater_day=0
less_day=0
while days<=0:
    print("ERROR")
    days=int(input("Number Of Days: "))
for i in range(1,days+1):
    sales=int(input(f"Sales For Day{i}: "))
    while sales<0:
        print("error, sales cannot be negative")
        sales=int(input(f"Sales For Day{i}: "))
    total+=sales
    if sales>10000:
        greater_day+=1
    else:
        less_day+=1
average=total/days
print(f"Total Sales: NGN{total:.2F}")
print(f"Average Daily Sales: NGN{average:.2F}")
print(f"Days Above NGN10000: {greater_day}")
print(f"Days At Or Below NGN10000: {less_day}")
