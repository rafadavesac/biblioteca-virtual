# Menu principal

print('Bem vindo(a) a Biblioteca Virtual!')

comando = 0

while comando != 5:

    comando = int(input('O que você deseja fazer?\n'
                        '1.Se cadastrar\n'
                        '2.Retirar um livro\n'
                        '3.Devolver um livro\n'
                        '4.Alguma outra coisa\n'
                        '5.Sair\n'))

    if comando == 1:
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        email = input("Digite seu email: ")
        print('Seu cadastro está completo!')
