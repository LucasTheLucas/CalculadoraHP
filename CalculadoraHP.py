'''
CalculadoraHP.py
Aluno: Lucas Novaes Dias
Data: 11/05/2024

Esta tarefa representa uma calculadora de estilo HP
'''
#Aqui eu defini as 3 variaveis que vou utilizar!
numero = 0
operador = ""
finalizou = False

#Primeiramente dou bem-vindas ao usuario e digo a ele que isso é uma calculadora!
print("Bem-Vindo a calculadora HP 2000™")

#Após isso peço ao usuario para que ele digite o primeiro número da conta!
numero = float(input("Digite um valor: "))

#Depois que o valor for inserido entramos no laço While, esse laço foi escolhido devido não sabermos quantas vezes o usúario vai adicionar operaçoes ao número!
while finalizou == False:

    #Aqui o usuario vai digitar o operador ou se vai finalizar!
    operador = (input("Digite que operação vai fazer com esse número:\n1.+\n2.-\n3./\n4.*\nX.[FINALIZAR]\n\nDigite a opção: ")).upper()

    #Com o operador digitado dependendo do que foi inserido nele um desses casos vai ocorrer
    #Do 1 ao 4 sera pedido mais um número e o resultado sera guardado na variavel soma e então sera mostrado a conta por extenso
    #Apos isso o usuario vai poder continuar a usar a calculadora mas se ele não quiser ele pode digitar a opção X que ira finalizar o laço While
    #Assim mostrando o resultado resultado final.
    match operador:
        case "1":
            numero_da_operação = float(input("Digite o número que vai adicionar: "))
            soma = numero + numero_da_operação
            print(f"Resultado atual de {numero} + {numero_da_operação}: {soma}\n")
            numero = soma
        case "2":
            numero_da_operação = float(input("Digite o número que vai subtrair: "))
            soma = numero - numero_da_operação
            print(f"Resultado atual de {numero} - {numero_da_operação}: {soma}\n")
            numero = soma

        case "3":
            numero_da_operação = float(input("Digite o número que vai dividir: "))
            #De todos os casos o mais diferente seria o da divisão devido ser impossivel dividir por 0 foi colocado um if
            #Caso o valor do numero_da_operação seja diferente de 0 ele prossiguira com a conta normalmente
            #Caso contrario a conta não sera feita e o usuario sera informado que é impossivel dividir por 0

            if numero_da_operação != 0:
                soma = numero / numero_da_operação
                print(f"Resultado atual de {numero} / {numero_da_operação}: {soma}\n")
                numero = soma
            
            else:
                print("[NÃO É POSSÍVEL DIVIDIR POR ZERO]")

        case "4":
            numero_da_operação = float(input("Digite o número que vai multiplicar: "))
            soma = numero * numero_da_operação
            print(f"Resultado atual de {numero} * {numero_da_operação}: {soma}\n")
            numero = soma

        case "X":
            finalizou = True

#Quando sair do laço While você vera o resultado final.

print(f"O resultado é de: {numero}")
