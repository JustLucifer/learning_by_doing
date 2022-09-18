from GUI_calculator_model import sg, window
from errorClasses import CantDoTwoOperationsError, MalformedExpressionError
from math import sqrt
import sys
import re
from calculations import calc


class SimpleCalculator:
    NUMS = [str(i) for i in range(10)]
    OPERATORS = ('*', '-', '+', '/')

    def __init__(self) -> None:
        self.history = ''
    
    def calc_res_of_expression(self):
        for n, i in enumerate(self.history):
            if i in self.OPERATORS and n != 0:
                oper = i
                x = self.history[:n]
                y = self.history[n + 1:]
        if int(y) == 0 and oper == '/':
            window['-ERROR_OUT-'].update("Can't divide by zero")
        else:
            self.history = str(calc(float(x), oper, float(y)))

    def equal(self):
        if self.history == '' or \
        re.match('[*/+-]$', self.history):
            return
        else:
            if re.search('[*/+-]{2,}', self.history) \
            or re.match('[*/+-]?[.]', self.history) \
            or re.match('((\d*[.])?\d+)?[*/+-][.]', self.history) \
            or re.match('[*/]?(\d*[.])?\d+[*/+-]$', self.history) \
            or re.match('[*/](\d*[.])?\d+[*/+-]?((\d*[.])?\d+[*/+-]?)*$', self.history):
                window['-ERROR_OUT-'].update(MalformedExpressionError())
            elif re.match('[+-]?(\d*[.])?\d+[*/+-](\d*[.])?\d+[*/+-]((\d*[.])?\d+)?', self.history):
                window['-ERROR_OUT-'].update(CantDoTwoOperationsError())
            elif re.match('^[+-]?(\d*[.])?\d+$', self.history):
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
        if event == sg.WIN_CLOSED:
                window.close()
                sys.exit()
        window['-ERROR_OUT-'].update('')
        
        if event in self.NUMS or event in self.OPERATORS:
            self.history += event
        else:
            match event:
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