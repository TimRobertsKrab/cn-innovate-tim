def input_number():
    num = input("Enter an integer: ")
    try:
        num = int(num)
    except:
        print("You did not enter an integer. Try again")
        input_number()
    else:
        print(f"You entered {num}")

input_number()
