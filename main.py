from classe import *

if __name__ == '__main__':
    nome = input('Informe o nome: ')
    idade = int(input('Informe o idade: '))
    email = input('Informe o e-mail: ')

    # instância da classe
    usuario = Pessoa(nome, idade, email)

    # saída de dados
    print(f'Nome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'E-mail: {usuario.email}.')