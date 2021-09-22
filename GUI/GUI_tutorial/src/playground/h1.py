import PySimpleGUI as sg

sg.theme("DarkBrown1")

layout1 = [
    [sg.Text("ストップウォッチ", size=(20, 2), justification="center")],
    [
        sg.Text(
            "",
            size=(10, 2),
            font=("Arial", 20),
            justification="center",
            key="_OUTPUT_",
        )
    ],
    [sg.Text(" " * 5), sg.Button("更新", focus=True)],
    [sg.Text(" " * 5), sg.Button("Start/Stop", focus=True), sg.Quit()],
]

layout2 = [
    [sg.Text("ストップウォッチ", size=(20, 2), justification="center")],
    [
        sg.Text(
            "",
            size=(10, 2),
            font=("Arial", 20),
            justification="center",
            key="_OUTPUT_",
        )
    ],
    [sg.Text(" " * 5), sg.Button("Start/Stop", focus=True), sg.Quit()],
]

window = sg.Window("Stopwatch Timer", layout1)

timer_running, counter, layout, switch = True, 0, layout1, False

while True:
    event, values = window.read(timeout=10)

    # × もしくは Quitで終了
    if event in (None, "Quit"):
        break

    # Start/Stopボタンを押すとTrue/Falseが切り替わる
    elif event == "Start/Stop":
        timer_running = not timer_running

    # 更新ボタンを押すとレイアウト2に遷移する
    elif event == "更新":
        switch = not switch
        window.close()
        layout = layout2 if switch else layout1
        timer_running = True
        window = sg.Window("Stopwatch Timer", layout, finalize=True)

    # Trueならkey'_OUTPUT_'のsg.Textを更新
    if timer_running:
        window["_OUTPUT_"].update(
            "{:02d}:{:02d}.{:02d}".format(
                (counter // 100) // 60, (counter // 100) % 60, counter % 100
            )
        )
        counter += 1
