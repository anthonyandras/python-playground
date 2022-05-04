import turtle

def square(t, length):
  for i in range(4):
    t.fd(length)
    t.lt(90)

def polygon(t, length, n):
  for i in range(n):
    t.fd(length)
    t.lt(360/n)

bob = turtle.Turtle()
polygon(bob, 150, 6)
turtle.mainloop()
