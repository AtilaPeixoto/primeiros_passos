from random import randint
import PySimpleGUI as sg 

class genio:
    
    def __init__(self):
        self.mm = 1
        self.mx = 20
        self.maior = 'foi abaixo... Tente maior!'
        self.menor = 'foi alto... Tente menor!'
        self.acertou = 'Parabens!!!'
        
        
    def visor(self):
        layout = [
            [sg.Text('Escolha um numero e tente a sorte!!!', size=(40, 1))],
            [sg.Input(size=(20, 1), key='Value')],
            [sg.Button('JOGAR!!!', size=(30, 4), button_color='#00ff00', mouseover_colors='#ff0000' )],
            [sg.Output(size=(20, 10))]
        ]
        self.janela = sg.Window('Genio dos numeros', layout=layout)
        self.event, self.value = self.janela.Read()
        #if self.event == Win_cloused():
            
        
    
    def gerar(self):
        self.aleatorio = randint(self.mm, self.mx)
        self.enviar()
        
        
    def enviar(self):
        self.visor()
        while True:
            self.event, self.value = self.janela.Read()
            if self.event == sg.WIN_CLOSED:
                break
            if self.event == 'JOGAR!!!':
                fim = self.iniciar()
                if fim == True:
                    break
        
        
    def iniciar(self):
        try:
                self.numero = self.value['Value']
                if self.numero.isnumeric():
                    self.numero = int(self.numero)
                    acerto = self.responder()
                    if acerto == True:
                        return True
                else:
                    print("Digite um numero!!!")
        except:
            self.gerar()                    
    
    
    def responder(self):
        if self.numero > self.aleatorio:
            return print(self.menor)
        elif self.numero < self.aleatorio:
            return print(self.maior)
        else:
            return [print(self.acertou), True]
            
            
jogador = genio()
jogador.gerar()