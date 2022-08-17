from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from random import randint
from calculations import calculation
from kivy.uix.label import Label


class MainWindow(Widget):
    answer = ObjectProperty(None)
    result = ObjectProperty(None)
    
    def generate_task(self):
        self.x, self.y = randint(2, 9), randint(2, 9)
        self.oper = '*'
        return str(self.x) + ' ' + self.oper + ' ' + str(self.y)
        
    def check_answer(self):
        # self.task = ObjectProperty(None)
        
        res = calculation(self.x, self.oper, self.y)
        
        if int(self.answer.text) == res:
            self.ids.result.text = 'Right!'
            self.result.background_color = 0, 0.8, 0, 1
            print("Right!")
        else:
            self.result.background_color = 1, 0, 0, 1
            self.ids.result.text = 'Wrong!'
            print("Wrong!")
        
        self.ids.task.text = self.generate_task()
        
        self.answer.text = ''


class MathGameApp(App):
    
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MathGameApp().run()