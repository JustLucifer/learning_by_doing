from gi.repository import GLib
from pytube import YouTube
import PySimpleGUI as sg
import sys
import os


class YTubeDownloader:
    
    def __init__(self) -> None:
        sg.theme('DarkPurple1')
        sg.set_options(margins=(0,0),)
        self.downloads_dir = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD)
        self.menu_elements = ('Change download directory', 'Change default quality')
    
    def create_main_window(self):
        qualities = ('1080', '720', '360')
        menu = ['',[self.menu_elements[0], self.menu_elements[1], 'Exit']]
        layout = [
            [sg.ButtonMenu('Menu', menu, font='DejaVuSans 10', p=0, expand_x=True, k='-MENU-')],
            [sg.Text('Welcome to YouTube Downloader', p=15)],
            [sg.Text('Paste your video link here', p=((0,0),(20,5)))],
            [sg.Input('', s=(None,5), do_not_clear=False, tooltip='Paste video URL', p=((0,0),(0,15)), k='-URL-')],
            [sg.Combo(qualities, default_value='720', k='-QUALITY-')],
            [sg.Button('Download', p=((0,0),(40,45)))],
            [sg.Text('', k='-FINISHED-')],
        ]
        
        return sg.Window('YouTube Downloader', layout, size=(400,440), font='DejaVuSans 15',
                         element_justification='c', finalize=True)

    def download_video(self, window, params):
        link = params['-URL-']
        quality = params['-QUALITY-'] + 'p'
        yt = YouTube(link)
        if quality == '1080p':
            yd = yt.streams.get_highest_resolution()
        else:
            yd = yt.streams.get_by_resolution(quality)
        yd.download(self.downloads_dir)
        os.system('play -nq -t alsa synth {} sine {}'.format(1, 440))
        window['-FINISHED-']('Video Downloaded')

    def change_default_directory(self):
        ...
    
    def change_default_quality(self):
        ...
    
    def run(self):
        window = self.create_main_window()
        while True:
            self.event, values = window()
            print(self.event, values)
            if self.event in ('Exit', sg.WIN_CLOSED):
                window.close()
                sys.exit()
            elif self.event == 'Download':
                self.download_video(window, values)
            elif self.event == '-MENU-':
                if values['-MENU-'] == self.menu_elements[0]:
                    self.change_default_directory()
                else:
                    self.change_default_quality()