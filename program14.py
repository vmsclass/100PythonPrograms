#program to print the sum of n numbers
n = int(input("Enter the n value"))
total = 0

for i in range(1,n+1):
    total = total + i

print("The total sum is",total)
