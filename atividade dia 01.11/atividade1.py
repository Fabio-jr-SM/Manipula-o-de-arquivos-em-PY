import os
import json

if os.path.exists('notas.json'):
    f = open('notas.json','r')
    texto = f.read()
    f.close()
    notas = json.loads(texto)
else:
    print("Arquivo Inexistente!!")

soma=0
cont=0
print("------------------ TURMA 1A -------------")
print("|{:<25} |{:<5} |{:<5}|".format("NOME","TURMA","NOTA"))

for i in notas:
    if i[1] == '1A':
        print("|{:<25} |{:<5} |{:<5}|".format(i[0],i[1],i[2]))
        soma+=i[2]
        cont+=1
print(f"Média da turma: {soma/cont}")

print("\n\n")

soma=0
cont=0
print("------------------ TURMA 1B -------------")
print("|{:<25} |{:<5} |{:<5}|".format("NOME","TURMA","NOTA"))
for i in notas:
    if i[1] == '1B':
        print("|{:<25} |{:<5} |{:<5}|".format(i[0],i[1],i[2]))
        soma+=i[2]
        cont+=1
print(f"Média da turma: {soma/cont}")

print("\n\n")

soma=0
cont=0
print("------------------ TURMA 1C -------------")
print("|{:<25} |{:<5} |{:<5}|".format("NOME","TURMA","NOTA"))
for i in notas:
    if i[1] == '1C':
        print("|{:<25} |{:<5} |{:<5}|".format(i[0],i[1],i[2]))
        soma+=i[2]
        cont+=1
print(f"Média da turma: {soma/cont}")
