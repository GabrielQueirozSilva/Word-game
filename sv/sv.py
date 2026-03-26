import mysql.connector as mysql
import socket
import threading
import pickle
import random
import struct
import os
from dotenv import load_dotenv

load_dotenv()

class Cadastro:
    def __init__(self, host=None, database=None, user=None, password=None):
        self.host     = host     or os.getenv("MYSQL_HOST")
        self.database = database or os.getenv("MYSQL_DATABASE")
        self.user     = user     or os.getenv("MYSQL_USER")
        self.password = password or os.getenv("MYSQL_PASSWORD")

    def _conectar(self, database=True):
        """Centraliza a criação da conexão."""
        params = dict(host=self.host, user=self.user, password=self.password)
        if database:
            params["database"] = self.database
        return mysql.connect(**params)

    def adicionar(self, palavra, traducao):
        self.de_cria()
        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("SELECT * FROM palavras WHERE Traducao = %s and Palavra = %s", (traducao, palavra))
        if cursor.fetchall():
            print("Palavra já presente no banco de dados!!")
        else:
            cursor.execute('INSERT INTO palavras (palavra,traducao,pontos,aprendido) VALUES (%s,%s,%s,%s)', (palavra, traducao, 0, 0))
            conect.commit()
        cursor.close()
        conect.close()

    def editar(self, id, palavra, traducao):
        self.de_cria()
        conect = self._conectar()
        cursor = conect.cursor()
        if palavra != '_':
            cursor.execute('UPDATE palavras SET palavra = %s WHERE id = %s', (palavra, id))
        if traducao != '_':
            cursor.execute('UPDATE palavras SET traducao = %s WHERE id = %s', (traducao, id))
        conect.commit()
        cursor.close()
        conect.close()

    def de_cria(self):
        conect = self._conectar(database=False)
        cursor = conect.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS servidor")
        cursor.close()
        conect.close()

        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS palavras(
                id integer PRIMARY KEY AUTO_INCREMENT,
                Palavra text NOT NULL,
                Traducao text NOT NULL,
                pontos INT NOT NULL,
                aprendido INT NOT NULL
            )
        """)
        conect.commit()
        cursor.close()
        conect.close()

    def acessar_mensagens(self):
        self.de_cria()
        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("SELECT * FROM palavras WHERE aprendido = 0")
        resultado = cursor.fetchall()
        cursor.close()
        conect.close()
        random.shuffle(resultado)
        return min(resultado, key=lambda tupla: tupla[3])[0:3]

    def acessar_mensagens_revise(self):
        self.de_cria()
        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("SELECT * FROM palavras WHERE aprendido = 1")
        resultado = cursor.fetchall()
        cursor.close()
        conect.close()
        random.shuffle(resultado)
        return min(resultado, key=lambda tupla: tupla[3])[0:3]

    def incremento(self, id):
        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("SELECT pontos FROM palavras WHERE id = %s", (id,))
        ponto = cursor.fetchone()[0]
        cursor.execute("UPDATE palavras SET pontos = %s WHERE id = %s", (ponto + 1, id))
        conect.commit()
        cursor.close()
        conect.close()

    def aprendido(self, palavra):
        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("SELECT id FROM palavras WHERE palavra = %s", (palavra,))
        result = cursor.fetchone()
        cursor.execute("UPDATE palavras SET aprendido = 1 WHERE id = %s", (result[0],))
        conect.commit()
        cursor.close()
        conect.close()

    def resettrys(self):
        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("UPDATE palavras SET pontos = 0 WHERE aprendido = 0")
        conect.commit()
        cursor.close()
        conect.close()

    def resetrevise(self):
        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("UPDATE palavras SET pontos = 0 WHERE aprendido = 1")
        conect.commit()
        cursor.close()
        conect.close()

    def lista_edit(self):
        conect = self._conectar()
        cursor = conect.cursor()
        cursor.execute("SELECT id, Palavra, Traducao FROM palavras")
        result = cursor.fetchall()
        cursor.close()
        conect.close()
        return result
        
            
def server(con):

    """
    Função utilizada para atender a comunicação com clientes.

    A função em questao faz a utilização da classe cadastro, ela recebe mensagens enviadas pelo cliente
    e faz a comparação delas em varios ifs e elifs dentro de um while true para poder receber varios clientes
    e funcionar indenpendetemente, caso não encontre um caso ela da pass e nao faz nada,
    cada if compara a mensagem enviada pelo cliente e caso se encaixe entra em uma função especifica da 
    classe cadastro e realiza uma ação especifica no banco de dados enviado os resultados dessa ação novamente
    para o cliente.

    Parameters
    ----------
    con : socket
        O objeto de soquete que representa a conexão com o cliente.

    Raises
    ------
    Exception
        Qualquer exceção que ocorra durante a execução das comparações antes ditas.

    """


    x = True
    print(f"Cliente se conectou")
    cadastro = Cadastro()

    while x:
        try:

            recebe = con.recv(1024)
            mensagem = recebe.decode() 
            comando = mensagem.split(',')

            if comando[0] == 'bye' or comando[0] == '' or comando[0] == None:
                print("cliente desconectado")
                x = False    
            
            elif comando[0] == 'adicionar':
                cadastro.adicionar(comando[1],comando[2])
                
            elif comando[0] == "incremento":
                cadastro.incremento(comando[1])
                
            elif comando[0] == "aprendido":
                cadastro.aprendido(comando[1])
                                
            elif comando[0] == "resettry":
                cadastro.resettrys()
                                
            elif comando[0] == "resetrevise":
                cadastro.resetrevise()
                
            elif comando[0] == "edit":
                cadastro.editar(comando[1],comando[2],comando[3])
                
            elif comando[0] == "lista_edit":
                a = pickle.dumps(cadastro.lista_edit())
                tamanho = struct.pack('!I', len(a))  # Tamanho da mensagem (4 bytes)
                con.sendall(tamanho + a)
                
            elif comando[0] == 'acessar_mensagens':
                a = pickle.dumps(cadastro.acessar_mensagens()) 
                con.send(a)
            
            elif comando[0] == 'acessar_mensagens_revise':
                a = pickle.dumps(cadastro.acessar_mensagens_revise()) 
                con.send(a)
                
            elif x:
                pass
            
        except Exception as e:
            print(f"Erro na comunicação: {e}")
            break
        
    con.close()

def main():
    host = ''
    port = 8007
    addr = (host, port)
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen(10)
    print('Aguardando conexões...')

    while True:
        con, addr = serv_socket.accept() 
        client_thread = threading.Thread(target=server, args=(con,))
        client_thread.start()
        
if __name__ == "__main__":
    main()