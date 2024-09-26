
"""
Determine whether the user has provided a first name and a last name. 
If both are provided, display the full name; if only one is given, 
display either the first or last name. If neither is provided, prompt that no name was given.
greeting = "Hello"
name = "Alice"
time_of_day = "morning"

message = greeting + ", " + name + "! Good afternoon!"
"""
greeting = "Hello"
name = "Alice"
time_of_day = "night"

if time_of_day == "morning":
    print(greeting + ", " + name + "! Good morning!")
elif time_of_day == "afternoon":
    print(greeting + ", " + name + "! Good afternoon!")
else : print(greeting + ", " + name + "!")