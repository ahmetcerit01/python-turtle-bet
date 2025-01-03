from turtle import Turtle, Screen
import random

# Ekranı ayarla
screen = Screen()
screen.setup(width=500, height=400)
screen.bgpic("bg3.gif")  # Arka plan görseli

# Kullanıcıdan tahmin al
user_bet = screen.textinput(title="What is your guess:", prompt="Which turtle will win the race?")

# Kaplumbağaları oluştur
turtle_colors = ["green", "yellow", "blue", "pink", "purple"]
location = -150
all_turtles = []

for i in range(0, 5):
    tim = Turtle()
    tim.color(turtle_colors[i])
    tim.shape("turtle")
    tim.penup()
    tim.goto(x=-240, y=location)
    location += 50
    all_turtles.append(tim)

# Yarışı başlat
is_race_on = True

while is_race_on:
    for i in all_turtles:
        speed = random.randint(0, 10)
        i.forward(speed)
        if i.xcor() == 230:  # Kaplumbağa bitiş çizgisine ulaştığında
            winning_color = i.pencolor()
            is_race_on = False
            # Kazanan rengi ekranda göster
            winner = Turtle()
            winner.hideturtle()
            winner.penup()
            winner.goto(0, 0)
            winner.write(f"The winner is {winning_color}!", align="center", font=("Poppins", 24, "bold"))
            if winning_color == user_bet:
                print(f"You guessed right! The winner is {winning_color}.")
            else:
                print(f"You guessed wrong! The winner is {winning_color}.")

# Çıkmak için bir olaya bağlan
def exit_fullscreen():
    screen.bye()  # Çıkış için ekranı kapat

screen.listen()
screen.onkey(exit_fullscreen, "Escape")  # Escape tuşuyla çıkış

# Ekranı açık tut
screen.mainloop()
