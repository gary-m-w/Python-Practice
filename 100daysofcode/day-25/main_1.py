import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name?").title()
    # print(answer_state)

    states = pandas.read_csv("50_states.csv")
    answers = states.state.to_list()
    guessed_states = []

    if answer_state == 'Exit':
        # missing_states = []
        missing_states = [state for state in answers if state not in guessed_states]
        # for i in answers:
        #     if i not in guessed_states:
        #         missing_states.append(i)
        print(missing_states)
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("missing_states")
        break
    if answer_state in answers:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_coords = states[states.state == answer_state]
        t.goto(x=int(state_coords.x),y=int(state_coords.y))
        t.write(answer_state)

        # print(answer_state)
        score += 1
        # print(f"{score}/50")
    # else:
        # print(f"Try again. {score}/50")
        # print(answer_state)

screen.exitonclick()
# states_dict = {
#         "Alabama": [], "Alaska": [], "Arizona": []
#     }

# def get_mouse_click_coor(x, y):
#     print(x, y)


# for i in states_dict:
#     print(f"Click {i}")
#     states_dict[i] = turtle.onscreenclick(get_mouse_click_coor)
#     turtle.mainloop()
# print(states_dict)