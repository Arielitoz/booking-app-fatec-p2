import funcs.formatacao
import time, sys, sqlite3, main, datetime, os

db_path = os.path.join(os.path.dirname(__file__), "..", "hotel.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

resCodigo = None
idhospede = None

# função para escolha na rota HÓSPEDE realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolha_Hospede():
    try:
        funcs.formatacao.colocarLinhas()
        escolhaHospede = input("FHA - Gerenciamento do hóspede , temos:\n\n1 - Verificar todas as reservas\n2 - Verificar reserva\n3 - Cadastrar/Checkin hóspede\n4 - Alteração de cadastro do hóspede:\n5 - Remover/Checkout hóspede\n6 - Verificar quartos disponíveis\n7 - Voltar à escolha anterior\n8 - Encerrar\nInsira uma opção: ---> ")
    
        match escolhaHospede:
            case "1":
                recuperar_Hospedes()
            case "2":
                recuper_HospedeId()
            case "3":
                cadastrar_Hospede()
            case "4":
                alterar_Hospede()
            case "5":
                deletar_Hospede()
            case "6":
                verificar_Quartos()
            case "7":
                main.main()
            case "8":
                print("Obrigado por usar os serviços FHA, encerrando o programa. :)")
                time.sleep(1)
                conn.close()
                sys.exit()
            case _:
                print("Opção inválida, insira novamente:")
                time.sleep(1)
                escolha_Hospede()

    except KeyboardInterrupt:
        print("\nEncerrando o programa, FHA agradece. ;)")
        time.sleep(1)
        conn.close()
        sys.exit()

# funcão para cadastro de hóspede - create
def cadastrar_Hospede():
    try:
        funcs.formatacao.formatacaoFHA()
        print("Reserva Hóspede:")
        
        time.sleep(1)
        # Solicita o nome do hóspede e valida se são dois nomes com letras maiúsculas
        while True:
            time.sleep(0.5)
            nomeHospede = input("\nNome do hóspede (Nome e Sobrenome iniciados com letra maiúscula, separados por espaço).\n Exemplo: Ronaldinho Neymar\n>  ")
            partes_do_nome = nomeHospede.split()
            
            time.sleep(0.5)
            if not usuario_Dados(partes_do_nome) and (len(partes_do_nome) == 2 and partes_do_nome[0].istitle() and partes_do_nome[1].istitle() and len(nomeHospede)):
                break
            else:
                time.sleep(0.5)
                print("Formato incorreto, Digite novamente.")
        while True:  
            time.sleep(0.5)
            qtdPessoas = input("N° de pessoas no quarto: ")
            time.sleep(0.5)
            if qtdPessoas.upper() in {'1', '2', '3','4','5','6'}:
                break
            else:
                time.sleep(0.5)
                print("A capacidade é de até 6 pessoas por quarto. Digite novamente.")
        while True:
            numeroQuartoAlugado = input("N° do quarto: ")
            if numeroQuartoAlugado.isdigit() and 1 <= int(numeroQuartoAlugado) <= 20:
                break
            else:
                cur.execute("SELECT COUNT(*) FROM hospede;")
                resCodigo = cur.fetchone()
                print(f"Temos 20 quartos no total, disponível no momento: {20 - resCodigo[0]} quartos. Digite novamente.")
        # nomeHospede = input("\nNome do hóspede: ")
        # qtdPessoas = input("N° de pessoas no quarto: ") # validar n°
        # numeroQuartoAlugado = input("N° do quarto: ")
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
        conn.close()
        sys.exit()

    #Enviar instrução a ser executada pelo sqlite; try this later
    conn.execute("INSERT INTO hospede VALUES(?,?,?,?,?,?,?)", (idhospede,nomeHospede, qtdPessoas,numeroQuartoAlugado, diarias, dataCheckIn, formaPagamento));
    conn.commit()


    escolhaNovamente = input("\nDeseja cadastrar um novo hóspede: S - SIM / N - NÃO\n>  ")
    match escolhaNovamente.upper():
        case 'S':
            cadastrar_Hospede()
        case 'N':
            time.sleep(1)
            escolha_Hospede()
            # print("Obrigado por utilizar nossos serviços, FHA agradece.")
            # conn.close()
            # time.sleep(1)
            # sys.exit()

# funcão para deeltar registro de hóspede(delete)
def deletar_Hospede():
    print("\nVamos finalizar o Check-Out")
    time.sleep(1)
    # validação campos
    idHospede = input("\nInsira o código do hóspede para realizar a operação: \n> ")
    time.sleep(0.5)

    cur.execute("Select count(*), nomeHospede, numeroQuarto from hospede where idHospede = " + idHospede)
    resCodigo = cur.fetchone()
    if resCodigo[0] == 1:
        print("Existe uma reserva no nome de '",resCodigo[1].upper(),"'. No quarto, N°:", resCodigo[2])
        validarExclusao = input("\nDeseja finalizar o Check-Out? \nS- Sim; N - Não\n> ")

        if validarExclusao.upper() == "S":
            cur.execute("Delete from hospede where idHospede = " + idHospede)
            conn.commit()
            time.sleep(0.5)
            print("\nCheck-out realizado com sucesso;")
            time.sleep(0.5)
       
        escolha_Hospede()
    else:
        time.sleep(0.5)
        print("Nenhuma reserva foi identificada!")
        time.sleep(0.5)
        escolha_Hospede()

# função para alterar(update) os dados do  banco de dados - Alterar um registro, campo do banco de dados
def alterar_Hospede():
    print("\nAlteração de reserva:")
    time.sleep(1)
    # validação campos
    idHospede = input("\nInsira o código do hóspede para realizar a operação: \n> ")
    time.sleep(0.5)
    cur.execute("Select count(*), nomeHospede, numeroQuarto,qtdDiarias, formaPagamento from hospede where idHospede = " + idHospede)
    resCodigo = cur.fetchone()
    if resCodigo[0] == 1:
        print("\nExiste uma reserva no nome de '",resCodigo[1].upper(),"'. No quarto, N°:", resCodigo[2], ".\nQuantidade de diárias: ", resCodigo[3], ". Forma de Pagamento: ", resCodigo[4].upper())
        time.sleep(0.5)
        escolhaAlteracao = input('\nO que deseja alterar: \n1 - Nome; \n2 - N°Quarto;\n3 - Diárias;\n4 - Forma de Pagamento\n> ')
        match escolhaAlteracao:
            case '1':
                while True:
                    nomeHospede = input("\nNome do hóspede (Nome e Sobrenome iniciados com letra maiúscula, separados por espaço).\n Exemplo: Ronaldinho Neymar\n>  ")
                    partes_do_nome = nomeHospede.split()
                    if not usuario_Dados(partes_do_nome) and (len(partes_do_nome) == 2 and partes_do_nome[0].istitle() and partes_do_nome[1].istitle() and len(nomeHospede)):
                        break
                    else:   
                        time.sleep(0.5)
                        print("Formato incorreto, Digite novamente.")
                time.sleep(0.5)
                conn.execute("UPDATE hospede SET nomeHospede = ? WHERE idHospede = ?;", (nomeHospede,idHospede));
                conn.commit()
                time.sleep(0.5)
                print("\nAlteração concluída!")
                time.sleep(0.5)
                escolha_Hospede()
            case '2':
                while True:
                    time.sleep(0.5)
                    numeroQuarto = input("Insira a atualização referente ao número de quartos: ")
                    time.sleep(0.5)
                    if numeroQuarto.upper() in {'1', '2', '3','4','5','6'}:
                        break
                    else:
                        time.sleep(0.5)
                        print("A capacidade é de até 6 pessoas por quarto. Digite novamente.")
                    conn.execute("UPDATE hospede SET numeroQuarto = ? WHERE idHospede = ?;", (numeroQuarto,idHospede));
                    conn.commit()
                    time.sleep(0.5)
                    print("\nAlteração concluída!")
                    time.sleep(0.5)
                    escolha_Hospede()
            case '3':
                qtdDiarias = input("Insira a atualização referente ao número de diárias: ")
                time.sleep(0.5)
                conn.execute("UPDATE hospede SET qtdDiarias = ? WHERE idHospede = ?;", (qtdDiarias,idHospede));
                conn.commit()
                time.sleep(0.5)
                print("\nAlteração concluída!")
                time.sleep(0.5)
                escolha_Hospede()
            case '4':
                formaPagamento = ""
                while formaPagamento.upper() not in {'C', 'D', 'P'}:
                    formaPagamento = input("\nForma de pagamento: \nC - Crédito;\nD - Débito;\nP - Pix;\n> ")
                print("Forma de pagamento aceita")
                time.sleep(0.5)
                conn.execute("UPDATE hospede SET formaPagamento = ? WHERE idHospede = ?;", (formaPagamento,idHospede));
                conn.commit()
                time.sleep(0.5)
                print("\nAlteração concluída!")
                time.sleep(0.5)
                escolha_Hospede()
            case _:
                print("Opção inválida, insira novamente:")
                time.sleep(1)
                alterar_Hospede()
                
    else:
        time.sleep(0.5)
        print("Nenhuma reserva foi identificada!")
        time.sleep(0.5)
        escolha_Hospede()

# função para recuperar(read) os dados do  banco de dados - todos os registros
def recuperar_Hospedes():
    time.sleep(0.5)
    print("\nRecuperando registros em nossa base de dados: ")
    time.sleep(0.5)

    cur.execute("Select idHospede, nomeHospede, numeroQuarto, checkIn from hospede")
    resCodigo = cur.fetchall()

    if len(resCodigo) >  0:

        print("\nRegistros encontrados: ")
        for registros in resCodigo:
            funcs.formatacao.formatacaoFHA()
            print("\nRegistro Hóspede[Id]: ", registros[0])
            print("\nNome Completo:", registros[1].upper())
            print("N° do Quarto:" , registros[2])
            print("Check-In realizado na data:", registros[3]);
            funcs.formatacao.formatacaoFHA()
            time.sleep(0.5)

        print("\nForam encontrados um total de:" , len(resCodigo), "registro(s)  em nossa base;")
        time.sleep(0.5)
        print('\nVoltando às opções:')
        time.sleep(3)
        escolha_Hospede()
    else:
        print("\nNenhum registro encontrado em nossa base, FHA agradece")
        time.sleep(1)
        escolha_Hospede()

# função para recuperar(read) os dados do  banco de dados - registro único
def recuper_HospedeId():
    time.sleep(0.5)
    # validação campos
    idHospede = input("\nInsira o código do hóspede para buscar um registro: \n> ")
    time.sleep(0.5)

    cur.execute("Select count(*), idHospede, nomeHospede, numeroQuarto, checkIn from hospede where idHospede = " + idHospede)
    resCodigo = cur.fetchone()
    if (int(idHospede)) < 0 :
        print("O valor não pode ser negativo , insira novamente")
        recuper_HospedeId()
    if resCodigo[0] > 0:
        time.sleep(0.5)
        print("\nRegistro encontrado: ")
        funcs.formatacao.formatacaoFHA()
        print("\nRegistro Hóspede[Id]: ", resCodigo[1])
        print("\nNome Completo:", resCodigo[2].upper())
        print("N° do Quarto:" , resCodigo[3])
        print("Check-In realizado na data:", resCodigo[4]);
        funcs.formatacao.formatacaoFHA()
    else:
        print("\nNenhum registro encontrado em nossa base, FHA agradece")
        time.sleep(1)
        escolha_Hospede()
        
    time.sleep(1)
    escolha_Hospede()

def usuario_Dados(nome):
    return any(not char.isalnum() for char in nome) or any(char.isdigit() for char in nome)

def verificar_Quartos():
    time.sleep(0.5)
    print("\nRecuperando quartos em nossa base de dados: ")
    time.sleep(0.5)

    cur.execute("Select idHospede, numeroQuarto, checkIn from hospede")
    resCodigo = cur.fetchall()

    if len(resCodigo) >  0:

        print("\nRegistros encontrados: ")
        for registros in resCodigo:
            funcs.formatacao.formatacaoFHA()
            print("\nRegistro Hóspede[Id]: ", registros[0])
            print("N° do Quarto:" , registros[1])
            print("Check-In realizado na data:", registros[2]);
            funcs.formatacao.formatacaoFHA()
            time.sleep(0.5)

        print("\nForam encontrados um total de:" , len(resCodigo), "quartos(s)  em nossa base;")
        print("\nSendo eles: ")
        for registros in resCodigo:
            time.sleep(0.5)
            print("\nQuarto(s) Ocupado(s): N° ", registros[1])
        time.sleep(0.5)
        print('\nVoltando às opções:')
        time.sleep(3)
        escolha_Hospede()
    else:
        print("\nNenhum registro encontrado em nossa base, FHA agradece")
        time.sleep(1)
        escolha_Hospede()