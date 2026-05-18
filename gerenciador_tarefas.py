from datetime import date

tarefas = []

def adicionar_tarefa(descricao, data_criacao, prazo, prioridade):
    """
    Adiciona uma nova tarefa à lista de tarefas.
    Parâmetros:
        descricao : Descrição da tarefa a ser realizada.
        data_criacao: Data de criação da tarefa, gerada automaticamente.
        prazo : Prazo em dias para concluir a tarefa.
        prioridade : Nível de prioridade da tarefa (baixa, média ou alta).
    """
    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "data_criacao": data_criacao,
        "prazo": prazo,
        "prioridade": prioridade,
        "status": "A fazer"
    }
    tarefas.append(tarefa)

def mostrar_tarefas():
    """
    Lista todas as tarefas cadastradas.
    """
    if len(tarefas) == 0:
        print("A lista de tarefas está vazia!")
    else:
        for tarefa in tarefas:
            print(f"""ID: {tarefa['id']}
                Descrição: {tarefa['descricao']}.
                Data: {tarefa['data_criacao']}.
                Prazo: {tarefa['prazo']} dias.
                Prioridade: {tarefa['prioridade']}.
                Status: {tarefa['status']}.""")

def concluida(id):
    """
    Marca uma tarefa como concluída, buscando pelo ID.
    Parâmetros:
        id : Identificador único da tarefa a ser marcada como concluída.
    """
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["status"] = "Concluída"
            break
    else:
        print("Nenhuma tarefa encontrada!")

def remover_tarefa(id):
    """
    Remove uma tarefa da lista, buscando pelo ID.
    Parâmetros:
        id : Identificador único da tarefa a ser removida.
    """
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            break
    else:
        print("Nenhuma tarefa encontrada!")

while True:
    print(f"""
      1 - Adicionar tarefa
      2 - Mostrar tarefas
      3 - Concluir tarefa
      4 - Excluir tarefa
      5 - Sair
      """)
    opcao = input("Escolha uma opção:")
    if opcao == "1":
        descricao = input("Tarefa:")
        data_criacao = date.today()
        prazo = input("Quantos dias para cumprir a tarefa?")
        prioridade = input("""Prioridade da tarefa:
                           1 - Baixa
                           2 - Média
                           3 - Alta
                           """)
        if prioridade == "1":
            prioridade = "Baixa"
        elif prioridade == "2":
            prioridade = "Média"
        elif prioridade == "3":
            prioridade = "Alta"
        adicionar_tarefa(descricao, data_criacao, prazo, prioridade)
    elif opcao == "2":
        mostrar_tarefas()
    elif opcao == "3":
        id = int(input("Digite a ID da tarefa concluída:"))
        concluida(id)
    elif opcao == "4":
        id = int(input("Digite a ID da tarefa a ser excluída:"))
        remover_tarefa(id)
    elif opcao == "5":
        break
    else:
        print("Digite um número válido!")
