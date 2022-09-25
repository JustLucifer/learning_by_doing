import PySimpleGUI as sg


class TicTacToe:
    
    NUMS = [i for i in range(9)]
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
                  [sg.B('', k=0, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image),
                   sg.B('', k=1, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image),
                   sg.B('', k=2, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image)],
                  [sg.B('', k=3, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image),
                   sg.B('', k=4, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image),
                   sg.B('', k=5, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image)],
                  [sg.B('', k=6, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image),
                   sg.B('', k=7, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image),
                   sg.B('', k=8, f='bold', mouseover_colors='#f1ede3', image_filename=button_def_image)]
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
            elif int(event) in self.NUMS:
                if self.cells[int(event)] == '':
                    if self.turn == 'Player1':
                        self.cells[int(event)] = 'X'
                        self.turn = 'Player2'
                        self.window[event](image_filename=self.x_image)
                    elif self.turn == 'Player2':
                        self.cells[int(event)] = 'O'
                        self.window[event](image_filename=self.o_image)
                        self.turn = 'Player1'
