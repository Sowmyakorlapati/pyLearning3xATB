# Fibonacci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8
n=int(input("Enter the Fibonacci Number:"))
a, b =0, 1
print(a)
print(b)
for i in range(2, n):
    c=a+b
    a=b
    b=c
    print(c)