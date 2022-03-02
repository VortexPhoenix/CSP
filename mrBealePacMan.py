import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.screensize(500,300,"black")
wn.bgpic("52a33c10ae0c117156dd2807a4f324da.png")
wn.title("PacMan")

#initialize turtle
bealepic = "pacBeale.gif"
wn.addshape(bealepic)
mazedrawer = trtl.Turtle()
mazerunner = trtl.Turtle(shape=bealepic)

#Ghost Turtles

clyde = trtl.Turtle(shape="turtle")
clyde.penup()
clyde.color("orange")
clyde.goto(-90,20)

inky = trtl.Turtle(shape="turtle")
inky.penup()
inky.color("blue")
inky.goto(-30,20)

pinky = trtl.Turtle(shape="turtle")
pinky.penup()
pinky.color("pink")
pinky.goto(30,20)

blinky = trtl.Turtle(shape="turtle")
blinky.penup()
blinky.color("red")
blinky.goto(85,20)



mazerunner.penup()
mazerunner.goto(0,-43)
mazerunner.color("yellow")


#Variables
angle = 90
path_width = 20
wall_length = path_width
# colors = ["blue","red","orange","pink","green","purple","black","brown","goldenrod","sienna","fuchsia"]
wall_thickness = 4
num_walls = 25
mze_wll_clr = "red"


def draw_door(pos):
    #draw door
    mazedrawer.forward(pos)
    mazedrawer.penup()
    mazedrawer.forward(path_width*2)
    mazedrawer.pendown()

def draw_barrier(pos):
    #draw barrier
    mazedrawer.forward(pos)
    mazedrawer.left(angle)
    mazedrawer.forward(path_width*2)
    mazedrawer.backward(path_width*2)
    mazedrawer.right(angle)

def go_up():
    mazerunner.setheading(90)
def go_down():
    mazerunner.setheading(270)
def go_left():
    mazerunner.setheading(180)
def go_right():
    mazerunner.setheading(0)            

def go_turtle():
    mazerunner.forward(1)

    wn_canvas = wn.getcanvas()
    x,y = mazerunner.position()
    margin = 5
    items = wn_canvas.find_overlapping(x+margin, -y+margin, x - margin, -y - margin)

    if (len(items) > 0):
        canvas_color = wn_canvas.itemcget(items[0], 'fill')
        if canvas_color == mze_wll_clr:
            mazerunner.color('gray')
            wn.onkeypress(None, 'space')
            return
    wn.ontimer(go_turtle, 15)


#Setup for maze
mazedrawer.pensize(wall_thickness)
mazedrawer.color(mze_wll_clr)
mazedrawer.speed("fastest")

#Drawing the maze

# ghost box trace
mazedrawer.color(mze_wll_clr)
mazedrawer.penup()
mazedrawer.setheading(180)
mazedrawer.goto(-55,60)
mazedrawer.pendown()
mazedrawer.forward(60)
mazedrawer.left(90)
mazedrawer.forward(80)
mazedrawer.left(90)
mazedrawer.forward(235)
mazedrawer.left(90)
mazedrawer.forward(80)
mazedrawer.left(90)
mazedrawer.forward(60)

# Outer top maze trace
mazedrawer.penup()
mazedrawer.setheading(180)
mazedrawer.goto(495,50)
mazedrawer.pendown()
mazedrawer.forward(180)
mazedrawer.right(90)
mazedrawer.forward(70)
mazedrawer.right(90)
mazedrawer.forward(175)
mazedrawer.left(90)
mazedrawer.forward(205)
mazedrawer.left(90)
mazedrawer.forward(975)
mazedrawer.left(90)
mazedrawer.forward(205)
mazedrawer.left(90)
mazedrawer.forward(175)
mazedrawer.right(90)
mazedrawer.forward(70)
mazedrawer.right(90)
mazedrawer.forward(180)
mazedrawer.penup()
mazedrawer.setheading(-90)
mazedrawer.goto(0,325)
mazedrawer.pendown()
mazedrawer.forward(80)

# Outer bottom maze trace
mazedrawer.penup()
mazedrawer.setheading(180)
mazedrawer.goto(495,-10)
mazedrawer.pendown()
mazedrawer.forward(-180)
mazedrawer.right(-90)
mazedrawer.forward(-70)
mazedrawer.right(-90)
mazedrawer.forward(-175)
mazedrawer.left(-90)
mazedrawer.forward(-205)
mazedrawer.left(-90)
mazedrawer.forward(-975)
mazedrawer.left(-90)
mazedrawer.forward(-205)
mazedrawer.left(-90)
mazedrawer.forward(-175)
mazedrawer.right(-90)
mazedrawer.forward(-70)
mazedrawer.right(-90)
mazedrawer.forward(-180)


# for side in range(num_walls):
#     wall_length += path_width
#     mazedrawer.color(mze_wll_clr)
    
    # if side > 4:
    #     mazedrawer.left(angle)

    #     #randomize location of doors and barriers
    #     door = rand.randint(path_width*2, (wall_length - path_width*2))
    #     barrier = rand.randint(path_width*2, (wall_length - path_width*2))
    #     while abs(door - barrier) < path_width:
    #         door = rand.randint(path_width*2, (wall_length - path_width*2))
        

    #     if (door < barrier):
    #         draw_door(door)
    #         draw_barrier(barrier - door - path_width*2)
    #         #draw rest of wall  
    #         mazedrawer.forward(wall_length - barrier)
    #     else:
    #         draw_barrier(barrier)
    #         draw_door(door - barrier)
    #         #draw rest of wall
    #         mazedrawer.forward(wall_length - door - path_width*2)    

# mazedrawer.hideturtle()

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_up, "w")

wn.onkeypress(go_down, "Down")
wn.onkeypress(go_down, "s")

wn.onkeypress(go_left, "Left")
wn.onkeypress(go_left, "a")

wn.onkeypress(go_right, "Right")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_turtle, "space")

wn.listen()
wn.mainloop()