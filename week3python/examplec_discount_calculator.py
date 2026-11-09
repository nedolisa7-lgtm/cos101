# Matric Number: VUG/SEN/26/17164
print("Discount Calculator")
original_amount=int(input("Original Amount: "))
if original_amount<0:
    print("ERROR")
else:
    if original_amount< 10000:
        discount=(0/100)*original_amount
        print(f"Discount amount: N{discount}")
        total1= original_amount-discount
        print(f"Amount payable: N{total1}")
    elif original_amount==10000 or original_amount<50000:
        discount_1=(5/100)*original_amount
        print(f"Discount amount: N{discount_1}")
        total2= original_amount-discount_1
        print(f"Amount payable: N{total2}")
    elif original_amount>=50000:
        discount_2=(10/100)*original_amount
        print(f"Discount amount: N{discount_2}")
        total3= original_amount-discount_2
        print(f"Amount payable: N{total3}")


          

    
