"""
Check if the user has provided both a first name and a last name. 
If both are provided, display the full name. If only one is provided, 
display either the first name or last name accordingly. If neither is provided, 
display a message indicating that no name was given.
first_name = "John"
last_name = "Doe"
"""
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

if first_name and last_name:
    print("Full name is: " + first_name + " " + last_name)
elif first_name :
    print("First name is: " + first_name)
elif last_name :
    print("Last name is: " + last_name)
else: print("No name provided.")

"""
In Python, you can directly use the variable name to check if it has a value.
Python treats None, an empty string (""), 0, and False as “falsy” (evaluates to False), 
while any non-empty value is considered “truthy” (evaluates to True). 
Therefore, there’s no need to explicitly check if the variable equals None or True. 
Simply checking the variable is enough to determine if it has a value.
"""