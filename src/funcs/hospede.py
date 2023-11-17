import funcs.formatacao
import time
import sqlite3

conn = sqlite3.connect("hotel.db")
cur = conn.cursor()

# função para escolha na rota HÓSPEDE realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolhaHospede():
    funcs.formatacao.colocarLinhas()
    escolhaHospede = input("\nNas opções de gerenciamento do hóspede , temos:\n\n\n1 - Verificar reservas(Read-all)\n2 - Verificar reserva N°(Read - Id)\n3 - Cadastrar hóspede(Create)\n4 - Atualizar hóspede: (Update)\n5 - Remover/Checkout hóspede(Delete)\n6 - Voltar\nInsira uma opção: ---> ")
   
    if escolhaHospede == "1":
        print("oi1")
    elif escolhaHospede == "2":
        print("oi2")
    elif escolhaHospede == "3":
        cadastrarHospede()
    elif escolhaHospede == "4":
        print("oi4")
    elif escolhaHospede == "5":
        print("oi5")
    elif escolhaHospede == "6":
        print("oi6")
    else:
        print("Estamos voltando ao ínicio, obrigado!")
        quit()

def cadastrarHospede():
    nomeHospede = input("Insira o nome do hospede")
    qtdPessoas = input("N° de pessoas junto ao hóspede")
    quartoAlugado = input("Qual o número do quarto")
    diarias = input("Insira a quantidade de dias")
    formaPagamento = input("Insira C - crédito; D - Débito; P - Pix")
    dataCheckIn = input("Insira o dia")
    dataCheckOut = input("Insira a data de saída")
   
     #Enviar instrução a ser executada pelo sqlite
    conn.execute("insert into HOSPEDE values(?,?,?,?,?,?,?)", (nomeHospede, qtdPessoas,quartoAlugado, diarias, formaPagamento, dataCheckIn, dataCheckOut));
    conn.commit()