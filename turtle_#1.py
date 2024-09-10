from turtle import Turtle
import random
import math as m

class RandomSquare:

    def __init__(self, width, depth, length):
        self.width = width
        self.depth = depth
        self.length= length

        self.t = Turtle()
        self.t.pensize(2)
        self.t.screen.colormode(255)
        self.t.speed(10)

        for line in range(self.depth):
            for square in range(self.width):
                self.centre_square(line, square, 5.0)
                self.randomiser(line, self.depth)
                self.square_orentate()
                #self.fill_colour()
                self.white2black()
                self.square()

        self.t.screen.exitonclick()

    def centre_square(self, line, count,  margin):
        x_min = ((self.length * (self.width - 1)) + (margin * (self.width - 1))) / -2.0
        x_pos = x_min + (count * (self.length + margin))

        y_max = ((self.length * (self.depth - 1)) + (margin * (self.depth - 1))) / 2.0
        y_pos = y_max - (line * (self.length + margin))

        self.t.penup()
        self.t.setpos(x_pos, y_pos)

    def square_orentate(self):
        self.t.fd(self.length/2.0)
        self.t.right(90)
        self.t.fd(self.length/2.0)
        self.t.left(180)

    def fill_colour(self):
        if self.random_angle == 0:
            self.R = 255
            self.G = 255
            self.B = 255
        else:
            RGB = 255 - (abs(self.random_angle) * 3)

            if RGB < 0:
                RGB = 0

            if self.random_angle > 0:
                self.R = 255
                self.G = RGB
                self.B = RGB
            elif self.random_angle < 0 :
                self.R = RGB
                self.G = RGB
                self.B = 255

    def white2black(self):
        RGB = int(255 - (abs(self.random_angle) * 3))
        self.R = RGB
        self.G = RGB
        self.B = RGB


    def square(self):
        print(self.R, self.G, self.B)
        self.t.fillcolor((self.R, self.G, self.B))
        self.t.begin_fill()

        self.t.pendown()
        for side in range(4):
            self.t.fd(self.length)
            self.t.left(90)
        self.t.penup()
        self.t.end_fill()

    def randomiser(self, line, line_max):
        if line == 0:
            self.random_angle = 0
        else:
            scale = m.sqrt(45) / (line_max - 1)
            r_min = int(((line - 1) * scale)**2)
            r_max = int((line * scale)**2)
            random_angle = random.randint(r_min, r_max)
            twist = 0
            while twist == 0:
                twist = random.randint(-1, 1)
            self.random_angle = random_angle * twist
            #print(scale, r_min, r_max, random_angle)
            self.t.setheading(0)
            self.t.right(self.random_angle)


RandomSquare(30, 60, 10)



