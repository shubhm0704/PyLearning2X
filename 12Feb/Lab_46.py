# Triangle Classifier
a = float(input("Enter Value of side1:"))
b = float(input("Enter Value of side2:"))
c = float(input("Enter Value of side3:"))

if (a == b == c):
    print("Triangle is Equilateral")
elif (a == b != c):
    print("Triangle is Isosceles")
elif (a != b == c):
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")
