import tkinter.messagebox
from tkinter import *
import pandas
import os.path
import os
from IPython.display import display
import  PasswordGenerator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = PasswordGenerator.generate_password()
    password_textfield.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    filename = 'password_manager.csv'
    website = website_text_field.get()
    username = username_textfield.get()
    password = password_textfield.get()

    if website == '' or username == '' or password == '':
        tkinter.messagebox.showwarning('Warning!', 'Please fill the available fields!')
        return
    else:
        is_ok = tkinter.messagebox.askquestion(website,
                                               'These are the information entered.'
                                               '\nWebsite: {0}\nUsername: {1}\nPassword: {2}.\nis ok to save?'
                                               .format(website, username, password))
        if is_ok == 'yes':
            info = {
                "website": website,
                "user_name": username,
                "password": password
            }

            if os.path.isfile(filename):
                data = pandas.read_csv('password_manager.csv')

                available_websites = data.website.to_list()
                if website in available_websites:
                    data.loc[data.website == website, 'user_name'] = username
                    data.loc[data.website == website, 'password'] = password
                else:
                    print('data not available for {0}'.format(website))
                    data = data.append(info, ignore_index=True)

                data.to_csv(filename, index=False)
                display(data)
            else:
                dataframe = pandas.DataFrame(info, index=[0])
                display(dataframe)
                dataframe.to_csv(filename, index=False)

            resetInfo()


def resetInfo():
    website_text_field.delete(0, END)
    password_textfield.delete(0, END)
    website_text_field.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(120, 100, image=logo_image)
canvas.grid(row=0, column=1)

# website and its entry
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_text_field = Entry(width=37)
website_text_field.grid(row=1, column=1, columnspan=2)
website_text_field.focus()

# Email and its entry
username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)

username_textfield = Entry(width=37)
username_textfield.grid(row=2, column=1, columnspan=2)
username_textfield.insert(0, 'ankitbharti1994@gmail.com')

# password and it's field
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password_textfield = Entry(width=21)
password_textfield.grid(row=3, column=1)

generate_password_button = Button(text='Generate Password', width=12, command=generate_password)
generate_password_button.grid(row=3, column=2)

# add button
add_button = Button(text='Add', width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
