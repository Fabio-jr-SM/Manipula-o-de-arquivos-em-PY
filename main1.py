import os
os.system("cls")

lista = ['Fabio','Sla']
nome_dir = 'meus_arquivos'
nome_arq = 'exemplo.txt'

f = open(os.path.join(nome_dir,nome_arq),'w+')

f.write(str(lista))
f.close()