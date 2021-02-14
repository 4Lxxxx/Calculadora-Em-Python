# Calculadora em PY , feita por mim ;-;
def calculate():
    operação = input('''
Informe a operação para ser realizada:
+ adição
- subtração
* multiplicação
/ divisão
''')

    numero_1 = int(input('Informe o primeiro numero: '))
    numero_2 = int(input('Informe o segundo numero: '))
    
    if operação == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operação == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operação == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operação == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('Informe uma operação valida!')

    
    again()

def again():
    calcular_novamente = input('''
Gostaria de calcular novamente? 
Sim(S) ou Não(N)
''')

    if calcular_novamente.upper() == 'S':
        calculate()
    elif calcular_novamente.upper() == 'N':
        print('By: 4Lxxxx')
    else:
        again()

calculate()

input()