# função que compara o valor da string e retorna o valor em true e false
def vogal(caractere):
    return caractere.upper() in 'AEIOU'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    caractere = input('Digite um caractere para saber se é verdadeiro ou falso:')
    # imprimindo o resultado na tela do computador do usuário
    print(f'Seu caractere é: {vogal(caractere)}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()