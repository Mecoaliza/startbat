import PySimpleGUI as sg
import os
from datetime import datetime
##import schedule

horarios = ["08:40", "09:30", "10:33", "11:20", "13:00", "13:50", "14:50", "16:00"]

def TempoRestante(horarios):
    now = datetime.now()
    execution_time = datetime.strptime(horarios, "%H:%M")
    execution_datetime = datetime(now.year, now.month, now.day, execution_time.hour, execution_time.minute)
        
    time_remaining = execution_datetime - now   
        
    return  time_remaining 

def create_layout(horarios):
    layout = [
    [sg.Text('')],
    [sg.Text('', size=(5,1)), sg.Text('Horários de Execução do RPA Relatórios', justification='center')]
    ]

    for horario in horarios:
        layout.append(
            [sg.Text(f'{horario}'), 
             sg.ProgressBar(100, orientation='h', size=(20, 20), key=f'-{horario}_progress'),
             sg.Text('', size=(20, 1), key=f'-{horario}_remaining')])
             
    layout.append([sg.Button('Fechar')])
    
    return layout

def format_time(remaining_time):
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'

def StartRpa():
    return os.system("start C:/temp/aplic/rpasaldos.bat")

def update_progress_bars(window, horarios):
    executed = set()
    
    while len(executed) < len(horarios):
        current = datetime.now().strftime("%H:%M")
        
        for i, horario in enumerate(horarios):
            remaining_time = TempoRestante(horario)
            total_seconds = remaining_time.total_seconds()
            total_minutes = total_seconds / 60
            percent_remain = (total_minutes / 60) * 100 
            window[f'-{horario}_progress'].update_bar(percent_remain)
            executed_text = 'Executed!' if TempoRestante(horario).days < 0 else 'Waiting...'
            remaining_str = format_time(remaining_time)
            window[f'-{horario}_remaining'].update(remaining_str + f' - {executed_text}')
            
         
            if current == horario and horario not in executed:
                StartRpa()
                executed.add(horario)
                
        event, values = window.read(timeout=1000)
        if event == sg.WINDOW_CLOSED or event == 'Fechar':
            break

    #window.close()

sg.theme('LightGreen')
layout = create_layout(horarios)
window = sg.Window('Barras de Progresso', layout, size=(450,300), finalize=True)

update_progress_bars(window, horarios)