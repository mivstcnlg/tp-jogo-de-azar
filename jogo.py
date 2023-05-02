from random import randrange

#inicializando variaveis
tentativas = 0
resp = 's'

#definindo o valor que vai ser sorteado
num = randrange(0, 10)

#iniciando o programa
print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("|                             ADIVINHE O NÚMERO                            |")
print("|━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|")
print("| REGRAS:                                                                  |")
print("| - Só poderá escolher números entre 0 e 10.                               |")
print("| - Você tem direito a apenas 5 tentativas, logo após é reiniciado o jogo. |")
print("| - Se acertar na 1° tentativa, ganha 100 pontos.                          |")
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
print("（￣▽￣）")
print("BOA SORTE!")
print("")

while resp == 's' or resp == 'S':
    while tentativas <= 5:
        chute = int(input("Escolha um número: "))

        if chute >= 0 and chute <= 10:

            if chute == num:
                print("Você acertou!")
                if tentativas == 0:
                    print("(。♡‿♡。)")
                    print("100 pontos!")
                elif tentativas == 1:
                    print("(´✪‿✪`)")
                    print("80 pontos!")
                elif tentativas == 2:
                    print("(✿ฺ。✿ฺ)")
                    print("60 pontos!")
                elif tentativas == 3:
                    print("(⌒_⌒;)")
                    print("40 pontos!")
                elif tentativas == 4:
                    print("(-’๏_๏’-)")
                    print("20 pontos!")
            else:
                print("")
                print("┏(;-_-)┛")
                print("Tente de novo!")
                tentativas = tentativas + 1
            
            if tentativas > 4:
                print("")
                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■100%")
                print("Voce chegou no limite de tentativas")
                print("")
                resp = input("Deseja jogar novamente? S/N: ")
                if resp == 's' or resp == 'S':
                    tentativas = 0
                    num = randrange(0, 10)
            elif chute == num:
                tentativas = 6
                print("")
                resp = input("Deseja jogar novamente? S/N: ")
                if resp == 's' or resp == 'S':
                    tentativas = 0
                    num = randrange(0, 10)
        else:
            print("")
            print("【・_・?】")
            print("Digite um número valido!")   