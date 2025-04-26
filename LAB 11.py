while True:
    try:
        number = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

print("You entered: ",number)
