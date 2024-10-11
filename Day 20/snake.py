from turtle import Turtle, Screen

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.initialise_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)




    def initialise_snake(self):
        x_pos = 0
        for num in range(3):
            new_segment = Turtle('square')

            new_segment.color('white')
            new_segment.penup()
            new_segment.setx(x_pos)
            x_pos -= MOVE_DISTANCE
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_seg_x = self.segments[seg_num - 1].xcor()
            new_seg_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_seg_x, new_seg_y)

        self.head.forward(MOVE_DISTANCE)