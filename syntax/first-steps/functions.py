import math

degrees = 45
radians = degrees / 180.0 * math.pi
height = math.sin(radians)
print(height)
x = math.sin(degrees / 360.0 * 2 * math.pi)
print(x)


def say_hello(name):
    print(f"Hello, {name}")


say_hello('Unknown Hero')
