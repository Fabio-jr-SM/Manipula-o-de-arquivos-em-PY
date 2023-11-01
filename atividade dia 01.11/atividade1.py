import json

def carregar_tabela():
    with open('notas.json','r') as f:
        texto = f.read()
        notas = json.loads(texto)
    return notas

def print_table(tabela,turma):
    print(f"------------------ TURMA {turma} -------------")
    print("|{:<25} |{:<5} |{:<5}|".format("NOME","TURMA","NOTA"))

    for nome_reg,turma_reg,nota_reg in tabela:
        if turma_reg == turma:
            print("|{:<25} |{:<5} |{:<5}|".format(nome_reg,turma_reg,nota_reg))

def calcular_media(tabela,turma):
    soma = 0
    cont = 0

    for nome_reg,turma_reg,nota_reg in tabela:
        if turma_reg == turma:
            soma +=nota_reg
            cont +=1
    return soma/cont

if __name__=='__main__':
    tabela = carregar_tabela()
    for turma in ['1A','1B','1C']:
        print_table(tabela,turma)
        print(f"Media da turma: {calcular_media(tabela,turma)}")
