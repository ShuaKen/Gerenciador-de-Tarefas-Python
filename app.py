import PySimpleGUI as sg

def criarJanelaInicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha,key='container')],[sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]
    return sg.Window('Todo list', layout=layout, finalize=True)
#Criar janela
janela= criarJanelaInicial()
#criar regras da janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],[[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criarJanelaInicial()
