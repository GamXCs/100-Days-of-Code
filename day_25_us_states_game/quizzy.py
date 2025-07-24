import turtle
import pandas as pd

# Read the state data
data = pd.read_csv("50_states.csv")

# Set up the turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)  # Set the map image as the background

# converts the states from the csv into a list in order to compare
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    # Prints a textbox with a header and prompts user for a guess
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_location = data[data.state == answer_state]
        # Using .item() gets the value to handle the error since we had an int/float
        t.goto(state_location.x.item(), state_location.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)
