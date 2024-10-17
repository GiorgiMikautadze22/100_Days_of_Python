from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.score_count = 0
        self.score = Turtle()
        self.show_score()


    def show_score(self):
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(-350, 220)
        self.score.write(f'Score: {self.score_count}', align='center', font=("Arial", 15, "normal"))


    def increase_score(self):
        self.score_count += 1
        self.score.clear()
        self.score.write(f'Score: {self.score_count}', align='center', font=("Arial", 15, "normal"))

    def game_over(self):
        game_over = Turtle()
        game_over.hideturtle()
        game_over.write('Game Over', align='center', font=("Arial", 45, "normal"))

