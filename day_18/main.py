from turtle import Turtle, Screen


#We can also shorthand modules by giving them an alias
#from turtle import t (instead of having to type of Turtle)

tim = Turtle()

tim.color("blue")

def drawShape(numOfSides):
    angle = (360/numOfSides)
    for i in range(numOfSides):
        tim.forward(40)
        tim.right(angle)
for shapeSide in range(3,11):
    drawShape(shapeSide)

# for i in range(3):
#     tim.forward(40)
#     tim.right(120)
# for i in range(4):
#     tim.forward(40)
#     tim.right(90)
# for i in range(5):
#     tim.forward(40)
#     tim.right(72)
# for i in range(6):
#     tim.forward(40)
#     tim.right(60)
# for i in range(7):
#     tim.forward(40)
#     tim.right(51)
# for i in range(8):
#     tim.forward(40)
#     tim.right(45)
# for i in range(9):
#     tim.forward(40)
#     tim.right(40)
# for i in range(10):
#     tim.forward(40)
#     tim.right(36)

















screen = Screen()
screen.exitonclick()