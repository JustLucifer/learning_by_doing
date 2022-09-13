from GUI_calculator_model import sg, window
from math import sqrt
from calculations import calc


class SimpleCalculator:
    NUMS = [str(i) for i in range(10)]
    OPERATORS = ('*', '-', '+', '/')
    
    def __init__(self) -> None:
        self.history = ''

    def check_number(self, event):
        self.history += event
        try:
            if self.history[0] == '0' and self.history[1] == '0':
                self.history = self.history[:-1]
        except IndexError:
            pass

    def check_operator(self, event):
        self.history += event
        oper = event
        x = self.history[:-1]
        index = self.history.index(oper)
        return x, oper, index

    def equal(self, x, oper, index):
        try:
            y = self.history[index + 1:]
        except NameError:
            pass
        else:
            # calculates the result of expression
            res = calc(float(x), oper, float(y))
            self.history = str(res)

    def clear_input_field(self, param):
        if param == '-CLEAR-':
            self.history = self.history[:-1]
        else:
            self.history = ''
    
    def run(self):
        while True:
            event, values = window.read()
            match event:
                case sg.WIN_CLOSED:
                    window.close()
                    break
                case event if event in self.NUMS:
                    self.check_number(event)
                case event if event in self.OPERATORS:
                    x, oper, index = self.check_operator(event)
                case '-EQUAL-':
                    self.equal(x, oper, index)
                case '-CLEAR-':
                    self.clear_input_field(event)
                case '-CLEAR_EVR-':
                    self.clear_input_field(event)
                case '-SQRT-':
                    self.history = str(sqrt(float(self.history[:-1])))
                case '-DOT-':
                    self.history += '.'
                    
            window['-INPUT-'].update(self.history)
            print(event, values)