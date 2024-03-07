#Imprimindo a mensagem na tela do usuário.
print('Quer saber quantos segundos se passaram depois da meia noite até a última hora?')
#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário.
hora = int(input("Coloque aqui a hora atual:"))
#Fazendo os calcúlos.
minuto = hora*60
segundo = minuto*60
#Imprimindo a data formatada na ordem certa.
print('Segundos que se passaram depois da meia noite até a hora recente:', segundo)