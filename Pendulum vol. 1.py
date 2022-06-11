from tkinter import *
import math
import time

root = Tk()
mx = 1000
my = 1000
c = Canvas(root, width=mx, height=my)
c.pack()

# l = int(input())
# alpha = int(input())  # угол на который отводят маятник

ball = c.create_oval(0, 0, 0, 0, fill="red", width=0)

l = 400
alpha = 40
g = 10
v = 0
pi = math.pi
fi0 = 0

alpha_rad = (alpha * pi) / 180

A = l * math.sin(alpha_rad)

T = 2 * pi * (l / g) ** 0.5

w = (2 * pi) / T

background = c.create_rectangle(0, 0, mx, my, width=0, fill="grey95")

for i in range(110, mx - 110, 20):
    footing_dash = c.create_line(i, 100, i + 20, 80, width=3, fill="grey80")

slice_ = c.create_line(100, 80, (mx - 100), 80, width=3, fill="grey95")

footing = c.create_line(100, 100, (mx - 100), 100, width=3)

line = c.create_line((mx // 2), 100, (mx // 2), 100 + l, width=3)

xn = (mx // 2) - A * math.cos(0 + fi0)
yn = l * math.cos(alpha_rad)

xn = int(xn)
yn = int(yn)

c.create_line(100, l + 200, mx - 100, l + 200, width=3)
c.create_line((mx // 2), l + 200, (mx // 2), my, width=3)

c.create_line((mx // 2), 100, (mx // 2), 100 + l, width=3, fill="grey90", dash=(100, 10))
c.create_oval((mx // 2) - 30, 100 - 30 + l, (mx // 2) + 30, 100 + 30 + l, fill="grey95", width=3, outline="grey90", dash=(100, 10))

c.create_line((mx // 2), 100, (mx // 2) + A, 100 + ((l ** 2) - (A ** 2)) ** 0.5, width=3, fill="grey90", dash=(100, 10))
c.create_oval((mx // 2) + A - 30, 100 + ((l ** 2) - (A ** 2)) ** 0.5 - 30, (mx // 2) + A + 30, 100 + ((l ** 2) - (A ** 2)) ** 0.5 + 30, fill="grey95", width=3, outline="grey90", dash=(100, 10))

u = 1

for t in range(0, 1000):

    xk = A * math.cos(w * t + fi0)
    yk = ((l ** 2) - (xk ** 2)) ** 0.5

    print(xk)
    print(yk)

    c.delete(ball)
    c.delete(line)

    c.create_oval((mx // 2) + xk - 1, 100 + yk - 1, (mx // 2) + xk + 1, 100 + yk + 1, fill="grey93", width=0)

    line = c.create_line((mx // 2), 100, (mx // 2) + xk, 100 + yk, width=3)
    ball = c.create_oval((mx // 2) + xk - 30, 100 + yk - 30, (mx // 2) + xk + 30, 100 + yk + 30, fill="black", width=3)

    c.update()
    time.sleep(0.07)




    gr = c.create_oval((mx // 2) + xk - 1, l + 200 + u, (mx // 2) + xk + 1, l + 200 + u, fill="red", width=0)

    u += 1
    xn = xk
    yn = yk




# for t in range(0, 100):

root.mainloop()