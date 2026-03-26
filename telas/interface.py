import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QMovie
from teste import Tela_Inicial  
from tela_know import Tela_Know
from tela_lets_try import Ui_lets_Try
from tela_add_word import Tela_Add_Word 
from revise import Revise
from tela_edit import tela_edit
import pickle
import socket
import struct

class Cliente:
    
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.addr = ((ip,port))
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
            
    def conectar_servidor(self):

        try:
            self.cliente_socket.connect(self.addr)
            print("Conectado ao servidor.")
            app = QApplication(sys.argv)
            self.window = Main(self.cliente_socket)
            sys.exit(app.exec_())

        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")
    
    def resetar(cliente_socket):
        mensagem = f'resettry'
        cliente_socket.send(mensagem.encode())
        
    def incremento(cliente_scoket,id):
        mensagem = f'incremento,{id}'
        cliente_scoket.send(mensagem.encode())
        
    def iknow(cliente_socket,word):
        menssagem =  f'aprendido,{word}'
        cliente_socket.send(menssagem.encode())
   
    def resetarrevise(cliente_socket):
        menssagem = f'resetrevise'
        cliente_socket.send(menssagem.encode())   
        
    def edit(cliente_socket,temp):
        mensagem = f'edit,{temp[0]},{temp[1]},{temp[2]}'
        cliente_socket.send(mensagem.encode())
    
    def adicionou(cliente_socket,palavra,traducao):
        mensagem = f"adicionar,{palavra},{traducao}"
        cliente_socket.send(mensagem.encode())    
        
    def lista_edit(cliente_socket):
        mensagem = f'lista_edit'
        cliente_socket.send(mensagem.encode()) 
        tamanho_bytes = cliente_socket.recv(4)
        tamanho = struct.unpack('!I', tamanho_bytes)[0]
        data = b""
        while len(data) < tamanho:
            data += cliente_socket.recv(tamanho - len(data))   
        return pickle.loads(data) 

    def acessar_mensagem(cliente_socket):
        menssagem =  f'acessar_mensagens'
        cliente_socket.send(menssagem.encode())
        recebido = cliente_socket.recv(1024)
        return pickle.loads(recebido)

    def acessar_mensagem_revise(cliente_socket):
        mensagem = f'acessar_mensagens_revise'
        cliente_socket.send(mensagem.encode())
        recebido = cliente_socket.recv(1024)
        return pickle.loads(recebido) 

class Ui_Main:
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)
        
        self.QtStack = QtWidgets.QStackedLayout()
        
        self.telas = {
            'tela_inicial': QtWidgets.QWidget(),
            'tela_know': QtWidgets.QWidget(),
            'tela_lets_try': QtWidgets.QWidget(),
            'tela_add_word': QtWidgets.QWidget(),
            'tela_revise': QtWidgets.QWidget(),
            'tela_edit': QtWidgets.QWidget(),
        }        
    
        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.telas['tela_inicial'])

        self.movie = QMovie("C:\\Users\\gabri\\Desktop\\download.gif")
        self.tela_inicial.label.setMovie(self.movie)
        self.movie.start()

        self.tela_know = Tela_Know()
        self.tela_know.setupUi(self.telas['tela_know'])
        
        self.tela_revise = Revise()
        self.tela_revise.setupUi(self.telas['tela_revise'])
        
        self.tela_lets_try = Ui_lets_Try()
        self.tela_lets_try.setupUi(self.telas['tela_lets_try'])
        
        self.tela_add_word = Tela_Add_Word()
        self.tela_add_word.setupUi(self.telas['tela_add_word'])

        self.tela_edit = tela_edit()
        self.tela_edit.setupUi(self.telas['tela_edit'])
        
        for tela in self.telas.values():
            self.QtStack.addWidget(tela)

class Main(QMainWindow):
    def __init__(self,cliente_socket):
        super(Main, self).__init__(None)
        self.cliente_socket = cliente_socket
        
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        #tela Know lambda:self.abrirTela('cadastro')()
        self.ui.tela_inicial.know_button.clicked.connect(lambda:self.abrirTela('tela_know')())
        self.ui.tela_know.lets_try.clicked.connect(lambda:self.abrirTela('tela_lets_try')())
        self.ui.tela_know.add_world.clicked.connect(lambda:self.abrirTela('tela_add_word')())
        self.ui.tela_know.revise.clicked.connect(lambda:self.abrirTela('tela_revise')())
        self.ui.tela_know.edit_world.clicked.connect(lambda:self.abrirTela('tela_edit')())
        self.ui.tela_know.pushButton.clicked.connect(self.retornar)
        
        #tela lets try
        self.ui.tela_lets_try.chet.clicked.connect(self.cheat)
        self.ui.tela_lets_try.reset.clicked.connect(self.reset)
        self.ui.tela_lets_try.i_know.clicked.connect(self.ik)
        self.ui.tela_lets_try.edit.clicked.connect(lambda:self.abrirTela('tela_edit')())
        self.ui.tela_lets_try.resposta.returnPressed.connect(self.indentifi)
        self.ui.tela_lets_try.pushButton_2.clicked.connect(self.retornar)

        #tela revise
        self.ui.tela_revise.pushButton_6.clicked.connect(self.cheat)
        self.ui.tela_revise.pushButton_5.clicked.connect(self.resetrevise)
        self.ui.tela_revise.lineEdit.returnPressed.connect(self.indentifi)
        self.ui.tela_revise.pushButton_2.clicked.connect(self.retornar)


        #tela edit
        self.ui.tela_edit.lista.itemClicked.connect(self.lista)
        self.ui.tela_edit.edicoes.returnPressed.connect(self.editar)
        self.ui.tela_edit.confirm.clicked.connect(self.retornar)

        #tela add word
        self.ui.tela_add_word.palavra.returnPressed.connect(self.desce)
        self.ui.tela_add_word.traducao.returnPressed.connect(self.adiciona_palavra)
        self.ui.tela_add_word.pushButton_2.clicked.connect(self.retornar)
    # GERAL

    def abrirTela(self, nome_tela):
        if nome_tela == 'tela_lets_try' or nome_tela == 'tela_revise':
            self.word = Cliente.acessar_mensagem(self.cliente_socket)
            self.ui.tela_lets_try.pergunta.setText(self.word[1])
            self.word1 = Cliente.acessar_mensagem_revise(self.cliente_socket)
            self.ui.tela_revise.label_2.setText(self.word1[1])
        elif nome_tela == 'tela_edit':
            if self.ui.tela_edit.lista.count() == 0:
                self.ui.tela_edit.informacoes.setText("")
                list = Cliente.lista_edit(self.cliente_socket)
                list = sorted(list, key=lambda x: x[1])
                for item in list:
                    self.ui.tela_edit.lista.addItem("%s | %s = %s" % (item[0],item[1], item[2]))
                    

        def mudar_tela():
            self.atual = nome_tela
            self.ui.QtStack.setCurrentWidget(self.ui.telas[nome_tela])
        return mudar_tela

    def retornar(self):
        if self.atual == "tela_edit" or self.atual == "tela_revise" or self.atual == "tela_add_word"or self.atual == "tela_lets_try":
            self.ui.QtStack.setCurrentWidget(self.ui.telas['tela_know'])
            self.atual = "tela_know"
        elif self.atual == "tela_know":
            self.ui.QtStack.setCurrentWidget(self.ui.telas['tela_inicial'])

    def indentifi(self):
        if self.atual == 'tela_lets_try':
            if self.word[2] == self.ui.tela_lets_try.resposta.text():
                self.ui.tela_lets_try.frame.setStyleSheet("background-color: green;")
                Cliente.incremento(self.cliente_socket,self.word[0])
            else:
                self.ui.tela_lets_try.frame.setStyleSheet("background-color: red;")
            self.word = Cliente.acessar_mensagem(self.cliente_socket)
            self.ui.tela_lets_try.pergunta.setText(self.word[1])
            self.ui.tela_lets_try.resposta.setText("")
            self.ui.tela_lets_try.label_Chet.setText("")
            self.ui.tela_lets_try.frame.show()
            QtCore.QTimer.singleShot(350, self.ui.tela_lets_try.frame.hide)
        else:
            if self.word1[2] == self.ui.tela_revise.lineEdit.text():
                self.ui.tela_revise.frame.setStyleSheet("background-color: green;")
                Cliente.incremento(self.cliente_socket,self.word1[0])
            else:
                self.ui.tela_revise.frame.setStyleSheet("background-color: red;")
            self.word1 = Cliente.acessar_mensagem_revise(self.cliente_socket)
            self.ui.tela_revise.label_2.setText(self.word1[1])
            self.ui.tela_revise.label_Chet.setText("")
            self.ui.tela_revise.lineEdit.setText("")
            self.ui.tela_revise.frame.show()
            QtCore.QTimer.singleShot(350, self.ui.tela_revise.frame.hide)

    def cheat(self):
        if self.atual == "tela_lets_try":
            self.ui.tela_lets_try.label_Chet.setText(self.word[2])
            self.ui.tela_lets_try.label_Chet.setStyleSheet("color: white;")  
        else:
            self.ui.tela_revise.label_Chet.setText(self.word1[2])
            self.ui.tela_revise.label_Chet.setStyleSheet("color: white;")  

    #TELA EDIT WORD
    def lista(self,item):
        self.ui.tela_edit.informacoes.setText(item.text())

    def editar(self):
        partes = [parte.strip() for parte in self.ui.tela_edit.edicoes.text().replace('|', '').replace('=', '').split()]
        Cliente.edit(self.cliente_socket,partes)
        self.ui.tela_edit.edicoes.setText("")
        self.ui.tela_edit.lista.clear()
        list = Cliente.lista_edit(self.cliente_socket)
        list = sorted(list, key=lambda x: x[1])
        for item in list:
            self.ui.tela_edit.lista.addItem("%s | %s = %s" % (item[0],item[1], item[2]))
        self.ui.tela_edit.informacoes.setText("%s | %s = %s" % (partes[0],partes[1],partes[2]))



    # TELA LETS TRY
    def reset(self):
        Cliente.resetar(self.cliente_socket)
        
    def ik(self):
        print(self.word[1])
        Cliente.iknow(self.cliente_socket, self.word[1])
        print(f"palavra aprendidda: {self.word[1]}")
        
        
    # TELA REVISE
    def resetrevise(self):
        Cliente.resetarrevise(self.cliente_socket)


    # TELA ADD WORD
    
    def desce(self):
        self.ui.tela_add_word.traducao.setFocus()
        
    def adiciona_palavra(self):
        Cliente.adicionou(self.cliente_socket,self.ui.tela_add_word.palavra.text(),self.ui.tela_add_word.traducao.text())
        self.ui.tela_add_word.palavra.setText("")
        self.ui.tela_add_word.traducao.setText("")

if __name__ == '__main__':
    cliente = Cliente('localhost', 8007)
    cliente.conectar_servidor() 