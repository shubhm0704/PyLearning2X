#Year is Leap or not

year = int(input("Enter the year:"))

if (year % 4 ==0 and year % 100 != 0):
    print("Input Value is Leap Year")
elif(year % 400 ==0):
    print("Input Value is a leap year")
else:
    print("Input is not a leap year")
