import os
os.system("cls")

nome_dir = 'meus_arquivos'
nome_arq = 'exemplo.txt'

f = open(os.path.join(nome_dir,nome_arq),'r')
lista = eval(f.read())
for nome in lista:
    print(nome)
f.close()