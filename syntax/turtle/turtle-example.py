import turtle
import math
bob = turtle.Turtle()
print(bob)

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)





def arc(t, r, angle):
    """
    Draws an arc with the given parameters.
    :param t:
    :param r:
    :param angle:
    :return:
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    arc(t, r, 360)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

arc(bob, r = 33, angle = 260)


turtle.mainloop()