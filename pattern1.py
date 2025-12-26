n = 5
for i in range(n):
    x= "*" * (i+1) + " " * (2*(n-i-1)) + "*" * (i+1)
    print(x)
for i in range(n-2,-1,-1):
    x= "*" * (i+1) + " " * (2*(n-i-1)) + "*" * (i+1)
    print(x)