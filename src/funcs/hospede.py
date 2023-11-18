import funcs.formatacao
import time, sys, sqlite3, main, datetime, os

db_path = os.path.join(os.path.dirname(__file__), "..", "hotel.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# função para escolha na rota HÓSPEDE realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolha_Hospede():
    try:
        funcs.formatacao.colocarLinhas()
        escolhaHospede = input("FHA - Gerenciamento do hóspede , temos:\n\n1 - Verificar reservas(Read-all)\n2 - Verificar reserva N°(Read - Id)\n3 - Cadastrar hóspede(Create)\n4 - Atualizar hóspede: (Update)\n5 - Remover/Checkout hóspede(Delete)\n6 - Voltar à escolha anterior\n7 - Encerrar\nInsira uma opção: ---> ")
    
        match escolhaHospede:
            case "1":
                print("oi")
            case "2":
                print("oi2")
            case "3":
                cadastrar_Hospede()
            case "4":
                print("oi4")
            case "5":
                deletar_Hospede()
            case "6":
                main.main()
            case "7":
                print("Obrigado por usar os serviços FHA, encerrando o programa. :)")
                time.sleep(1)
                sys.exit()
            case _:
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
        funcs.formatacao.formatacaoCreate()
        print("Reserva Hóspede:")
        idhospede = None
        nomeHospede = input("\nNome do hóspede: ")
        qtdPessoas = input("N° de pessoas no quarto: ") # validar n°
        numeroQuartoAlugado = input("N° do quarto: ")
        diarias = input("Quantidade de diárias: ")
        print("Check-In realizado no dia: " + str(datetime.datetime.now()))
        currentdate = datetime.datetime.today()
        dataCheckIn = currentdate.date() # formato data ex: 2023-11-17 (YYYY-MM-DD)
        formaPagamento = ""
        # while formaPagamento.upper() != 'C' and formaPagamento.upper() != "D" and formaPagamento.upper() != "P":
        while formaPagamento.upper() not in {'C', 'D', 'P'}:
            formaPagamento = input("\nForma de pagamento: \nC - Crédito;\nD - Débito;\nP - Pix;\n> ")
        print("Forma de pagamento aceita")
        time.sleep(1)
        print("\nReserva feita em nome de: " + nomeHospede + ", Obrigado(a)!")

    except KeyboardInterrupt:
        print("\nEncerrando o programa, FHA agradece. ;)")
        time.sleep(1)
        sys.exit()

    #Enviar instrução a ser executada pelo sqlite; try this later
    conn.execute("INSERT INTO hospede VALUES(?,?,?,?,?,?,?)", (idhospede,nomeHospede, qtdPessoas,numeroQuartoAlugado, diarias, dataCheckIn, formaPagamento));
    conn.commit()


    escolhaNovamente = input("\nDeseja cadastrar um novo hóspede: S - SIM / N - NÃO\n>  ")
    match escolhaNovamente.upper():
        case 'S':
            cadastrar_Hospede()
        case 'N':
            print("Obrigado por utilizar nossos serviços, FHA agradece.")
            conn.close()
            time.sleep(1)
            sys.exit()
        case _:
            print('\n Não foi possível entender seu desejo, obrigado')
            conn.close()
            sys.exit()

# funcão para cadastro de hóspede
def deletar_Hospede():
    print("\nVamos finalizar o Check-Out")
    time.sleep(1)
    idHospede = input("\nInsira o código do hóspede para realizar a operação: \n> ")
    time.sleep(0.5)
    # tratativa de insert
    cur.execute("Select count(*), nomeHospede, numeroQuarto from hospede where idHospede = " + idHospede)
    resCodigoDelete = cur.fetchone()
    if len(resCodigoDelete) > 1:
        print("Existe uma reserva no nome de '",resCodigoDelete[1].upper(),"'. No quarto, N°:", resCodigoDelete[2])
        validarExclusao = input("\nDeseja finalizar o Check-Out? \nS- Sim; N - Não\n> ")

        if validarExclusao.upper() == "S":
            cur.execute("Delete from hospede where idHospede = " + idHospede)
            conn.commit()
            time.sleep(0.5)
            print("\nCheck-out realizado com sucesso;")
            time.sleep(0.5)
        # conn.close()
        escolha_Hospede()
    else: 
        print("Nenhuma reserva foi identificada!")
        escolha_Hospede()