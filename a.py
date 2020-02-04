import b
import time

arq = 'teste.txt'
if not b.arqExiste(arq):
    b.criarArq(arq)

while True:
    r = b.menu(['Pessoas Cadastradas','Cadastrar Pessoa', 'Sair do Sistema'])
    if r == 1:
        b.lerArq(arq)
    elif r == 2:
        b.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title()
        idade = b.leiaInt('Idade: ')
        b.cadastrar(arq,nome,idade)
    elif r == 3:
        break
    else:
        print('Digite uma opção válida')
b.cabecalho('SAINDO DO SISTEMA.. ATÉ LOGO')
time.sleep(2)


