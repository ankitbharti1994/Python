import turtle
from StateInput import StateInput

screen = turtle.Screen()
screen.title('U.S States game')
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)


# # self defined function to print coordinate
# def button_click(x, y):
#     print("You clicked at this coordinate({0},{1})".format(x, y))
#
#
# # onscreen function to send coordinate
# turtle.onscreenclick(button_click, 1)
# turtle.listen()  # listen to incoming connections
# turtle.speed(10)  # set the speed
# turtle.done()    # hold the screen
#
# screen.exitonclick()

state_input = StateInput()
state_input.showAlert()
