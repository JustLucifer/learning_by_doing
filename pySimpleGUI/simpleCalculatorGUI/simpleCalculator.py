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
        val = self.history.rstrip('+-*/')

        for n, i in enumerate(val):
            if i in self.OPERATORS and n != 0:
                oper = i
                x = val[:n]
                y = val[n + 1:]

        if int(y) == 0 and oper == '/':
            window['-ERROR_OUT-']("Can't divide by zero")
        else:
            self.history = str(calc(float(x), oper, float(y)))
    
    def pre_check_history(self, next_func):
        if re.match('[*/+-]$', self.history) \
        or re.search('[*/+-]{2,}', self.history) \
        or re.match('[*/+-]?[.]', self.history) \
        or re.match('((\d*[.])?\d+)?[*/+-][.]', self.history) \
        or re.match('[*/](\d*[.])?\d+[*/+-]?((\d*[.])?\d+[*/+-]?)*$', self.history):
            window['-ERROR_OUT-'](MalformedExpressionError())
        else:
            if next_func == '=':
                self.equal()
            else:
                self.calc_square_root()

    def equal(self):
        if re.match('[+-]?(\d*[.])?\d+[*/+-](\d*[.])?\d+[*/+-](\d*[.])?\d+', self.history):
            window['-ERROR_OUT-'](CantDoTwoOperationsError())
        elif re.match('[+-]?(\d*[.])?\d+[*/+-]?$', self.history):
            self.history = str(float(self.history.strip('+-*/')) * 2)
        else:
            self.calc_res_of_expression()
    
    def calc_square_root(self):

        if self.history[0] == '-' or self.history[-1] == 'i':
            minus = 'i'
        else:
            minus = ''

        # check position of operator
        for n, i in enumerate(self.history):
            if i in '+-*/' and n != len(self.history) - 1 and n != 0:
                window['-ERROR_OUT-'](MalformedExpressionError())
                return

        val = self.history.strip('+-*/i')
        self.history = str(round(sqrt(float(val)), 6)) + minus

    def clear_input_field(self, param):
        if param == 'C':
            self.history = self.history[:-1]
        else:
            self.history = ''

    def change_history(self, event):
        if event == sg.WIN_CLOSED:
                window.close()
                sys.exit()
        window['-ERROR_OUT-']('')
        
        if event in self.NUMS or event in self.OPERATORS:
            self.history += event
        elif event == '.':
            self.history += '.'
        elif self.history == '':
            return
        else:
            if event.startswith('C'):
                self.clear_input_field(event)
            else:
                self.pre_check_history(event)

    def run(self):
        while True:
            event, values = window.read()
            self.change_history(event=event)
            window['-INPUT-'](self.history)
            print(event, values)