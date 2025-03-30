def calculate_discount(original_price,percentage_discount):
   
    if  percentage_discount >= 20:
       discount_amount=(percentage_discount/100)*original_price
       final_price=original_price - discount_amount
       return final_price
    else:
      return original_price
try:
   original_price=float(input("Enter the original price ->"))
   percentage_discount=float(input("Enter the percentage discount ->"))

   final_price=calculate_discount(original_price,percentage_discount)
   print(f"Final price ->{final_price:.2f}")

except ValueError:
   print("Invalid input.Please enter a numeric value")

