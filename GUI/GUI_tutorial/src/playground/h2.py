import PySimpleGUI as sg

sg.theme("DarkBlue2")

tab1_layout = [
    [sg.Text("ストップウォッチ", size=(20, 2), justification="center")],
    [
        sg.Text(
            "",
            size=(10, 2),
            font=("Helvetica", 20),
            justification="center",
            key="_OUTPUT_",
        )
    ],
    [sg.Text(" " * 5), sg.Button("Start/Stop", focus=True), sg.Quit()],
]

tab2_layout = [[sg.Text("tab 2")], [sg.Input(key="input")]]

layout = [
    [sg.TabGroup([[sg.Tab("Tab 1", tab1_layout), sg.Tab("Tab 2", tab2_layout)]])],
    [sg.Button("Read")],
]

window = sg.Window("ストップウォッチ", layout, default_element_size=(12, 1))
timer_running, counter = True, 0

while True:
    event, values = window.read(timeout=10)

    # × もしくは Quitで終了
    if event in (None, "Quit"):
        break

    # Start/Stopボタンを押すとTrue/Falseが切り替わる
    elif event == "Start/Stop":
        timer_running = not timer_running

    # Readボタンを押すとinputのテキストが表示
    elif event == "Read":
        print(values["input"])

    # Trueならkey'_OUTPUT_'のsg.Textを更新
    if timer_running:
        window["_OUTPUT_"].update(
            "{:02d}:{:02d}.{:02d}".format(
                (counter // 100) // 60, (counter // 100) % 60, counter % 100
            )
        )
        counter += 1
