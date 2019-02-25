import math
k = 0
n = int(input("Enter the number : "))
z = 0
for i in range(1,n+1):
    for i in range (1,n+1):
        if (n % i == 0):
            j = math.pow(i,2)
            k = k + j
    n = n-1
z = z + k
print(z)
