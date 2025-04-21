# Match
# Switch

numbers = int(input("Enter Number 1-6\n"))
match numbers:
    case 1:
        print("you have entered 1")
    case 2:
        print("you have entered 2")
    case 3:
        print("you have entered 3")
    case 4:
        print("you have entered 4")
    case 5:
        print("you have entered 5")
    case 6:
        print("you have entered 6")
    case _:
        print("AAP KON")
