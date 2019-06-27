# Asks the user to enter the name and stores it inside the name variable
name = input("Please enter your name: ")
# Asks the user to enter there name and converts it into a interger and stores it inside the vairbale age
age = int(input("Please enter your age: "))
# Created a variable year with the current year
year = 2019
# Created hundred_years_old variable to store (100 - age) + year
hundred_years_old = (100 - age) + year
# Created a message variable to store string interopolation that syas the users name and prints a string "you will turn 100 in year" and than the variable hundred_years_old.
user_message = (f"Hello {name} you will turn 100 in year {hundred_years_old}!")

# Prints out the variable message to the user in the terminal
print(user_message)
