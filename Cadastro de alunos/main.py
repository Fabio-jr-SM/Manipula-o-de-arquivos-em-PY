import os

def cadastrar_aluno(cadastro):
    nome = input("Digite nome do aluno: ")
    email = input("Digite email do aluno: ")
    turma = input("Digite a turma do aluno: ")

    if cadastro == dict():
        rga = 1
    else:
        rga = max(cadastro.keys())+1
    
    cadastro[rga] = (nome,email,turma)
    
def listar_alunos(cadastro):
    print("{:<10} {:<20} {:<20} {:<20}".format("RGA","NOME","EMAIL","TURMA"))
    for rga, tupla in cadastro.items():
        print("--------------------------------------------------------------------")
        print('{:<10}'.format(rga),end='')
        for item in tupla:
            print('{:<20}'.format(item),end='')
        print("\n--------------------------------------------------------------------")

    

def buscar_cadastro(cadastro):
    rga_busca = int(input("Digite o RGA para buscar: "))
    if rga_busca in cadastro.keys():
        print(cadastro[rga_busca])
    else:
        print("Aluno Inexistente\n")

def salvar_cadastro_em_arquivo(cadastro):
    name_file = input("Digite o nome do arquivo e tipo: ")
    f = open(name_file,'w')
    f.write(str(cadastro))
    f.close()

def carregar_cadastro_de_darquivo():
    name_file = input("Digite o nome do arquivo: ")
    if os.path.exists(name_file):
        f = open(name_file,'r')
        texto = f.read()
        f.close()
        return eval(texto)
    else:
        print("Arquivo Inexistente!!")
        return None
    
def menu():
    cadastro = {}
    while True:
        print("==========MENU==========")
        op = input("Escolha uma Opção\n"
                    "1 - Cadastrar Estudante\n"
                    "2 - Listar Cadastro\n"
                    "3 - Buscar cadastro por RGA\n"
                    "4 - salvar cadastro em arquivo\n"
                    "5 - Carregar cadastros de arquivos\n"
                    "0 - Sair\n")
        
        if op == '1':
            cadastrar_aluno(cadastro)
        elif op == '2':
            listar_alunos(cadastro)
        elif op == '3':
            buscar_cadastro(cadastro)
        elif op == '4':
            salvar_cadastro_em_arquivo(cadastro)
        elif op == '5':
            retorno = carregar_cadastro_de_darquivo()
            if retorno is not None:
                cadastro = retorno
        elif op == '0':
            break
        else:
            print("Opção invalida")

if __name__ == '__main__':
    menu()
