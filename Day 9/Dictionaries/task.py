programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again."
}

# print(programming_dictionary["Bug"])

programming_dictionary["Add"] = "This adds to the dictionary"
for key in programming_dictionary:
    print(f"{key} : {programming_dictionary[key]}")

#can wipe a dictionary

# empty_dictionary = {}
# programming_dictionary = {}
# print(programming_dictionary)

#Can update dictionary
programming_dictionary["Bug"] = "Proof that we can edit."

print(programming_dictionary)


city_temps = {
    "Cairo": 35,
    "London": 15,
    "New York": 22,
    "Moscow": 5,
    "Sydney": 28
}

city_feels = {}

for key in city_temps:
    if city_temps[key] >= 30:
        city_feels[key] = "Hot"
    elif city_temps[key] > 19:
        city_feels[key] = "Warm"
    elif city_temps[key] > 9:
        city_feels[key] = "Cool"
    else:
        city_feels[key] = "Cold"