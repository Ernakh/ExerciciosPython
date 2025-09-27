#Criar um arquivo TXT contendo atividades e status das atividades, uma linha por atividade e logo abaixo da linha o status da atividade.
#Deve ter um menu e implementar as opções de incluir atividade, remover atividade e concluir atividade e todas as operações devem ser gravadas no arquivo

from pathlib import Path

atividades = []
ARQ = Path("C:\\Users\\fabri\\OneDrive\\Cursos\\Especialização em Inteligência Artificial e Machine Learning\\1 - Algoritmos e Programação com Python\\atividades.txt")

def listar():
    with open(ARQ, "r", encoding="utf-8") as f:
        i = 1
        for linha in f:
            atividades.append(linha)
        i = 1
        aux = 1
        for l in atividades:
            if i % 2 != 0:
                print(f"{aux} - {l}", end="")
                aux = aux + 1
            else:
                print(f"   {l}")    
            i += 1  

def incluir():
    desc = input("Descrição da atividade: ")
    status = "Pendente" 
    with open(ARQ, "a+", encoding="utf-8") as f:
        f.write(desc + "\n" + status + "\n")
    print("Entrada adicionada ao diário com sucesso!")

def remover(indice):
    total_atividades = len(atividades)//2
    if total_atividades == 0:
        print("Não há atividades para remover.")
        return

    if indice < 1 or indice > total_atividades:
        print("Número inválido.")
        return

    inicio = (indice - 1) * 2
    fim = inicio + 2
    del atividades[inicio:fim]

    with open(ARQ, "w", encoding="utf-8") as f:
        f.writelines(atividades)
    print("Atividade removida com sucesso!")

def concluir(indice):

    total_atividades = len(atividades) // 2
    if total_atividades == 0:
        print("Não há atividades para concluir.")
        return

    if indice < 1 or indice > total_atividades:
        print("Número inválido.")
        return

    pos_status = (indice - 1) * 2 + 1
    atividades[pos_status] = "Concluída\n"

    with open(ARQ, "w", encoding="utf-8") as f:
        f.writelines(atividades)
    print(f"Atividade {indice} concluída com sucesso!")


print("Menu de Atividades")
print("1 - Incluir Atividade")                  
print("2 - Excluir Atividade")                  
print("3 - Concluir Atividade")                  

if not Path(ARQ).exists():
    Path(ARQ).write_text("", encoding="utf-8")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    incluir()
elif opcao == 2:
    listar()
    remover(int(input("Escolha uma atividade: ")))
elif opcao == 3:
    listar()
    concluir(int(input("Escolha uma atividade: ")))
else:
    print("Opção inválida.\n")




