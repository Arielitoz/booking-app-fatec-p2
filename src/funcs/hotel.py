import funcs.formatacao
import time
import sqlite3

conn = sqlite3.connect("hotel.db")
cur = conn.cursor()

# função para escolha na rota HOTEL realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolhaHotel():
    funcs.formatacao.colocarLinhas()
    escolhaHotel = input("\nNas opções de gerenciamento do hotel , temos:\n\n\n1 - Verificar quartos(Read-all)\n2 - Verificar quarto N°(Read - Id)\n3 - Cadastrar Quarto(Create)\n4 - Atualizar quarto: (Update)\n5 - Remover um quarto(Delete)\n6 - Voltar\nInsira uma opção: ---> ")
   
    if escolhaHotel == "1":
        print("oi1")
    elif escolhaHotel == "2":
        print("oi2")
    elif escolhaHotel == "3":
        cadastrarQuarto()
    elif escolhaHotel == "4":
        print("oi4")
    elif escolhaHotel == "5":
        print("oi5")
    elif escolhaHotel == "6":
        print("oi6")
    else:
        print("Estamos voltando ao ínicio, obrigado!")
        quit()

# função para cadastro de quarto 
def cadastrarQuarto():
    numeroQuarto = input("Insira o n° do quarto")
    qtdTotalQuartos = input("N° de pessoas junto ao hóspede") # default number
    qtdDisponivel = input("Qual o número do quarto")
    diarias = input("Insira a quantidade de dias")
    formaPagamento = input("Insira C - crédito; D - Débito; P - Pix")
    dataCheckIn = input("Insira o dia")

    #Enviar instrução a ser executada pelo sqlite
    conn.execute("insert into HOSPEDE values(?,?,?,?,?,?,?)", (nomeHospede, qtdPessoas,quartoAlugado, diarias, formaPagamento, dataCheckIn, dataCheckOut));
    conn.commit()