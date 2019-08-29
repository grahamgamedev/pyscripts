import turtle, random, time

def probe(x, y, level):
    if level < 5:
        fred = turtle.Turtle()
        fred.penup()
        fred.setpos(x, y)
        
        color = (random.randint(0, 9) /10, random.randint(0, 9) /10, random.randint(0, 9) /10)
        fred.pencolor(color)
        fred.pendown()


            
        fred.left(random.randint(0, 270))
        fred.forward(random.randint(50, 200))
        x = fred.pos()[0]
        y = fred.pos()[1]
        level += 1

        for i in range(3):
            probe(x, y, level)

           
probe(0, 0, 0)
