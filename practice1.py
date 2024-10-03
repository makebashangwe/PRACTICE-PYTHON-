password = input("Please enter a password:")
if len(password) < 8:
    print("Password must be at least 8 characters")

criteria_1 = False # upper
criteria_2 = False # lower case
criteria_3 = False # numbers
criteria_4 = False #  symbols

special_char = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

if criteria_1 and criteria_2 and criteria_3 and criteria_4:
    print("Password Strength: Strong! ")
elif criteria_1 and criteria_2 and criteria_3:
    print("Password Strength: Medium! ")
else:
    print("Password Strength: Weak! ")


if any(char.isupper() for char in password):
    criteria_1 = True
else:
    print("Missing Criteria: must contain be at least one uppercase character. ")

if any(char.islower() for char in password):
    criteria_2 = True
else:
    print("Missing Criteria: must contain be at least one lowercase character. ")

if any(char.isdigit() for char in password):
    criteria_3 = True
else:
    print("Missing Criteria: must contain be at least one number.")

if any(char in special_char for char in password):
    criteria_4 = True
else:
    print("Missing Criteria: must contain at least one special character.")

