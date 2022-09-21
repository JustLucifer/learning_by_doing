import PySimpleGUI as sg


layout = [
    [sg.T('Today', s=(43,1), font='None 15')],
    [sg.Table(values='', headings=['Tasks'], k='-TABLE-',
              num_rows=30, enable_events=True, auto_size_columns=False,
              col_widths=[40], vertical_scroll_only=False,
              justification='l', font='None 15')],
    [sg.B('Add', s=(5,1))]
]

window = sg.Window('ToDo', layout, finalize=True, element_justification='c',
                   font='bold', )
