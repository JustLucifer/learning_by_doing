import PySimpleGUI as sg
import sys

sg.theme('Gray Gray Gray')

# -------- Popups ----------
# res = sg.popup_get_text('Please, enter a text:',
#                         # password_char='*',
#                         title='popup',
#                         keep_on_top=True,
#                         location=(800, 375),
#                         font='Courier 18')
# print(res)


# -------- Buttons ----------
# menu_button = ['Menu', ['File', 'Edit', 'View', 'Settings', ['audio', 'graphics']]]


# layout = [
#     [sg.ButtonMenu('Menu', menu_def=menu_button)],
#     [sg.B('Button 1'), sg.B('Button 2')],
#     [sg.Ok(tooltip='Submit'), sg.Cancel(button_color='red')]
# ]

# window = sg.Window('Buttons', layout)
# event, values = window.read()
# print(event, values)


# ----------- CheckBox & DropDown -------------

# languages = ['English', 'German', 'French']

# col_1 = [
#     [sg.T('What is your name:')],
#     [sg.I(key='-NAME-', size=(16, 10))],
#     [sg.Ok(), sg.Cancel()],
# ]

# col_2 = [
#     [sg.CB('python', key='-python-')],
#     [sg.CB('C#', key='-C#-')],
#     [sg.CB('php', key='-php-')],
#     [sg.DD(languages, key='-LANGUAGE-', default_value=languages[0])],
# ]

# layout = [
#     [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(col_2)],
# ]

# window = sg.Window('My App', layout)

# while True:
#     event, values = window.read()
#     if event == 'Cancel':
#         window.close()
#         break
#     elif event == 'Ok':
#         sg.popup('Your name is', values['-NAME-'])
#     print(event, values)


# ----------- Frame Listbox Menu Multiline -----------------

# cities = ['Paris', 'Berlin', 'London', 'Kiev', 'Helsinki', 'New-York']
# menu = [
#     ['File', ['New file', 'Open', 'Save', 'Exit']],
#     ['Edit', ['Copy', 'Past']],
#     ['Help', ['Tutorials', 'About']],
# ]

# frame = [
#     [sg.T('Name:'), sg.I(key='-NAME-')],
#     [sg.HorizontalSeparator()],
#     [sg.CB('Python', key='-python-'), sg.CB('C#', key='-C#-')],
#     [sg.LB(cities, size=(8,4), key='city')], # result as list
# ]

# layout = [
#     [sg.Menu(menu, key='-MENU-')],
#     [sg.Multiline(key='-MULTI-', size=(53, 5))],
#     [sg.Frame('My Frame', frame)],
#     [sg.Ok(), sg.Cancel()],
# ]

# window = sg.Window('My App', layout,)

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event in ['Cancel', 'Exit']:
#         window.close()
#         break
#     print(event, values)


# ----------- Progress Bar -----------------

# layout = [
#     [sg.ProgressBar(1000, orientation='h', size=(50, 25), key='-PRSBAR-')],
#     [sg.Cancel()]
# ]

# window = sg.Window('My App', layout,)

# for i in range(1000):
#     event, values = window.read(timeout=1)
#     if event == sg.WIN_CLOSED or event == 'Cancel':
#         window.close()
#         break
#     window['-PRSBAR-'].update(i+1)
# print(event, values)
# window.close()


# --------- Tabs RadioButtons Slider Spin StatusBar -------------

# tab_1 = [
#     [sg.T('Full Name'), sg.I(size=(30,4),)],
#     [sg.Radio('Male', group_id='gender')],
#     [sg.Radio('Female', group_id='gender')],
#     [sg.T('Age:')],
#     [sg.Slider(range=(1,100), orientation='h', default_value=20, key='-AGE-')],
#     [sg.Spin(values=list(range(1,11)), size=(5, 4), initial_value=3)],
#     [sg.Ok('Sumbit'), sg.Cancel()],
# ]

# tab_2 = [
#     [sg.CB('Python', size=(10,4)), sg.CB('C#',)],
#     [sg.CB('JavaScript', size=(10,4)), sg.CB('Java',)],
# ]

# layout = [
#     [sg.StatusBar('Welcome to my app')],
#     [sg.TabGroup([
#         [sg.Tab('Tab 1', tab_1), sg.Tab('Tab 2', tab_2)]
#     ])]
# ]

# window = sg.Window('My App', layout)

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel':
#         window.close()
#         break
#     print(event, values)


# --------- File-FolderBrowse Calendar -------------

# sg.Table for creating Table

# layout = [
#     [sg.I(key='-PATH-')],
#     [sg.T('File Browse', size=(33,1)), 
    #  sg.FileBrowse(target='-PATH-', 
#                    file_types=(
#                        ('text files', '*.txt'), 
#                        ('png files', '*.png')
#                        ))], # for saving - FileSaveAs
#     [sg.T('Folder Browse', size=(33,1)), sg.FolderBrowse(target='-PATH-')],
#     [sg.T(size=(29,1)), sg.CalendarButton('Choose date')],
#     [sg.Ok(), sg.Cancel()],
# ]

# window = sg.Window('My App', layout,
#                    enable_close_attempted_event=True)

# while True:
#     event, values = window.read()
#     # if event in ('Cancel', sg.WIN_CLOSED):
#     #     window.close()
#     #     break
    
#     # attempt to close the window
#     if event == '-WINDOW CLOSE ATTEMPTED-' and \
#     sg.popup_yes_no('Do you want to close app?', title='Confirm') == 'Yes':
#             window.close()
#             sys.exit()
#     # elif event == 'Ok':
#     #     window['-OUTPUT-'].update(values['-DATE-'])
#     print(event, values)

# ---------- List Comprehension to Build Rows - Table Simulation -------------

# headings = ['HEADER 1', 'HEADER 2', 'HEADER 3','HEADER 4']  # the text of the headings
# header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]  # build header layout
# input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]
# layout = header + input_rows

# window = sg.Window('Table Simulation', layout, font='Courier 12')
# event, values = window.read()


# ---------- Output Element -------------

# def ChatBot():
#     layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],
#               [sg.Output(size=(80, 20))],
#               [sg.Multiline(size=(70, 5), enter_submits=True),
#                sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
#                sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

#     window = sg.Window('Chat Window', layout, default_element_size=(30, 2))

#     # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
#     while True:
#         event, value = window.read()
#         if event == 'SEND':
#             print(value)
#         else:
#             break
#     window.close()
# ChatBot()
