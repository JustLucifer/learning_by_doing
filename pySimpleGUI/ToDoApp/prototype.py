import PySimpleGUI as sg

layout = [
    [sg.CalendarButton('Set date', s=(10,1)), sg.T('-- -- -- --', k='-DATE-')],
    [sg.T('Write Task:'), sg.I(k='-TASK-', font=('None 15'), s=(32,1))],
    [sg.Table(values='', headings=['Index', 'Date', 'Task'], k='-TABLE-',
              s=(500,10), enable_events=True, auto_size_columns=False,
              col_widths=[5,9,30], vertical_scroll_only=False,
              justification='l', font='None 15')],
    [sg.B('Add', s=(5,1), button_color='green'), sg.B('Delete', k='-DEL-'),
     sg.Exit()],
]

window = sg.Window('To Do App', layout)

tasks = []
count = 1

while True:
    event, values = window.read()
    if event in ('Exit', sg.WIN_CLOSED):
        window.close()
        break
    elif event == 'Add':
        date = window['-DATE-'].get().split()[0]
        task = [[count, date, values['-TASK-']]]
        tasks += task
        window['-TABLE-'](tasks)
        window['-TASK-']('')
        count += 1
    elif event == '-DEL-':
        if values['-TABLE-']:
            index = values['-TABLE-'][0]
            del tasks[index]
            window['-TABLE-'](tasks)
    print(event, values)