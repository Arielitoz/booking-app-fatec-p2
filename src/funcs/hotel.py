import funcs.formatacao, main, sys, time
# import time, sys, sqlite3, main, datetime

# conn = sqlite3.connect("hotel.db")
# cur = conn.cursor()

# função para escolha na rota HOTEL realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolha_Hotel():
    try:
        funcs.formatacao.colocarLinhas()
        escolhaHotel = input("FHA - Gerenciamento do hotel , temos:\n\n1 - Verificar quartos(Read-all)\n2 - Verificar quarto N°(Read - Id)\n3 - Cadastrar Quarto(Create)\n4 - Atualizar quarto: (Update)\n5 - Remover um quarto(Delete)\n6 - Voltar à escolha anterior\n7 - Encerrar\nInsira uma opção: ---> ")

        match escolhaHotel:
            case "1":
                escolha_Hotel()
            case "2":
                escolha_Hotel()
            case "3":
                escolha_Hotel()
            case "4":
                escolha_Hotel()
            case "5":
                escolha_Hotel()
            case "6":
                main.main()
            case "7":
                print("Obrigado por usar os serviços FHA, encerrando o programa. :)")
                time.sleep(1)
                # conn.close()
                sys.exit()
            case _:
                print("Opção inválida, insira novamente:")
                time.sleep(1)
                escolha_Hotel()

    except KeyboardInterrupt:
        print("\nEncerrando o programa, FHA agradece. ;)")
        time.sleep(1)
        # conn.close()
        sys.exit()

# função para cadastro de quarto 
# def cadastrar_Quarto():
#     print("\nVamos cadastrar uma reserva de")
#     numeroQuarto = input("Insira o n° do quarto")
#     qtdTotalQuartos = input("N° de pessoas junto ao hóspede") # default number
#     qtdDisponivel = input("Qual o número do quarto")
#     diarias = input("Insira a quantidade de dias")
#     formaPagamento = input("Insira C - crédito; D - Débito; P - Pix")
#     dataCheckIn = input("Insira o dia")

#     #Enviar instrução a ser executada pelo sqlite
#     conn.execute("insert into HOSPEDE values(?,?,?,?,?,?,?)", (nomeHospede, qtdPessoas,quartoAlugado, diarias, formaPagamento, dataCheckIn, dataCheckOut));
#     conn.commit()

def iniciar_Login():
    try:
        funcs.formatacao.colocarLinhas()
        print("\nIniciando Sistema...")
        time.sleep(1)
        usuario = input("\nInsira seu login de usuário: ")
        senhaUsuario = input("\nInsira sua senha: ")

        if usuario == "fatecsegna2" and senhaUsuario == "fatec4242":
            print("Você tem acesso de admin")
            time.sleep(1)
            escolha_Hotel()
        else:
            print("\nVocê não tem acesso de administrador")
            time.sleep(1)
            main.main()
    except KeyboardInterrupt:
        print("\nEncerrando o programa, FHA agradece. ;)")
        time.sleep(1)
        # conn.close()
        sys.exit()
