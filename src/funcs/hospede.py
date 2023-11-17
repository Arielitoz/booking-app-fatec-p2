import funcs.formatacao
import time, sys, sqlite3, main, datetime

conn = sqlite3.connect("hotel.db")
cur = conn.cursor()

# função para escolha na rota HÓSPEDE realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolha_Hospede():
    try:
        funcs.formatacao.colocarLinhas()
        escolhaHospede = input("FHA - Gerenciamento do hóspede , temos:\n\n1 - Verificar reservas(Read-all)\n2 - Verificar reserva N°(Read - Id)\n3 - Cadastrar hóspede(Create)\n4 - Atualizar hóspede: (Update)\n5 - Remover/Checkout hóspede(Delete)\n6 - Voltar à escolha anterior\n7 - Encerrar\nInsira uma opção: ---> ")
    
        if escolhaHospede == "1":
            print("oi")
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
    try:
        print("Reserva Hóspede:")
        nomeHospede = input("\nNome do hóspede: ")
        qtdPessoas = input("N° de pessoas no quarto: ")
        quartoAlugado = input("N° do quarto: ")
        diarias = input("Quantidade de diárias: ")
        print("Check-In realizado no dia: " + str(datetime.datetime.now()))
        cdt = datetime.datetime.today()
        dataCheckIn = cdt.date() # formato data ex: 2023-11-17 (YYYY-MM-DD)
        #dataCheckOut = input("Insira a data de saída") provavelmente tirar esse campo
        formaPagamento = ""
        # while formaPagamento.upper() != 'C' and formaPagamento.upper() != "D" and formaPagamento.upper() != "P":
        while formaPagamento.upper() not in {'C', 'D', 'P'}:
            formaPagamento = input("\nForma de pagamento: \nC - Crédito;\nD - Débito;\nP - Pix;\n> ")
        print("Forma de pagamento aceita")

    except KeyboardInterrupt:
        print("\nEncerrando o programa, FHA agradece. ;)")
        time.sleep(1)
        sys.exit()

    #Enviar instrução a ser executada pelo sqlite; try this later
    #conn.execute("insert into HOSPEDE values(?,?,?,?,?,?,?)", (nomeHospede, qtdPessoas,quartoAlugado, diarias, formaPagamento, dataCheckIn, dataCheckOut));
    #conn.commit()