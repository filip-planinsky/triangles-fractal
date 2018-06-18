from __future__ import print_function
import turtle
import time
import math

# wrapper methods - so we can produce a log with all commands.
# this we know and can debug how we came up with the drawing.
# enable the prints if you want to debug and see the full turtle path :)
def backward(x):
    #print("backward (%f)" % x)
    happy_turtle.backward(x)

def forward(x):
    #print("forward (%f)" % x)
    happy_turtle.forward(x)

def left(x):
    #print("left (%f)" % x)
    happy_turtle.left(x)

def right(x):
    #print("right (%f)" % x)
    happy_turtle.right(x)

def penup():
    #print("penup")
    happy_turtle.penup()

def pendown():
    #print("pendown")
    happy_turtle.pendown()

def color(x):
    #print("color (%s)" % x)
    happy_turtle.color(x)



def draw_triangle(size):
    pendown()
    new_size = abs(calculate_new_size(size, alpha))
    right(90 - beta)
    forward(new_size)
    new_size = abs(calculate_new_size(size, beta))
    right(180 - gamma)
    forward(new_size)
    right(180 - alpha)
    forward(size)
    penup()

def draw_sqare(size):
    pendown()
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    penup()

def reset_turtle_for_right_side_drawing(size):
    backward(size)
    right(90)
    forward(size)
    right(90-gamma)

def reset_turtle_for_left_side_drawing(new_size, size):
    backward(new_size)
    left(90)
    backward(new_size)
    right(180-alpha)

    backward(size)
    left(90)

def calculate_new_size(size, angle):
    side = (size / math.sin(math.radians(gamma))) * math.sin(math.radians(angle))
    return side

def recursion(size, level, direction):
    print(">>>>> Direction %s, level: %i, size: %f" % (direction, level, size))

    # some fun with colors. every level will have its own color.
    color(level_colors[(level-1) % 6])

    # when drawing the left side - set the inclination degree first.
    if (direction == 'L'):
        left(beta)

    draw_sqare(size)

    # position the turtle for the next level
    right(90)
    forward(size)

    # if the level we just drew is the last one, exit the recursive call
    if level == max_level:
        return

    # calculate the size of the left side square for the next level and recurse
    new_size = abs(calculate_new_size(size, alpha))
    recursion(new_size, level + 1, 'L')
    print("<<<<< Exit. Direction %s, level: %i, size: %f, prev size: %f"
          % ('L', level+1, new_size, size))

    # position turtle for right side drawing
    reset_turtle_for_right_side_drawing(new_size)

    # calculate the size of the right side square for the next level and recurse
    new_size = abs(calculate_new_size(size, beta))
    recursion(new_size, level + 1, 'R')
    print("<<<<< Exit. Direction %s, level: %i, size: %f, prev size: %f"
          % ('R', level+1, new_size, size))

    # reset position of turtle for left side square drawing
    reset_turtle_for_left_side_drawing(new_size, size)

    # option, if you'd like to have the triangles in one solid color.
    # personally, I like the colorful sides more.
    if (draw_trinangle_enabled == True):
        color("black")
        draw_triangle(size)
        # set the turtle in initial position, after the triangle draw
        right(90)



# ------ main -------

# it's our turtle - it's alive :)
happy_turtle = turtle.Turtle()


# ----- Global variables for settings -------
# beta = 34
# alpha = 70
# gamma = 76
# size = 90

beta = 32
alpha = 73
gamma = 75
size = 87

# speed = 1 -> slowest - bigger animation delay for the turtle
# speed = 10 -> fastest - smaller animation delay for the turtle
# speed = 0 -> max speed - no animation delay for the turtle
speed = 10

# up to which level we like to draw
max_level = 5

# do we need solid color triangles as well?
draw_trinangle_enabled = False

# just fun with colors.
level_colors = ["red", "green", "blue", "cyan", "pink", "brown"]

happy_turtle.speed(speed)
penup()

# check at least that our input is somewhat valid
if (alpha + beta + gamma != 180 or size < 0):
    print("Sum off all angles must be 180 degrees and size must be bigger than zero!")
    exit(1)


# init turtle position, where we like it to be for start of recursion.
# this is optiona - it just makes the final drawing "look" the proper side up
left(90)
backward(size)
right(beta)

start_time = time.time()

recursion(size, 1, 'L')

elapsed_time = time.time() - start_time

# just for fun put the turtle where all started.
backward(size)

if elapsed_time > 60:
    print ("Drawing took %d:%d minutes"
           % (elapsed_time / 60, elapsed_time % 60))
else:
    print ("Drawing took %f seconds." % (elapsed_time))

# keep the turtle window open, until someone hits enter.
raw_input("Hit enter for end")


