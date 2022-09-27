import PySimpleGUI as sg


class TicTacToe:
    
    EVENTS = [0] + [f'0{i}' for i in range(8)]
    DEF_IMAGE = 'pySimpleGUI/SimpleTicTacToe/images/white.png'
    X_IMAGE = 'pySimpleGUI/SimpleTicTacToe/images/x.png'
    O_IMAGE = 'pySimpleGUI/SimpleTicTacToe/images/o.png'

    def __init__(self) -> None:
        self.turn = 'Player1'
        self.cells = [''] * 9
        self.score_x = 0
        self.score_o = 0
        sg.theme('LightGrey3')
        sg.set_options(text_color='#505754', button_element_size=(105,105), border_width=0)

    def create_main_window(self):
        # 'f' shortcut for font
        layout = [[sg.T('Player 1', f='Arial 15', p=2, k='-P1-'), sg.T(' ' * 38), sg.T('Player 2', f='Arial 15', p=2, k='-P2-')],
                        [sg.T(self.score_x, f='bold', text_color='#77d6ec', p=2, k='-SP1-'), sg.T(' ' * 54),
                         sg.T(self.score_o, f='bold', text_color='#eda4a4', p=2, k='-SP2-')],
                        [[sg.B('', k=0, f='bold', mouseover_colors='#f1ede3', image_filename=self.DEF_IMAGE) for _ in range(3)] for _ in range(3)]
        ]

        return sg.Window('TicTacToe', layout, size=(360,415), element_justification="c", element_padding=0, finalize=True,
                         use_custom_titlebar=True, titlebar_background_color='#f2f2ee', titlebar_font='Arial 13',titlebar_text_color='#505754')

    def window_update_template(self, k_plain, index, symbol, k_bold, image_filename):
        self.window[k_plain](font='Arial 15')
        self.cells[index] = symbol
        self.window[k_bold](font='Arial 15 bold')
        self.window[self.event](image_filename=image_filename)

    def update_window_grid(self):
        index = self.EVENTS.index(self.event)
        if self.cells[index] == '':
            if self.turn == 'Player1':
                self.turn = 'Player2'
                self.window_update_template('-P1-', index, 'X', '-P2-', self.X_IMAGE)
            elif self.turn == 'Player2':
                self.turn = 'Player1'
                self.window_update_template('-P2-', index, 'O', '-P1-', self.O_IMAGE)

    def check_for_winner(self, lst) -> str:
        winner = ''
        for el in lst:
            if set(el) == {'X'}:
                winner = 'X wins!'
                self.score_x += 1
                self.window['-SP1-'](self.score_x)
            elif set(el) == {'O'}:
                winner = 'O wins!'
                self.score_o += 1
                self.window['-SP2-'](self.score_o)
            elif self.cells.count('') == 0:
                winner = "It's a Draw!"
        return winner

    def analyze_grid(self):
        win_combinations = [self.cells[:3], self.cells[3:6], self.cells[6:],  # horizontal
                           self.cells[:7:3], self.cells[1::3], self.cells[2::3],  # vertical
                           self.cells[::4], self.cells[2:8:2]]  # diagonal
        winner = self.check_for_winner(win_combinations)
        
        if winner != '':
            layout = [[sg.T(winner, f='Arial 20 bold')]]
            sg.Window('', layout, no_titlebar=True, auto_close=True, auto_close_duration=1, )()
            return True
        return False

    def run(self) -> None:
        self.window = self.create_main_window()
        self.window['-P1-'](font='Arial 15 bold')
        while True:
            self.event, values = self.window.read()
            print(self.event, values)
            if self.event == sg.WIN_CLOSED:
                self.window.close()
                break
            else:
                self.update_window_grid()
                if self.analyze_grid():
                    self.cells = [''] * 9
                    for i in self.EVENTS:
                        self.window[i](image_filename=self.DEF_IMAGE)
