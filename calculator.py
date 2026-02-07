a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
ch = input("Enter your choice: + for addition, - for subtraction, * for multiplication, / for division")

if ch == '+':
    print("Sum =",a+b)
elif ch == '-':
    print("Difference =",a-b)
elif ch == '*': 
    print("Product =",a*b)          
elif ch == '/':
    if b != 0:
        print("Quotient =",a/b)
    else:
        print("Error: Division by zero is not allowed.")    
else:
    print("Invalid choice")