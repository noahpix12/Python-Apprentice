# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here ) to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 
import turtle

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

# Set up the screen                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

t = turtle.Turtle()                  # Create a turtle named tina
t.penup()
screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji.png") # Set the background image of the screen
def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

set_turtle_image(t, "moustache1.gif")
def turtle_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle

    This function will make the turtle tilt 20 degrees 18 times, making a full
    circle. It is called by the turtle when the user clicks on it.

    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """

    print('turtle clicked!')
    
    t.goto(x,y)

# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))
   
turtle.done()      
