import tkinter
from enum import Enum

#
#   Label   _   Button  _
#   _     Button   _    _
#   _       _      _    Entry
#


class Color(Enum):
    RED = 1
    GREE = 2
    BLUE = 3


window = tkinter.Tk()
# Write code in between
window.title('First GUI Program')
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="I'm a label", font=('Aerial', 24, 'bold'))
# my_label.pack()
my_label.grid(row=0, column=0)

my_button1 = tkinter.Button(text='Click Me!')
# my_button.pack()
my_button1.grid(row=0, column=2)

# def generate(color: Color.GREE):
#     pass
#
#
# generate(Color.BLUE)


def button_clicked():
    my_label.config(text=entry.get())


my_button2 = tkinter.Button(text='Click Me!', command=button_clicked)
# my_button.pack()
my_button2.grid(row=1, column=1)

entry = tkinter.Entry(width=20)
# entry.pack()
entry.grid(row=2, column=3)

window.mainloop()
