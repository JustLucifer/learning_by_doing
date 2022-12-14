from gi.repository import GLib
from pytube import YouTube
import PySimpleGUI as sg
import json
import sys
import os
import re


class YTubeDownloader:
    
    def __init__(self) -> None:
        sg.theme('DarkPurple1')
        sg.set_options(margins=(0,0),)
        self.menu_elements = ('Change download directory', 'Change default quality',
                              'Download from .txt file')
        self.read_settings_from_json()

    def read_settings_from_json(self):
        try:
            with open('youtube_video_downloader/settings/def_dir.json') as f:
                s = json.load(f)['dir']
                if s:
                    self.downloads_dir = s
                else: 
                    raise FileNotFoundError
        except FileNotFoundError:
            self.downloads_dir = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD)

        try:
            with open('youtube_video_downloader/settings/def_quality.json') as f:
                s = json.load(f)['qual']
                self.def_quality = s
        except FileNotFoundError:
            self.def_quality = '720'
    
    def create_main_window(self):
        qualities = ('1080', '720', '360')
        menu = ['',[self.menu_elements, 'Exit']]
        layout = [
            [sg.ButtonMenu('Menu', menu, font='DejaVuSans 10', p=0, expand_x=True, k='-MENU-')],
            [sg.Text('Welcome to YouTube Downloader', p=15)],
            [sg.Text('Paste your video link here', p=((0,0),(20,5)))],
            [sg.Input('', s=(None,5), do_not_clear=False, tooltip='Paste video URL', p=((0,0),(0,15)), k='-URL-')],
            [sg.Combo(qualities, default_value=self.def_quality, k='-QUALITY-')],
            [sg.Button('Download', p=((0,0),(40,45)))],
            [sg.Text('', k='-FINISHED-')],
        ]
        
        return sg.Window('YouTube Downloader', layout, size=(400,440), font='DejaVuSans 15',
                         element_justification='c', finalize=True)

    def check_link(self, window, url):
        if re.match('https://www.youtube.com/watch?.+', url):
            return url
        else:
            window['-FINISHED-']('Incorrect url')

    def download_video(self, window, link, quality):
        link = link
        quality = quality + 'p'
        yt = YouTube(link)
        if quality == '1080p':
            yd = yt.streams.get_highest_resolution()
        else:
            yd = yt.streams.get_by_resolution(quality)
        yd.download(self.downloads_dir)
        # os.system('play -nq -t alsa synth {} sine {}'.format(1, 440))
        window['-FINISHED-']('Video Downloaded')

    def change_default_directory(self):
        folder = sg.popup_get_folder('Choose new folder', font='DejaVuSans 12', size=(30, 40))
        if folder not in ('', ' '):
            self.downloads_dir = folder
        with open('youtube_video_downloader/settings/def_dir.json', 'w') as f:
            json.dump({'dir': self.downloads_dir}, f)
    
    def change_default_quality(self):
        layout = [
            [sg.Text('Choose new default quality', p=15)],
            [sg.Radio('1080', group_id='-Q-', k='1080'),
             sg.Radio('720', group_id='-Q-', k='720'),
             sg.Radio('360', group_id='-Q-', k='360')],
            [sg.Text('Setting will be applied after restart', p=15, font='DejaVuSans 10')],
            [sg.Ok(p=0), sg.Text(''), sg.Cancel(p=0)],
        ]
        
        window = sg.Window('YouTube Downloader', layout, font='DejaVuSans 13', element_justification='c')

        while True:
            event, values = window()
            print(event, values)
            if event == 'Ok':
                for k, v in values.items():
                    if v is True:
                        self.def_quality = k
            window.close()
            break
        
        with open('youtube_video_downloader/settings/def_quality.json', 'w') as f:
            json.dump({'qual': self.def_quality}, f)
    
    def download_multiple_videos_from_file(self):
        file_with_links = sg.popup_get_file('Select .txt file\n(links must be separated by a new line)',
                                            title='Select file',
                                            font='DejaVuSans 12',
                                            size=(30, 40),
                                            file_types=(('text files', '*.txt'),))
        if file_with_links in (' ', '', None): return
        
        with open(file_with_links) as f:
            lst_links = f.read().split('\n')

        for n, link in enumerate(lst_links):
            if re.match('https://www.youtube.com/watch?.+', link):
                yt = YouTube(link)
                yd = yt.streams.get_by_resolution(self.def_quality + 'p')
                yd.download(self.downloads_dir)
                print(n + 1, yt.title, 'downloaded')
        else:
            os.system('play -nq -t alsa synth {} sine {}'.format(1, 440))
    
    def run(self):
        window = self.create_main_window()
        while True:
            event, values = window()
            print(event, values)
            if event == sg.WIN_CLOSED:
                window.close()
                sys.exit()
            elif event == 'Download':
                link = self.check_link(window, values['-URL-'])
                if link is not None:
                    self.download_video(window, link, values['-QUALITY-'])
            elif event == '-MENU-':
                if values['-MENU-'] == self.menu_elements[0]:
                    self.change_default_directory()
                elif values['-MENU-'] == self.menu_elements[1]:
                    self.change_default_quality()
                elif values['-MENU-'] == self.menu_elements[2]:
                    self.download_multiple_videos_from_file()
                else:
                    window.close()
                    sys.exit()
