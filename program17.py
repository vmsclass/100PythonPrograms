# program to print the fibonacci series of n terms

n = int(input("Enter the number of terms you want: "))

a = 0
b = 1

print("Fibonacci series : ")

print(a)
print(b)

for i in range(n-2):
    c = a + b
    print(c)
    a = b
    b = c
    
    
