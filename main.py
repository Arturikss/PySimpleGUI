import PySimpleGUI as sg


class Logs:
    def skaits(x):
        return x * 22

    sg.theme('darkblue 3')
    izvelne = [
        [
            '&Fails',
            ['&Atvērt', '&Saglabāt', '---', '&Propertijas', '&Aizvērt']
        ],
        [
            '&Rediģēt',
            ['Ielīmēt', [
                'Speciāls',
                'Normāls',
            ], 'Atgriezt'],
        ],
        ['&Palīdzība', '&Par'],
    ]

    izkartojums = [[sg.Menu(izvelne, tearoff=False, pad=(300, 2))],
              [sg.T('Produkts')], [sg.I(key='-IN-')], [sg.T('Ievadīts')],
              [sg.T(key='-OUT-')], [sg.B('Izlasīt'),
                                    sg.B('Aizvērt')]]

    window = sg.Window('Artūra Darbs', izkartojums)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Aizvērt':
            break
        if event == 'Izlasit':
            rez = skaits(float(values['-IN-']))
            window['-OUT-'].update(value=round(rez, 2))
    window.close()
