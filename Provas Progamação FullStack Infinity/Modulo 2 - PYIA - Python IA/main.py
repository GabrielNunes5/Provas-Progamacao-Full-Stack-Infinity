'''
Desenvolver um programa de linha de comando que permite
aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
prioridades e categorias. O projeto será organizado em várias
partes e usará funções, listas, tuplas, dicionários, conjuntos e
um ambiente virtual. Passos do projeto:
# Configuração do Ambiente Virtual:
Crie um ambiente virtual usando o módulo venv

# Definição de Dados:
Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir
informações como nome, descrição, prioridade e categoria. Você pode usar
dicionários para representar as tarefas.

# Funções:
Crie funções para adicionar tarefas, listar tarefas, marcar tarefas
como concluídas, exibir tarefas por prioridade ou categoria, e outras
funcionalidades que desejar.

# Menu de Comandos:
Crie um menu de comandos de linha de comando que permita ao
usuário interagir com o programa.
'''
from funcoes_to_do import (adicionar_tarefa,
                           listar_tarefas,
                           concluir_tarefa,
                           exibir_por_prioridade,
                           exibir_por_categoria)


# Exibe o menu e gerencia as interações do usuário
def menu():
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir tarefas por prioridade")
        print("5. Exibir tarefas por categoria")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade da tarefa (Alta, Média, Baixa): ")
            categoria = input("Categoria da tarefa: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            try:
                indice = int(
                    input("Número da tarefa a marcar como concluída: "))
                concluir_tarefa(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "4":
            prioridade = input(
                "Prioridade para filtrar (Alta, Média, Baixa): ")
            exibir_por_prioridade(prioridade)
        elif opcao == "5":
            categoria = input("Categoria para filtrar: ")
            exibir_por_categoria(categoria)
        elif opcao == "6":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
