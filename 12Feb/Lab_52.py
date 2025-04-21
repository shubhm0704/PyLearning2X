browser = input("Enter Browser Name\n")

match browser:
    case "Chrome":
        print("Chrome code executed!")
    case "FireFox":
        print("FF code executed!")
    case _:
        print("Go Yaha se!")