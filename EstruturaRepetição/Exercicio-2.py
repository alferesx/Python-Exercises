print('Cadastro')
usuario = input('Usuario: ')
senha = input('Senha: ')

while(usuario == senha):
    print('O usuario e senha não podem ser iguais')
    usuario = input('Usuario: ')
    senha = input('Senha: ')

print('Bem vindo')
print(usuario)
