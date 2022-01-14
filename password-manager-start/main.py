import json
import tkinter.messagebox
from tkinter import *
import pandas
import os.path
import os
from IPython.display import display
import PasswordGenerator
from enum import Enum


class FileExtension(Enum):
    CSV = 0,
    JSON = 1

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = PasswordGenerator.generate_password()
    password_textfield.delete(0, END)
    password_textfield.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    # Comeback and make it more extensible
    csv_filename = 'password_manager.csv'
    json_filename = 'password_manager.json'
    file_format = FileExtension.JSON
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
            if file_format == FileExtension.JSON:
                save_in_json_file(json_filename, website, username, password)
            elif file_format == FileExtension.CSV:
                save_in_csv_file(csv_filename, website, username, password)
            else:
                raise TypeError('Chosen File type not supported')

            resetInfo()


def save_in_csv_file(filename: str, website: str, username: str, password: str):
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


def save_in_json_file(filename: str, website: str, email: str, password: str):
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open(filename, 'r') as file_data:
            try:
                # Read data
                data = json.load(file_data)
                # Update the data
                data.update(new_data)
            except json.decoder.JSONDecodeError:
                write_json_data(new_data, filename)
            else:
                write_json_data(data, filename)
    except FileNotFoundError:
        write_json_data(new_data, filename)


def write_json_data(data, filename):
    with open(filename, 'w') as write_file_data:
        json.dump(data, write_file_data, indent=4)


def resetInfo():
    website_text_field.delete(0, END)
    password_textfield.delete(0, END)
    website_text_field.focus()


def search():
    website = website_text_field.get()
    if len(website) > 0:
        try:
            with open('password_manager.json') as file_data:
                data = json.load(file_data)
                info = data[website]
                username = info['email']
                password = info['password']
        except FileNotFoundError:
            tkinter.messagebox.showwarning('Warning!', 'Data not available for the entered website.')
        except KeyError:
            tkinter.messagebox.showwarning('Warning!', 'Data not available for the entered website.')
        else:
            username_textfield.delete(0, END)
            password_textfield.delete(0, END)
            username_textfield.insert(0, username)
            password_textfield.insert(0, password)

    else:
        tkinter.messagebox.showwarning(title='Please enter website name')


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

website_text_field = Entry(width=21)
website_text_field.grid(row=1, column=1)
website_text_field.focus()

website_search_button = Button(text='Search', width=12, command=search)
website_search_button.grid(row=1, column=2)

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
