# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def multi_inputs(age, time):
    print(f"You are {age} years old ")
    print(f"You were born at {time}!")
multi_inputs("13", "12:45")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with(name="Gam", location="Birmingham")