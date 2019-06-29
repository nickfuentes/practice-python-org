"""user_input = int(input("Enter a number: "))

if user_input % 2 == 0:
    print("Your number is EVEN!")
else:
    print("You number is ODD!")"""


"""def odd_even():
    num_check = int(input("Enter a number to check: "))
    if num_check % 4 == 0:
        print("Your number is a Mutilple of 4 and EVEN!")
    elif num_check % 2 == 0:
        print("Your number is EVEN!")
    else:
        print("Your number is ODD!")


odd_even()"""


def num_divide():
    num_check = int(input("Enter a number to check: "))
    num_divide = int(input("Enter a number to divide: "))
    if num_check % 4 == 0:
        print("Your number is a Mutilple of 4 and divides evenly!")
    elif num_check % num_divide == 0:
        print("Your number diveds evenly!")
    else:
        print("Your number does not divide evenly!")


num_divide()
