# Matric Number: VUG/SEN/26/17164
numberofday=int(input("Number Of Days: "))
while numberofday<=0:
    print("ERROR")
    numberofday=int(input("Number Of Days: "))
totalsales=0
day=1
while day<=numberofday:
    sales_amount=int(input(f"Day {day} amount: "))
    while sales_amount<0:
        print("ERROR")
        sales_amount=int(input(f"Day {day} amount: "))
    totalsales=totalsales+sales_amount
    day=day+1
averagedaily=totalsales/numberofday
print(f"Total Sales: NGN{totalsales:.2F}")
print(f"Average Daily Sales: NGN{averagedaily:.2F}")
