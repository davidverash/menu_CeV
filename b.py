def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except:
            print("\033[31mERRO: digite um numero inteiro\033[m")
        else:
            return n
            break



def linha(tam=50):
    print('-'*tam)

def cabecalho(nome):
    linha()
    print(nome.center(50))
    linha()

def menu(lista):
    cabecalho('\033[0mMENU PRINCIPAL\033[m')
    for v,k in enumerate(lista):
        print(f'\033[33m{v+1}\033[m -  \033[34m{k}\033[m')
    linha()
    op = leiaInt('\033[0;33mSua opção:\033[m ')
    return op

def arqExiste(arq):
    try:
        a = open(arq,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(arq):
    try:
        a = open(arq,'wt+')
        a.close()
    except:
        print("Arquivo não criado")
    else:
        print(f'Arquivo <{arq}> criado com sucesso !!')


def lerArq(arq):
    try:
        a = open(arq,'rt')
    except:
        print('Não foi possivel ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n',' ')
            print(f'{dado[0].ljust(30)}{dado[1].rjust(10)} anos')
    finally:
        a.close()



def cadastrar(arq,nome = '<desconhecido',idade = 0):
    try:
        a = open(arq,'at')
    except:
        print("Houve um ERRO na abertura do arquivo")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO: não foi possível cadastrar')
        else:
            print(f'Novo cadastro de {nome} realizado com sucesso!')
            a.close()



