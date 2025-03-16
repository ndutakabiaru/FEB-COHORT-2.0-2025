# Nested conditionals  
num = int(input("Enter a number "))

if num % 2 == 0:  
    print("Even number")  
    if num > 0:  
        print("Also positive!")  
else:  
    print("Odd number")
