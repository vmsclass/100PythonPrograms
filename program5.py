# program for swapping two numbers without using temp variable. 
A = int(input("Enter the value for A "))
B = int(input("Enter the value for B "))

A = A + B
B = A - B
A = A - B

print("After Swapping")

print("A = ", A)
print("B = ", B)


