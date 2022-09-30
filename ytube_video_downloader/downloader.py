from gi.repository import GLib
import PySimpleGUI as sg
import sys


class YTubeDownloader:
    
    def __init__(self) -> None:
        sg.theme('DarkPurple1')
        sg.set_options(margins=(0,0),)
    
    def create_main_window(self):
        qualities = ('1080', '720', '480', '360', '240')
        menu = ['',['Change download directory', 'Change default resolution', 'Exit']]
        layout = [
            [sg.ButtonMenu('Menu', menu, font='DejaVuSans 10', p=0, expand_x=True,)],
            [sg.Text('Welcome to YouTube Downloader', p=15)],
            [sg.Text('Paste your video link here', p=((0,0),(20,5)))],
            [sg.Input('', s=(None,5), do_not_clear=False, tooltip='Paste video URL', p=((0,0),(0,15)), k='-URL-')],
            [sg.Combo(qualities, default_value='720', k='-QUALITY-')],
            [sg.Button('Download', p=((0,0),(40,45)))],
            [sg.T('', k='-FINISHED-',)],
        ]
        
        return sg.Window('YouTube Downloader', layout, size=(400,440), font='DejaVuSans 15',
                         element_justification='c',)
    
    def run(self):
        window = self.create_main_window()
        while True:
            event, values = window()
            print(event, values)
            if event in ('Exit', sg.WIN_CLOSED):
                window.close()
                sys.exit()
            elif event == 'Download':
                window['-FINISHED-']('Video downloaded ')
