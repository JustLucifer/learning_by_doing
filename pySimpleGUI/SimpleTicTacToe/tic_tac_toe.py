import PySimpleGUI as sg


class TicTacToe:
    
    EVENTS = [0] + [f'0{i}' for i in range(8)]
    DEF_IMAGE = 'pySimpleGUI/SimpleTicTacToe/images/white.png'
    X_IMAGE = 'pySimpleGUI/SimpleTicTacToe/images/x.png'
    O_IMAGE = 'pySimpleGUI/SimpleTicTacToe/images/o.png'

    def __init__(self) -> None:
        self.turn = 'Player1'
        self.cells = [''] * 9
        sg.theme('LightGrey3')
        sg.set_options(text_color='black', button_element_size=(105,105), border_width=0,)

    def create_main_window(self):
        # 'f' shortcut of font
        layout = [[sg.T('Player 1', f='Arial 15', p=2), sg.T(' ' * 38), sg.T('Player 2', f='Arial 15', p=2)],
                        [sg.T(0, f='bold', text_color='#77d6ec', p=2), sg.T(' ' * 54), sg.T(0, f='bold', text_color='#eda4a4', p=2)],
                        [[sg.B('', k=0, f='bold', mouseover_colors='#f1ede3', image_filename=self.DEF_IMAGE) for _ in range(3)] for _ in range(3)]
        ]

        return sg.Window('TicTacToe', layout, size=(360,400), element_justification="c", element_padding=0)

    def update_window_grid(self, window, event):
        index = self.EVENTS.index(event)
        if self.cells[index] == '':
            if self.turn == 'Player1':
                self.cells[index] = 'X'
                self.turn = 'Player2'
                window[event](image_filename=self.X_IMAGE)
            elif self.turn == 'Player2':
                self.cells[index] = 'O'
                self.turn = 'Player1'
                window[event](image_filename=self.O_IMAGE)

    def run(self) -> None:
        window = self.create_main_window()
        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                window.close()
                break
            else:
                self.update_window_grid(window, event)