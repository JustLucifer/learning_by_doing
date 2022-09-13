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
        self.after_error = False

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

    def handle_TwoOpersTogetherError(self):
        sg.popup_ok(self.TwoOpersTogetherError(), font='Arial 15 bold',
                    no_titlebar=True, grab_anywhere=True, line_width=10,
                    text_color='#ffb380')
        self.after_error = True
        self.oper = self.history[-2]
        self.x = self.history[:-2]

    def find_y(self):
        # checks if input contain to operators in a row
        if self.history[-1] in self.OPERATORS \
        and self.history[-2] in self.OPERATORS:
            raise self.TwoOpersTogetherError
        
        """checks in this way whether y == one of operators
        because of TwoOpersTogetherError """
        if self.after_error is True:
            return self.history[self.index:]
        return self.history[self.index + 1:]

    def equal(self):
        if self.history == '':
            return
        try:
            assert self.x is not None
            y = self.find_y()
        except self.TwoOpersTogetherError:
            self.handle_TwoOpersTogetherError()
        except (TypeError, AttributeError, AssertionError):
            # doubled up 'x' if (y or oper, index == '')
            self.history = str(float(self.history) * 2)
        else:
            # calculates the result of expression
            res = calc(float(self.x), self.oper, float(y))
            self.history = str(res)
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