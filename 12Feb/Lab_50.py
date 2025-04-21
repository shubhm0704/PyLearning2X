# Fibonacci

#a = 10
#b = 12
#a, b = a, a+b
#print(a, b)

a, b = 0, 1
while a < 10:
    print(a, end=" | ")
    a, b = b, b + a
