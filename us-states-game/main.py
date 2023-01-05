import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
text = turtle.Turtle()
text.pu()
text.hideturtle()
screen.setup(width=850, height=480)
turtle.shape(image)
states_picked = []

game_is_on = True
data = pandas.read_csv("50_states.csv")
states = data['state'].to_list()
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
while game_is_on:
    answer_state = answer_state.title()
    if answer_state == "Exit":
        states = [states.remove(state) for state in states_picked]
        states_csv = pandas.DataFrame(states)
        states_csv.to_csv("Your dumb ass forgot these")
        break
    for state in states:
        if answer_state == state and answer_state not in states_picked:
            states_picked.append(answer_state)
            state_data = data[data.state == state]
            text.goto(int(state_data.x), int(state_data.y))
            text.write(answer_state)
    answer_state = screen.textinput(title=f"{len(states_picked)}/50 States Correct",
                                    prompt="What's another state's name?")



