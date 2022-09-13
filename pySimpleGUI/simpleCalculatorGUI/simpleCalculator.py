from GUI_calculator_model import sg, window
from math import sqrt
from calculations import calc


class SimpleCalculator:
    NUMS = [str(i) for i in range(10)]
    OPERATORS = ('*', '-', '+', '/')
    
    
    class TwoOpersTogetherError(Exception):
        def __str__(self) -> str:
            return 'Malformed expression'
    
    
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
        self.oper = event
        self.x = self.history[:-1]
        self.index = self.history.index(self.oper)
        return self.x, self.oper, self.index

    def equal(self):
        try:
            if self.history[-1] in self.OPERATORS \
            and self.history[-2] in self.OPERATORS:
                raise self.TwoOpersTogetherError
            y = self.history[self.index + 1:]
        except self.TwoOpersTogetherError:
            sg.popup_ok(self.TwoOpersTogetherError(), font='Arial 15 bold',
                        no_titlebar=True, grab_anywhere=True, line_width=10)
        except (TypeError, AttributeError):
            # doubled up 'x' if (y or oper, index == '')
            self.history = str(float(self.history) * 2)
        else:
            # calculates the result of expression
            res = calc(float(self.x), self.oper, float(y))
            self.history = str(res)
        finally:
            self.x, self.oper, self.index = None, None, None

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
                    self.check_operator(event)
                case '-EQUAL-':
                    self.equal()
                case '-CLEAR-':
                    self.clear_input_field(event)
                case '-CLEAR_EVR-':
                    self.clear_input_field(event)
                case '-SQRT-':
                    self.history = str(sqrt(float(self.history)))
                case '-DOT-':
                    self.history += '.'
                    
            window['-INPUT-'].update(self.history)
            print(event, values)