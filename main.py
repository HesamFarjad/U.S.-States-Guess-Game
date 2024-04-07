import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.penup()
t.speed("fastest")
t.hideturtle()
guessed_states_stack = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states_stack) < 50:
    answer_state = screen.textinput(title=f"Guess the State ({len(guessed_states_stack)}/50)", prompt="What's another states name?").title()
    if answer_state == "Exit":
        missing_states_stack = [state for state in all_states if state not in guessed_states_stack]
        new_data = pandas.DataFrame(missing_states_stack)
        new_data.to_csv("missing_states.csv")
        screen.bye()
        break
    if answer_state in all_states:
        guessed_states_stack.append(answer_state)
        related_row_of_answer = data[data.state == f"{answer_state}"]
        x_coordinate = related_row_of_answer['x'].values[0]
        y_coordinate = related_row_of_answer['y'].values[0]
        t.goto(x_coordinate, y_coordinate)
        t.write(f"{answer_state}", font=("Arial", 12, "normal"))

# turtle.mainloop()








