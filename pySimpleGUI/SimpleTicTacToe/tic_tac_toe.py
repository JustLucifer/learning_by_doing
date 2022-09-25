import PySimpleGUI as sg


class TicTacToe:
    
    NUMS = [0] + [f'0{i}' for i in range(8)]
    x_image = 'pySimpleGUI/SimpleTicTacToe/images/x.png'
    o_image = 'pySimpleGUI/SimpleTicTacToe/images/o.png'
    sg.theme('LightGrey3')
    sg.set_options(
        text_color='black', button_element_size=(105,105), border_width=0,
    )    
    
    def __init__(self) -> None:
        button_def_image = 'pySimpleGUI/SimpleTicTacToe/images/white.png'
        self.turn = 'Player1'
        self.cells = ['' for _ in range(9)]
        self.layout = [[sg.T('Player 1', font='Arial 15', p=2), sg.T(text=' ' * 38), sg.T('Player 2', font='Arial 15', p=2),],
                       [sg.T(0, font='bold', text_color='#77d6ec', p=2), sg.T(text=' ' * 54), sg.T(0, font='bold', text_color='#eda4a4', p=2)],
                       [[sg.B('', k=0, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image) for _ in range(3)] for _ in range(3)]
        ]

        self.window = sg.Window('TicTacToe', self.layout, size=(360,400),
                                element_justification="c", element_padding=0,)
    
    def run(self) -> None:
        while True:
            event, values = self.window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                self.window.close()
                break
            elif event in self.NUMS:
                index = self.NUMS.index(event)
                if self.cells[index] == '':
                    if self.turn == 'Player1':
                        self.cells[index] = 'X'
                        self.turn = 'Player2'
                        self.window[event](image_filename=self.x_image)
                    elif self.turn == 'Player2':
                        self.cells[index] = 'O'
                        self.window[event](image_filename=self.o_image)
                        self.turn = 'Player1'
