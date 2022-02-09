# Importe turtle library
import turtle

# create turtle
t = turtle.Turtle()
"""
    Basic commands provided by turtle library
    
    t.forward(100)  # turtle t moves 100 pixels forward,
    t.left(42)  # rotates 42° left,
    t.forward(30)  # moves 30 pixels foward,
    t.right(160)  # rotates 160° right,
    t.backward(104)  # then moves 104 pixels backward
"""


# Exercice 1 : staircase function
# staircase of x stairs entered by the user (between 5 and 10)
# stair height to be defined by the user (between 20 and 50 pixels)
# Function staircase : Turtle builds the staircase
def staircase(nb, height):
    for i in range(0, nb):
        t.forward(height),
        t.right(90)
        t.forward(height),
        t.left(90)


# Exercice 2 : square function
# square of x pixels side
def square(side):
    for i in range(0, 4):
        t.forward(side)
        t.right(90)


# Exercice 3 : squares function
# x squares. Each square is twice the size of the previous one
def squares(nb, side):
    for i in range(0, nb):
        square(side)
        side *= 2


# Redirect the turtle correctly
t.left(90)

# Exercice 1 : staircase
stairs_nb = 0
stair_height = 0

# Asks for number of stairs
while not 5 <= stairs_nb <= 10:
    str_temp = input("Enter the number of stairs for the staircase (between 5 and 10): ")
    try:
        stairs_nb = int(str_temp)
    except ValueError:
        # handles errors due to invalid value
        print("Error : the value entered is not a number")

    if not 5 <= stairs_nb <= 10:
        # Warns the user about the entry is not in the authorized range
        print(f"The value entered: {stairs_nb} is incorrect. You must enter a value between 5 and 10")

# Asks for stair height
while not 20 <= stair_height <= 50:
    str_temp = input("Enter the stair height (between 20 and 50): ")
    try:
        stair_height = int(str_temp)
    except ValueError:
        print("Error : the value entered is not a number")

    if not 20 <= stair_height <= 50:
        print(f"The value entered: {stair_height} is incorrect. You must enter a value between 20 and 50")

staircase(stairs_nb, stair_height)

# Exercice 2 : square
length = 0
# Asks for square side length
while not 20 <= length <= 100:
    str_temp = input("Enter the length for the side of the square (between 20 and 100): ")
    try:
        length = int(str_temp)
    except ValueError:
        print("Error : the value entered is not a number")

    if not 20 <= length <= 100:
        print(f"The value entered: {length} is incorrect. You must enter a value between 20 and 100")

# square(length)

# Exercice 3 : multiple squares
squares_nb = 0
# Asks for square side length
while not 1 <= squares_nb <= 5:
    str_temp = input("Enter the number of squares you want (between 1 and 5): ")
    try:
        squares_nb = int(str_temp)
    except ValueError:
        print("Error : the value entered is not a number")

    if not 1 <= squares_nb <= 5:
        print(f"The value entered: {squares_nb} is incorrect. You must enter a value between 20 and 100")

squares(squares_nb, length)

# keep the GUI open
turtle.done()
