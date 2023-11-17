# Sistema de hotelaria: Hotel e hóspede: FHA
# Crud Check
# Create; Read - all. / code.; Update; Delete;
# Validações - implementar

# import de funções e arquivos
import funcs.hospede, funcs.hotel, funcs.formatacao, sys
from time import sleep

def main():
    escolha_Inicial()

# função para escolha inicial do caminho a ser realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolha_Inicial():
    try:
        funcs.formatacao.colocarLinhas()
        escolhaInicial = input("Bem-vindo(a) ao sistema FHA: Facilitador de Hospedagem e Acomodações:\n\nInsira um opção:\n1 - Hotel/Quartos\n2 - Hóspedes\n3 - Encerrar\nOpção desejada: ---> ")
        # match case == switch case
        match escolhaInicial:
            case '1':
                sleep(1)
                funcs.hotel.escolha_Hotel()
            case '2':
                sleep(1)
                funcs.hospede.escolha_Hospede()
            case '3':
                print("Obrigado por usar os serviços FHA, encerrando o programa. :)")
                sleep(1)
                sys.exit()
            case _:
                print("Insira novamente, opção inválida!!")
                sleep(1)
                escolha_Inicial()

    except KeyboardInterrupt:
        print("\nEncerrando o programa, FHA agradece. ;)")
        sleep(1)
        sys.exit()

if __name__ == "__main__":
    main()