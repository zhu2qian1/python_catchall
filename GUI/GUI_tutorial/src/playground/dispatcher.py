import PySimpleGUI as sg


def ok_func() -> None:
    print("ok")


def okok_func() -> None:
    print("okok")


def submit_func(msg: str = "msg"):
    print("submitted:", msg)


# 使いたい関数とkeyをセットにして辞書にするだけ
handler = {
    "-OK-": ok_func,
    "-OKOK-": okok_func,
    "Submit": submit_func,
}


layout = [
    [sg.Text("Sample Text")],
    [sg.Button("OK", key="-OK-")],
    [sg.Button("OKOK", key="-OKOK-")],
    [sg.Submit(), sg.Cancel()],
]


window = sg.Window("Sample", layout=layout)

while True:
    event, value = window.read()

    print(event, value)
    if event in [None, "Cancel"]:
        break

    function = handler[event]  # handlerからeventに応じた関数を呼び出す
    function()

window.close()
