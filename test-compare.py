import PySimpleGUI as sg
import re
import hashlib
def hash(fname, algo):
    if algo == 'MD5':
        hash = hashlib.md5()
    elif algo == 'SHA1':
        hash = hashlib.sha1()
    elif algo == 'SHA256':
        hash = hashlib.sha256()
    with open(fname) as handle: #opening the file one line at a time for memory considerations
        for line in handle:
            hash.update(line.encode(encoding = 'utf-8'))
    return(hash.hexdigest())
layout = [
    [sg.Text('Файл 1'), sg.InputText(), sg.FileBrowse(' НАЙТИ '),
     sg.Checkbox('MD5'), sg.Checkbox('SHA1')
     ],
    [sg.Text('Файл 2'), sg.InputText(), sg.FileBrowse(' НАЙТИ '),
     sg.Checkbox('SHA256')
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit(' ПРИНЯЛИ '), sg.Cancel(' ОТМЕНА ')]
]
window = sg.Window('Сравнение файлов!', layout)
while True:                             # The Event Loop
    event, values = window.read()
    #print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == ' ПРИНЯЛИ ':
        file1 = file2 = isitago = None
        #print(values[0],values[3]) #debug
        if values[0] and values[3]:
            file1 = re.findall('.+:\/.+\.+.', values[0])
            file2 = re.findall('.+:\/.+\.+.', values[3])
            isitago = 1
            if not file1 and file1 is not None:
                print('Ошибка: Файл 1 путь не правильный.')
                isitago = 0
            elif not file2 and file2 is not None:
                print('Ошибка: Файл 2 путь не правильный.')
                isitago = 0
            elif values[1] is not True and values[2] is not True and values[4] is not True:
                print('Ошибка: Выберите один тип алгоритма сравнения')
            elif isitago == 1:
                print('Инфо: Путь файла корректен.')
                algos = [] #algos to compare
                if values[1] == True: algos.append('MD5')
                if values[2] == True: algos.append('SHA1')
                if values[4] == True: algos.append('SHA256')
                filepaths = [] #files
                filepaths.append(values[0])
                filepaths.append(values[3])
                print('Инфо: Файлы сравниваются используя:', algos)
                for algo in algos:
                    print(algo, ':')
                    print(filepaths[0], ':', hash(filepaths[0], algo))
                    print(filepaths[1], ':', hash(filepaths[1], algo))
                    if hash(filepaths[0],algo) == hash(filepaths[1],algo):
                        print('Файлы одинаковые ', algo)
                    else:
                        print('Файлы не одинаковые ', algo)
        else:
            print('Пожалуйста выберете два файла.')
window.close()
