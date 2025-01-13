# Lista para armazenar as tarefas
tarefas = []


# Adiciona uma nova tarefa à lista
def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")


# Lista todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(
            f"[{idx}] {tarefa['nome']} - {tarefa['descricao']}"
            f"(Prioridade: {
                tarefa['prioridade']}, Categoria: {
                    tarefa['categoria']}, Status: {status})")


# Marca uma tarefa como concluída
def concluir_tarefa(indice):
    try:
        tarefas[indice - 1]["concluida"] = True
        print(f"Tarefa '{tarefas[indice - 1]
              ['nome']}' marcada como concluída!")
    except IndexError:
        print("Índice inválido. Tente novamente.")


# Exibe tarefas por prioridade
def exibir_por_prioridade(prioridade):
    print(f"Tarefas com prioridade {prioridade}:")
    tarefas_filtradas = [
        tarefa for tarefa in tarefas if tarefa["prioridade"] == prioridade]
    if not tarefas_filtradas:
        print("Nenhuma tarefa encontrada com essa prioridade.")
        return
    for tarefa in tarefas_filtradas:
        print(f"- {tarefa['nome']} ({tarefa['descricao']})")


# Exibe tarefas por categoria.
def exibir_por_categoria(categoria):
    print(f"Tarefas na categoria '{categoria}':")
    tarefas_filtradas = [
        tarefa for tarefa in tarefas if tarefa["categoria"] == categoria]
    if not tarefas_filtradas:
        print("Nenhuma tarefa encontrada nessa categoria.")
        return
    for tarefa in tarefas_filtradas:
        print(f"- {tarefa['nome']} ({tarefa['descricao']})")
