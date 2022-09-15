from GUI_calculator_model import sg, window
from math import sqrt
import sys
import re
from calculations import calc


class SimpleCalculator:
    NUMS = [str(i) for i in range(10)]
    OPERATORS = ('*', '-', '+', '/')


    class MalformedExpressionError(Exception):
        def __str__(self) -> str:
            return 'Malformed expression'


    def __init__(self) -> None:
        self.history = ''

    def handle_MalformedExpressionError(self):
        sg.popup_ok(self.MalformedExpressionError(), font='Arial 15 bold',
                    no_titlebar=True, grab_anywhere=True, line_width=10,
                    text_color='#ffb380')
    
    def calc_res_of_expression(self):
        for n, i in enumerate(self.history):
            if i in self.OPERATORS and n != 0:
                oper = i
                x = self.history[:n]
                y = self.history[n + 1:]
        self.history = str(calc(float(x), oper, float(y)))

    def equal(self):
        if self.history == '':
            return
        else:
            if re.match('^[*/]?\d+$', self.history) \
                or re.match('^(\d*[.])?\d+[*/+-]$', self.history):
                self.handle_MalformedExpressionError()
            elif re.match('^[+-]?\d*[*/+-]{2,}', self.history) \
                or re.match('^[+-]?(\d*[.])?\d+[*/+-]{2,}', self.history):
                self.handle_MalformedExpressionError()
            elif re.match('^[+-]?\d+$', self.history) \
                or re.match('^[+-]?(\d*[.])?\d+$', self.history):
                self.history = str(float(self.history) * 2)
            else:
                self.calc_res_of_expression()

    def clear_input_field(self, param):
        if param == '-CLEAR-':
            self.history = self.history[:-1]
        else:
            self.history = ''
    
    def calc_square_root(self):
        val = self.history.strip('+-*/')
        if self.history[0] == '-':
            minus = 'i'
        else:
            minus = ''
        self.history = str(round(sqrt(float(val)), 6)) + minus
    
    def change_history(self, event):
        if event in self.NUMS or event in self.OPERATORS:
            self.history += event
        else:
            match event:
                case sg.WIN_CLOSED:
                    window.close()
                    sys.exit()
                case '-EQUAL-':
                    self.equal()
                case '-CLEAR-':
                    self.clear_input_field(event)
                case '-CLEAR_EVR-':
                    self.clear_input_field(event)
                case '-SQRT-':
                    self.calc_square_root()
                case '-DOT-':
                    self.history += '.'

    def run(self):
        while True:
            event, values = window.read()
            self.change_history(event=event)
            window['-INPUT-'].update(self.history)
            print(event, values)