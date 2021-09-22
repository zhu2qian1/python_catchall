import PySimpleGUI as sg
from json import load
from random import choice

with open(".\\json\\sg\\themes.json") as f:
    themes = load(f)

theme = choice(themes)
sg.theme(theme)

window_title: str = "Window Title"

layout_orig = [
    [sg.Text("THEME: "), sg.Text(theme)],
    [sg.Text("Enter something on Row 2"), sg.InputText(key="-row2-")],
    [
        sg.Listbox(themes, key="-seltheme-", size=(16, None)),
        sg.OK(key="-in-"),
        sg.Cancel(),
    ],
]

window = sg.Window(window_title, layout=(layout := layout_orig))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, None, "Cancel"):
        break
    elif event == "-in-" and values["-seltheme-"]:
        theme = values["-seltheme-"][-1]
        print(theme)
window.close()
