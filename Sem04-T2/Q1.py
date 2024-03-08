#Armazenando dados em uma variável
numero1 = str(input('Para saber vários cálculos entre dois números basta você digitar o primeiro número aqui:'))
#Armazenando dados em uma variável
numero2 = str(input('Agora dite o segundo número:'))
#SOMA
numero1 = int(numero1)
numero2 = int(numero2)
#SOMA 2
soma = numero1+numero2
#SOMA 3
numero1 = str(numero1)
numero2 = str(numero2)
#CONCATENAÇÃO
numero1 = (numero1)
mumero2 = (numero2)
concatenar = numero1+numero2
#CONCATENAÇÃO 2
numero1 = int(numero1)
numero2 = int(numero2)
#MULTIPLICAÇÃO
multiplicacao = numero1*numero2
#MULTIPLICAÇÃO COMO STR
numero1 = str(numero1)
multiplicastr1 = numero1*numero2
#MULTIPLICAÇÃO COMO STR 2
numero1 = int(numero1)
numero2 = str(numero2)
multiplicastr2 = numero2*numero1
#MULTIPLICAÇÃO COMO STR 3
numero2 = int(numero2)
#DIVISÃO
divisao = numero1/numero2
#DIVISÃO INTEIRA DOS NÚMEROS
divsint = numero1//numero2
#EXPONENCIAÇÃO
exponenciacao = numero1**numero2
#EXPONENCIAÇÃO 2
exponenciacao = numero2**numero1
#MÓDULO OU RESTO DA DIVISÃO
resto = numero1%numero2
#Imprimindo resultado na tela do usuário
print('SOMA:',soma)
print('CONCATENAÇÃO:',concatenar)
print('MULTIPLICAÇÃO:',multiplicacao)
print('MULTIPLICAÇÃO ENTRE STRINGS:',multiplicastr1,multiplicastr2)
print('DIVISÃO:',divisao)
print('DIVISÃO INTEIRA:',divsint)
print('EXPONENCIAÇÃO:',exponenciacao)
print('RESTO DA DIVISÃO:',resto)