# Sistema de hotelaria: Hotel e hóspede
# Crud Check
# Create; Read - all. / code.; Update; Delete;
# Validações - implementar

import sqlite3 #biblioteca do sqlite
from time import sleep
# import de funções e arquivos
import funcs.hospede, funcs.hotel, funcs.formatacao

def main():
    escolha_Inicial()

# função para escolha inicial do caminho a ser realizado pelo usuário(funcionário do estabelecimento) - Funciona como um switch case
def escolha_Inicial():
    funcs.formatacao.colocarLinhas()
    escolhaInicial = input("Olá, tudo bem! Seja bem-vindo ao sistema de hotelaria barata:\n\nO que deseja fazer?\n1 - Hotel\n2 - Cliente\n3 - Encerrar\nOpção desejada: ---> ")
    if escolhaInicial == "1":
        sleep(1)
        funcs.hotel.escolhaHotel()
    elif escolhaInicial == "2":
        sleep(1)
        funcs.hospede.escolhaHospede()
    elif escolhaInicial == "3":
        print("Obrigado por usar nossos serviços, iremos encerrar o programa")
        sleep(1)
        quit()
    else:
        # escolhaInicial() -- validar
        print("Insira novamente, opção inválida!!")
        sleep(1)
        escolha_Inicial()

if __name__ == "__main__":
    main()