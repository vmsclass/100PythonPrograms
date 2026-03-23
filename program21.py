#program to find the given number is palindrome or not. 

num = int(input("Enter a number "))

original = num

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if rev == original:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")
    
