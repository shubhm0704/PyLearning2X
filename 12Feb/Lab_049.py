# Factorial
# n = 5
# 5*4*3*2*1

number = int(input("Enter number\n"))
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i  # Corrected this line
    print("Factorial ->>", fact)


