from turtle import Turtle
import random
import math as m

class CircleSquare:

    def __init__(self, length, radius, degree):
        self.length = length
        self.radius = radius

        self.t = Turtle()
        self.t.pensize(1)
        self.t.screen.colormode(255)
        self.t.speed(100)

        for i in range(10, radius, 5):
            for point in range(0, 360, degree):
                if random.randint(0, 10) == 1:
                    self.centre_turtle(point, i)
                    self.square_orientate()
                    self.square()

        self.t.screen.exitonclick()

    def centre_turtle(self, point, i):
        x = m.cos(m.radians(point)) * i
        y = m.sin(m.radians(point)) * i
        self.t.penup()
        self.t.setpos(x, y)
        self.t.setheading(point)

    def square_orientate(self):
        self.t.fd(self.length/2.0)
        self.t.right(90)
        self.t.fd(self.length/2.0)
        self.t.left(180)

     def square(self):

        self.t.fillcolor((0, 0, 0))
        self.t.begin_fill()

        self.t.pendown()
        for side in range(4):
            self.t.fd(self.length)
            self.t.left(90)
        self.t.penup()
        self.t.end_fill()

CircleSquare(5, 400, 1)


