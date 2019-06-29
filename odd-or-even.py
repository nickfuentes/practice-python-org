"""user_input = int(input("Enter a number: "))

if user_input % 2 == 0:
    print("Your number is EVEN!")
else:
    print("You number is ODD!")"""


def odd_even():
    user_input = int(input("Enter a number: "))
    if user_input % 4 == 0:
        print("Your number is a Mutilple of 4 and EVEN!")
    elif user_input % 2 == 0:
        print("Your number is EVEN!")
    else:
        print("Your number is ODD!")


odd_even()
