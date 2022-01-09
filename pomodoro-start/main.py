from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 4
reps = 0
Timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def start_button_clicked():
    start_timer()


def reset_button_clicked():
    reset_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, is_reset
    reps += 1
    start_button.config(state='disabled')

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # if its 8th rep, then take long break
        status_label.config(text='Break', foreground=RED)
        window.attributes('-topmost', 1)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # if its 2nd/4th/6th rep, then take short break of 5 minutes
        status_label.config(text='Break', foreground=PINK)
        window.attributes('-topmost', 1)
        count_down(short_break_sec)
    else:
        # if its 1st/3rd/5th/7th rep, then work for 25 minutes
        status_label.config(text='Work', foreground=GREEN)
        window.attributes('-topmost', 0)
        count_down(work_sec)


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(Timer)
    canvas.itemconfig(canvas_text, text='00:00')
    status_label.config(text='Status', foreground=GREEN)
    checkmark.config(text='')
    start_button.config(state='active')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(initial_value):
    minute = math.floor(initial_value / 60)
    seconds = initial_value % 60
    if minute < 10:
        minute = f'0{minute}'
    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(canvas_text, text='{0}:{1}'.format(minute, seconds))
    if initial_value > 0:
        global Timer
        Timer = window.after(1000, count_down, initial_value - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks = ''
            work_session = math.floor(reps / 2)
            for _ in range(work_session):
                checks += '✔️️'
            checkmark.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


# Label
status_label = Label(text='Status', foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
status_label.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
canvas_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# button
start_button = Button(text='Start', bg=YELLOW, highlightthickness=0, command=start_button_clicked)
start_button.grid(row=2, column=0)

# reset button
reset_button = Button(text='Reset', bg=YELLOW, highlightthickness=0, command=reset_button_clicked)
reset_button.grid(row=2, column=2)

# checkmark
checkmark = Label(foreground=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()
