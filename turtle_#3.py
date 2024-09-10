from turtle import Turtle
import random
import math as m

class TriangleCircle:

    def __init__(self, diameter, width, depth):
        self.diameter = diameter
        self.width = width
        self.depth = depth
        self.coord_list = []

        self.t = Turtle()
        self.t.pensize(1)
        self.t.screen.colormode(255)
        self.t.speed(100)

        for line in range(self.depth):
            for circle in range(self.width):
                self.CentreOffset(line, circle, 15)
                self.AddTriangle()
                self.draw()

        self.t.screen.exitonclick()

    def AddTriangle(self):
        for i in range(3):
            alpha = random.randint(0, 360)
            x = m.cos(m.radians(alpha)) * (self.diameter * 0.5)
            y = m.sin(m.radians(alpha)) * (self.diameter * 0.5)
            self.coord_list.append([x, y])

        self.coord_list.append(self.coord_list[-3])

    def CentreOffset(self, line, count, margin):
        x_min = ((self.diameter * (self.width - 1)) + (margin * (self.width - 1))) / -2.0
        self.x_pos = x_min + (count * (self.diameter + margin))

        y_max = ((self.diameter * (self.depth - 1)) + (margin * (self.depth - 1))) / 2.0
        self.y_pos = y_max - (line * (self.diameter + margin))

    def draw(self):
        self.t.penup()
        count = 0
        for i in self.coord_list:
            if count == 0:
                self.t.goto(i[0] + self.x_pos, i[1] + self.y_pos)
                self.t.pendown()
                count += 1

            if count == 4:
                self.t.goto(i[0] + self.x_pos, i[1] + self.y_pos)
                self.t.penup()
                count = 0

            else:
                self.t.goto(i[0] + self.x_pos, i[1] + self.y_pos)
                count += 1

TriangleCircle(80, 6, 10)
#TriangleCircle(200, 4, 1)
