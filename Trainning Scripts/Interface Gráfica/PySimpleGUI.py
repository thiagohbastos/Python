import PySimpleGUI as sg

class TelaPython:
    def __init__(self) -> None:
        #Layout
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button()]
        ]

        #Janela
        janela = sg.Window
