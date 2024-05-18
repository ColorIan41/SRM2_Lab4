import numpy as np


def func(x):
    return np.sqrt(x ** 2 - 64)


func_value = 22.868


def rectint(f, a, b, rectangles):
    cumulative_area = 0

    a = float(a)
    b = float(b)
    rectangles = float(rectangles)

    i = (b - a) / rectangles

    trailing_x = a
    leading_x = a + i

    while (a <= leading_x <= b) or (a >= leading_x >= b):
        area = f((trailing_x + leading_x) / 2) * i
        cumulative_area += area

        leading_x += i
        trailing_x += i

    return cumulative_area


def trapint(f, a, b, trapezoids):
    cumulative_area = 0

    a = float(a)
    b = float(b)
    trapezoids = float(trapezoids)

    i = (b - a) / trapezoids

    trailing_x = a
    leading_x = a + i

    while (a <= leading_x <= b) or (a >= leading_x >= b):
        area = (f(trailing_x) + f(leading_x)) * i / 2
        cumulative_area += area

        leading_x += i
        trailing_x += i

    return cumulative_area


def simpson(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])


def runge(h1, h2, p):
    error = abs(func_value-(h2 - ((h2 - h1) / (2 ** p - 1))))
    return error


print("\nКрок = 0.5:")
print(rectint(func, 8, 12, 8))
print(trapint(func, 8, 12, 8))
print(simpson(func, 8, 12, 8))

print("\nКрок = 0.25:")
print(rectint(func, 8, 12, 16))
print(trapint(func, 8, 12, 16))
print(simpson(func, 8, 12, 16))

print("\nРезультати процедури Рунге:")
print(runge(rectint(func, 8, 12, 8), rectint(func, 8, 12, 16), 1))
print(runge(trapint(func, 8, 12, 8), trapint(func, 8, 12, 16), 2))
print(runge(simpson(func, 8, 12, 8), simpson(func, 8, 12, 16), 2))
