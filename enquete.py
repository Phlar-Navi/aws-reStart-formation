print("Welcome to the survey! Please answer the following questions:")

firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
# age = input("What is your age? ")
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

print("\nThank you for participating in the survey!")

# print("Hello {} {}, you like a {} {}!".format(firstName, lastName, color, animal))

print(f"Hello {firstName} {lastName}, you like a {color} {animal} !")