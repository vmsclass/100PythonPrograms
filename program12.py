# program for basic calculator between two numbers

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")

choice = int(input("Enter your choice"))

if choice == 1:
    print("Result = ",num1+num2)
elif choice == 2:
    print("Result = ",num1-num2)
elif choice == 3:
    print("Result = ",num1*num2)
elif choice == 4:
    print("Result = ",num1//num2)
else:
    print("Invalid Choice")

