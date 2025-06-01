import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_num = float(input("What is the first number?: "))

while True:
    print("+\n" + "-\n" + "*\n" + "\\")
    operation = input("Pick an operation: ")
    second_num = float(input("What is the second number?: "))

    answer = float(calc_dict[operation](first_num, second_num))
    print(f"{first_num} {operation} {second_num} = {answer}")

    rerun = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ").lower()

    if rerun == "y":
        first_num = answer
    elif rerun == 'n':
        first_num = float(input("What is the first number?: "))
    else:
        print("Goodbye!")
        break


