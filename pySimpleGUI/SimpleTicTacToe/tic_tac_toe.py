import PySimpleGUI as sg

sg.theme('Reddit')

class TicTacToe:
    
    def __init__(self) -> None:
        layout = [[sg.T('Player 1', font='Arial 15'), sg.T(text=' ' * 47), sg.T('Player 2', font='Arial 15'),],
                  [sg.T(text=' ' * 3), sg.T(0, font='bold'), sg.T(text=' ' * 63), sg.T(0, font='bold')],
                  [[sg.B(' ', s=(10,8), font='bold', p=0, k=f'{i+1} {j+1}') for j in range(3)] for i in range(3)]]
        self.window = sg.Window('TicTacToe', layout)
        self.turn = 'first'
        self.cells = self.create_cells_for_check()
    
    def create_cells_for_check(self) -> list:
        cells = []
        for i in range(3):
            for j in range(3):
                cells.append(f'{i+1} {j+1}')
        return cells

    def run(self) -> None:
        while True:
            event, values = self.window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                self.window.close()
                break
            elif event in self.cells:
                if self.turn == 'first':
                    self.window[event]('X')
                    self.turn = 'second'
                elif self.turn == 'second':
                    self.window[event]('O')
                    self.turn = 'first'
