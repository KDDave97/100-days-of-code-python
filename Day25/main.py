import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.bgpic(image)
turtle.speed("fastest")
turtle.penup()
turtle.ht()

states_data = pandas.read_csv("50_states.csv")
data = states_data.to_dict()
guessed_list = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(f"{len(guessed_list)} / {len(states_data)} ", "Whats another state's name?")
    for states in data["state"]:
        if data["state"][states].lower() == answer_state.lower():
            state_name = (data["state"][states])
            state_x = (data["x"][states])
            state_y = (data["y"][states])
            turtle.goto(state_x, state_y)
            turtle.write(state_name)
            if state_name not in guessed_list:
                guessed_list.append(state_name)
    if len(guessed_list) == 50:
        game_is_on = False

screen.exitonclick()