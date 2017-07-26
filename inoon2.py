import turtle

x = 0
while x<300:
    Y = x**2/300 #x**2 is the same as x*x
    turtle.goto(x, Y)
    x = x + 100
    print(x)
    
turtle.mainloop()
