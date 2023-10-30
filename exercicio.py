import os 

os.system("cls")
lista = []

def cadastro(lista):
    f = open('cadastro.txt','w')
    f.write(str(lista))
    f.close()

def ler_cadastro():
    if os.path.exists('cadastro.txt'):
        f = open('cadastro.txt','r')
    else:
        f = open('cadastro.txt','w+')
        f.write('[]')
        f.close()
        f = open('cadastro.txt','r')
    texto = f.read()
    lista2 = eval(texto)
    return lista2

if __name__ == '__main__':

    lista = ler_cadastro()

    while True:
        op = input("Escolha uma opção:\n1 - Cadastrar Usuario\n2 - Listar usuarios\n")
        if op =='':
            break
        elif op=='1':
            nome = input("Digite o nome: ")
            lista.append(nome)
            cadastro(lista)
        
        elif op=='2':
            for nome in lista:
                print(nome)

        