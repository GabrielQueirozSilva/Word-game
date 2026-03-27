import pygame
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QVBoxLayout, QListView
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import socket
import pickle
import time
import tkinter as tk
from tkinter import messagebox

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Self-blinded are you be you pride; look thogh the nigth, the world is wide')
imagem_fundo = pygame.image.load("download (1).jpg").convert()
imagem_fundo_2 = pygame.image.load("download.jpg").convert()
largura_imagem = 740  # Largura 
altura_imagem = 700   # Altura 
imagem_fundo_2 = pygame.transform.scale(imagem_fundo_2, (largura_imagem, altura_imagem))

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL_CLARO = (173, 216, 230)
VERDE_CLARO = (144, 238, 144)
VERMELHO_CLARO = (255, 182, 193)
VIOLETA = (148, 0, 211)
LARANJA = (255, 165, 0)

# Fonte
fonte = pygame.font.SysFont(None, 36)


# Estados das telas
TELA_INICIAL = 'tela_inicial'
TELA_ADD_WORLD = 'tela_add_world'
TELA_LETS_TRY = 'tela_lets_try'
TELA_REVISE = 'tela_revise'
TELA_KNOW = 'tela_know'
TELA_EDIT = 'tela_edit'

# Variáveis de entrada de texto
input_rect = pygame.Rect(200, 150, 400, 50)
input_rect1 = pygame.Rect(200, 250, 400 ,50)

# Variáveis para a tela Let's Try
retangulo_1_rect = pygame.Rect(200, 100, 400, 50)
retangulo_2_rect = pygame.Rect(200, 200, 400, 50)
quadrado_rect = pygame.Rect(650, 100, 100, 100)

# Função para desenhar botões
def desenhar_botao(tela, cor, posicao, largura, altura, texto):
    pygame.draw.rect(tela, cor, (posicao[0], posicao[1], largura, altura))
    texto_botao = fonte.render(texto, True, PRETO)
    tela.blit(texto_botao, (posicao[0] + (largura - texto_botao.get_width()) // 2,
                            posicao[1] + (altura - texto_botao.get_height()) // 2))

# Função para verificar se o botão foi clicado
def botao_clicado(posicao_mouse, posicao_botao, largura, altura):
    return posicao_botao[0] <= posicao_mouse[0] <= posicao_botao[0] + largura and \
           posicao_botao[1] <= posicao_mouse[1] <= posicao_botao[1] + altura


def acessar_mensagem(self,cliente_socket):
    menssagem =  f'acessar_mensagens'
    self.cliente_socket.send(menssagem.encode())
    recebido = self.cliente_socket.recv(1024)
    return pickle.loads(recebido)

def acessar_mensagem_revise(self,cliente_socket):
    mensagem = f'acessar_mensagens_revise'
    self.cliente_socket.send(mensagem.encode())
    recebido = self.cliente_socket.recv(1024)
    return pickle.loads(recebido) 


def popup_simples(mensagem):
    root = tk.Tk()
    root.withdraw() 
    messagebox.showinfo("Aviso", mensagem)
    root.destroy()
    
class Cliente: #" chamou sua atencao"
    
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.addr = ((ip,port))
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    
    def conectar_servidor(self):
        """Utilizado para fazer a conexão com o servidor
        
        """
        try:
            self.cliente_socket.connect(self.addr)
            print("Conectado ao servidor.")
            self.show_main = Main(self.cliente_socket,TELA_INICIAL,'',True,'',True,'')
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")



# Função principal

class Main():
    def __init__(self,cliente_socket,estado_tela,input_text,active_input,retangulo_2_text,rodando,retangulo_1_texto):
        self.cliente_socket = cliente_socket
        self.estado_tela = estado_tela
        self.input_text = input_text
        self.active_input = active_input
        self.retangulo_2_text = retangulo_2_text
        self.rodando = rodando
        self.retangulo_1_texto = retangulo_1_texto
        
        while self.rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    posicao_mouse = pygame.mouse.get_pos()
                    if self.estado_tela == TELA_INICIAL:
                        if botao_clicado(posicao_mouse, (470, 100), 200, 100):
                            self.estado_tela = TELA_KNOW
                    elif self.estado_tela == TELA_KNOW:
                        if botao_clicado(posicao_mouse, (130, 100), 200, 100):                        
                            self.estado_tela = TELA_ADD_WORLD
                                                        
                        elif botao_clicado(posicao_mouse, (470, 100), 200, 100):
                            self.estado_tela = TELA_LETS_TRY
                            id,self.retangulo_1_texto,port = acessar_mensagem(self,cliente_socket)
                        
                        elif botao_clicado(posicao_mouse, (470, 300), 200, 100):
                            self.estado_tela = TELA_EDIT
                            
                        elif botao_clicado(posicao_mouse,(130,300),200,100):
                            self.estado_tela = TELA_REVISE
                            id,self.retangulo_1_texto,port = acessar_mensagem_revise(self,cliente_socket)
                            
                    elif self.estado_tela == TELA_LETS_TRY:
                            try:
                                if botao_clicado(posicao_mouse,(35,555),75,35):
                                    menssagem = f'resettry'
                                    self.cliente_socket.send(menssagem.encode())                            
                                    pygame.display.flip()
                                    
                                elif botao_clicado(posicao_mouse,(195,555),75,35):
                                    menssagem =  f'aprendido,{self.retangulo_1_texto}'
                                    self.cliente_socket.send(menssagem.encode())
                                    print(f"palavra aprendidda: {self.retangulo_1_texto}")
                    
                                elif botao_clicado(posicao_mouse,(115,555),75,35):
                                    self.estado_tela = TELA_EDIT
                                    print(id,self.retangulo_1_texto,port)
                            except:
                                popup_simples("Sem palavras no Banco de dados!")


                    elif self.estado_tela == TELA_REVISE:
                        if botao_clicado(posicao_mouse,(35,555),75,35):
                            menssagem = f'resetrevise'
                            self.cliente_socket.send(menssagem.encode())                            
                            pygame.display.flip()

                                                      
                elif evento.type == pygame.KEYDOWN and active_input:
                    
                        if evento.key == pygame.K_BACKSPACE:
                            if self.active_input == 'input_text':
                                self.input_text = self.input_text[:-1]
                            elif self.active_input == 'retangulo_2_text':
                                self.retangulo_2_text = self.retangulo_2_text[:-1]
                                
                        elif evento.key == pygame.K_ESCAPE:
                            self.retangulo_2_text = ''
                            self.retangulo_1_text = ''
                            if self.estado_tela == TELA_LETS_TRY:
                                self.estado_tela = TELA_KNOW
                            elif self.estado_tela == TELA_KNOW:
                                self.estado_tela = TELA_INICIAL
                            elif self.estado_tela == TELA_ADD_WORLD:
                                self.estado_tela = TELA_KNOW
                            elif self.estado_tela == TELA_REVISE:
                                self.estado_tela = TELA_KNOW
                            elif self.estado_tela == TELA_EDIT:
                                self.estado_tela = TELA_LETS_TRY
                            else:
                                self.rodando = False            
                                
                        elif evento.key == pygame.K_RETURN:
                            if self.estado_tela == TELA_LETS_TRY:
                                if self.retangulo_2_text == port:
                                    menssagem = f'incremento,{id}'
                                    self.cliente_socket.send(menssagem.encode())
                                    pygame.draw.rect(tela, VERDE_CLARO, quadrado_rect)
                                    pygame.display.flip()
                                    time.sleep(0.2)
                                    self.retangulo_2_text = ''
                                else:
                                    pygame.draw.rect(tela, VERMELHO_CLARO, quadrado_rect)
                                    pygame.display.flip()
                                    time.sleep(0.2)
                                    self.retangulo_2_text = ''
                                    print(port)
                                id,self.retangulo_1_texto,port = acessar_mensagem(self,cliente_socket)

                            if self.estado_tela == TELA_ADD_WORLD:
                                    try:
                                        a,b = self.input_text.split(',')
                                        menssagem =  f'adicionar,{a},{b}'
                                        self.cliente_socket.send(menssagem.encode())
                                        print(f"Texto adicionado: {self.input_text}")
                                        self.input_text = ''
                                        popup_simples("Palavra aprendida")
                                    except:
                                        popup_simples("Formato incorreto!")
                                    
                            if self.estado_tela == TELA_EDIT:
                                    try:
                                        palavra1,palavra2,estado = self.input_text.split(',')#estado siginifica aprendido ou não. Sim = 1 Não = 0
                                        menssagem = f'edit,{id},{palavra1},{palavra2},{estado}'
                                        self.cliente_socket.send(menssagem.encode())
                                        popup_simples("Palavra editada")
                                        self.input_text = ''
                                    except:
                                        popup_simples("Formato incorreto!")
                            
                            elif self.estado_tela == TELA_REVISE:
                                try:
                                    if self.retangulo_2_text == port:
                                        menssagem = f'incremento,{id}'
                                        self.cliente_socket.send(menssagem.encode())
                                        pygame.draw.rect(tela, VERDE_CLARO, quadrado_rect)
                                        pygame.display.flip()
                                        time.sleep(0.2)
                                        self.retangulo_2_text = ''
                                    else:
                                        pygame.draw.rect(tela, VERMELHO_CLARO, quadrado_rect)
                                        pygame.display.flip()
                                        self.retangulo_2_text = ''                                    
                                        time.sleep(0.2)
                                        print(port)
                                    id,self.retangulo_1_texto,port = acessar_mensagem_revise(self,cliente_socket)
                                except:
                                    popup_simples("Sem palavras aprendidas!")

                                


                        else:
                            if self.active_input == 'input_text':
                                self.input_text += evento.unicode
                            elif self.active_input == 'retangulo_2_text':
                                self.retangulo_2_text += evento.unicode
                            
            tela.fill(BRANCO)

            if self.estado_tela == TELA_INICIAL:
                tela.blit(imagem_fundo,(25,-115))
                desenhar_botao(tela, VERDE_CLARO, (470, 100), 200, 100, "know")                
                
            elif self.estado_tela == TELA_KNOW:
                tela.blit(imagem_fundo,(25,-115))
                desenhar_botao(tela, AZUL_CLARO, (130, 100), 200, 100, "Add Word")
                desenhar_botao(tela, VERDE_CLARO, (470, 100), 200, 100, "let's try")
                desenhar_botao(tela,VIOLETA,(130,300),200,100,"Revise")
                desenhar_botao(tela,LARANJA,(470,300),200,100,"Edit Word")


            elif self.estado_tela == TELA_ADD_WORLD:
                self.active_input = 'input_text'
                pygame.draw.rect(tela, AZUL_CLARO, input_rect)
                text_surface = fonte.render(self.input_text, True, PRETO)
                tela.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))

            elif self.estado_tela == TELA_EDIT:
                self.active_input = 'input_text'
                text = str(id) + " | " + self.retangulo_1_texto + " | " + port
                pygame.draw.rect(tela, AZUL_CLARO, input_rect)
                text_surface = fonte.render(text, True, PRETO)
                tela.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))
                
                pygame.draw.rect(tela, VERDE_CLARO, input_rect1)
                text_surface1 = fonte.render(self.input_text, True, PRETO)
                tela.blit(text_surface1, (input_rect1.x + 10, input_rect1.y + 10))

            elif self.estado_tela == TELA_LETS_TRY:
                self.active_input = 'retangulo_2_text'
                tela.blit(imagem_fundo_2,(30,-100))
                pygame.draw.rect(tela, AZUL_CLARO, retangulo_1_rect)
                text_surface_1 = fonte.render(self.retangulo_1_texto, True, PRETO)
                tela.blit(text_surface_1,(retangulo_1_rect.x + 10, retangulo_1_rect.y + 10))
                pygame.draw.rect(tela, AZUL_CLARO, retangulo_2_rect)
                text_surface_2 = fonte.render(self.retangulo_2_text, True, PRETO)
                tela.blit(text_surface_2, (retangulo_2_rect.x + 10, retangulo_2_rect.y + 10))
                pygame.draw.rect(tela, PRETO, quadrado_rect)
                desenhar_botao(tela,BRANCO,(35,555),75,35,"Reset")
                desenhar_botao(tela,BRANCO,(195,555),85,35,"I know")
                desenhar_botao(tela,BRANCO,(115,555),75,35,"Edit")

                
            elif self.estado_tela == TELA_REVISE:
                self.active_input = 'retangulo_2_text'
                tela.blit(imagem_fundo_2,(30,-100))
                pygame.draw.rect(tela, AZUL_CLARO, retangulo_1_rect)
                text_surface_1 = fonte.render(self.retangulo_1_texto, True, PRETO)
                tela.blit(text_surface_1,(retangulo_1_rect.x + 10, retangulo_1_rect.y + 10))
                pygame.draw.rect(tela, AZUL_CLARO, retangulo_2_rect)
                text_surface_2 = fonte.render(self.retangulo_2_text, True, PRETO)
                tela.blit(text_surface_2, (retangulo_2_rect.x + 10, retangulo_2_rect.y + 10))
                pygame.draw.rect(tela, PRETO, quadrado_rect)
                desenhar_botao(tela,BRANCO,(35,555),75,35,"Reset")
            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    cliente = Cliente('localhost', 8007)
    cliente.conectar_servidor()
