import funcs.formatacao
import time, sys, sqlite3, main

conn = sqlite3.connect("hotel.db")
cur = conn.cursor()

# função para escolha na rota HÓSPEDE realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolha_Hospede():
    try:
        funcs.formatacao.colocarLinhas()
        escolhaHospede = input("FHA - Gerenciamento do hóspede , temos:\n\n1 - Verificar reservas(Read-all)\n2 - Verificar reserva N°(Read - Id)\n3 - Cadastrar hóspede(Create)\n4 - Atualizar hóspede: (Update)\n5 - Remover/Checkout hóspede(Delete)\n6 - Voltar à escolha anterior\n7 - Encerrar\nInsira uma opção: ---> ")
    
        if escolhaHospede == "1":
            print("oi1")
        elif escolhaHospede == "2":
            print("oi2")
        elif escolhaHospede == "3":
            cadastrar_Hospede()
        elif escolhaHospede == "4":
            print("oi4")
        elif escolhaHospede == "5":
            print("oi5")
        elif escolhaHospede == "6":
            main.main()
        elif escolhaHospede == "7":
            print("Obrigado por usar os serviços FHA, encerrando o programa. :)")
            time.sleep(1)
            sys.exit()
        else:
            print("Opção inválida, insira novamente:")
            time.sleep(1)
            escolha_Hospede()

    except KeyboardInterrupt:
        print("\nEncerrando o programa, FHA agradece. ;)")
        time.sleep(1)
        sys.exit()

# funcão para cadastro de hóspede
def cadastrar_Hospede():
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