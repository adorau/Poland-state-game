import turtle
import pandas

screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()
screen.setup(900,700)
screen.bgpic("mapa_polski.gif")
data = pandas.read_csv("Lista_woj.csv", sep=";")
data_state = data.wojewodztwo.to_list()
points = 0
guessed = []
not_guessed = []


while len(guessed) < 16:
    answer = screen.textinput(f"{points}/16 Write 'exit' to escape.", "Next state:").lower()
    if answer in data_state and answer not in guessed:
        data_row = data[data.wojewodztwo == answer]
        x_state = int(data_row.x)
        y_state = int(data_row.y)
        turtle.goto(x_state,y_state)
        turtle.write(f"{answer}")
        points += 1
        guessed.append(answer)
    elif answer == "exit":
        for state in data_state:
            if state not in guessed:
                not_guessed.append(state)
        file ={
            "wojewodztwo": not_guessed
        }
        pandas.DataFrame(file).to_csv("not_guessed_states.csv")
        print(f"You've not guessed {len(not_guessed)}: {not_guessed}")
        break
