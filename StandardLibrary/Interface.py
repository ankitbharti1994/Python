import PySimpleGUI as sg
import pandas as pd


def perform(inputFile, output):
    data = pd.read_csv(inputFile)
    data['Sum'] = data.X + data.Y + data.Z
    data['Subtraction'] = data.X - data.Y - data.Z
    data['Multiplication'] = (data.X * data.Y * data.Z) ** 2

    data.to_csv(output)


def createUserInterface():
    # All the stuff inside your window.
    layout = [
        [sg.Text('Input File'), sg.In(), sg.FileBrowse(file_types=("CSV Files", "*.csv"))],
        [sg.Text('Output File'), sg.In(), sg.FolderBrowse()],
        [sg.Button('Generate'), sg.Button('Cancel')]
    ]

    # Create the Window
    window = sg.Window('Compution', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            break
        print('You entered ', values[0], values[1])
        perform(values[0], values[1])

    window.close()


createUserInterface()
