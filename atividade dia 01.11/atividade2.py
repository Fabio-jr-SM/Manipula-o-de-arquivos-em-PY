import json

def carregar_estoque():
    with open('estoque.json','r') as f:
        texto = f.read()
        estoque = json.loads(texto)
    return estoque



def mostrar_estoque(estoque):
    print(f"\n\n{'codigo':<8} {'nome':<18} {'preco':<8} {'estoque':<10} {'vendas':<10}")
    for codigo, lista in estoque.items():
        print(f"{codigo:<8} {lista[0]:<18} {lista[1]:<8} {lista[2]:<10} {lista[3]:<10}")

def registrar_venda(estoque):
    codigo_reg = input("Digite o codigo do produto: ")
    if codigo_reg in estoque.keys():
            if estoque[codigo_reg][2] == 0:
                print("Estoque Vazio\n")
            else:
                estoque[codigo_reg][2] -= 1
                estoque[codigo_reg][3] += 1

                with open('estoque.json','w') as f:
                    f.write(json.dumps(estoque))

        
def faturamento(estoque):
    soma = 0
    for codigo in estoque.keys():
        valor = estoque[codigo][1]*estoque[codigo][3]
        soma +=valor
    print(f"Faturamento Atual: {soma}")

def menu(estoque):
    while True:
        op = input("\n\nEscolha uma Opção:\n(1) Mostrar tabela\n(2) Registrar vendas\n(3) Calcular faturamento\n")

        if op == '1':
            mostrar_estoque(estoque)
        elif op == '2':
            registrar_venda(estoque)
        elif op == '3':
            faturamento(estoque)


if __name__=='__main__':
    estoque = carregar_estoque()
    menu(estoque)
