linguagens = {'david':'python','andre':'javascript','arthur':'c',
              'felipe':'python','joao':'c','maria':'php'}

lista = []
for value in set(linguagens.values()):
    lista.append(value)
lista.sort()
for i in lista:
    print(i.title())