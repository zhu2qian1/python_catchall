import PySimpleGUI as sg

sg.theme("DarkBrown1")

layout = [
    [sg.Text("TickWatch", size=(20, 2), justification="center")],
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

window = sg.Window("Stopwatch Timer", layout)

timer_running, counter = True, 0

while True:
    event, values = window.read(timeout=10)

    # × もしくは Quitで終了
    if event in (None, "Quit"):
        break

    # Start/Stopボタンを押すとTrue/Falseが切り替わる
    elif event == "Start/Stop":
        timer_running = not timer_running

    # Trueならkey'_OUTPUT_'のsg.Textを更新
    if timer_running:
        window["_OUTPUT_"].update(
            "{:02d}゜{:02d}′  {:02d}″".format(
                (counter // 100) // 60, (counter // 100) % 60, counter % 100
            )
        )
        counter += 1
