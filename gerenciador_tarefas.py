def adicionar_tarefa(descricao):
    with open('tasks.txt', 'a') as arquivo:
        arquivo.write(descricao + '\n')


def listar_tarefas():
    try:
        with open('tasks.txt', 'r') as arquivo:
            lista_de_tarefas_ou_umaTarefa = arquivo.readlines()
            if not lista_de_tarefas_ou_umaTarefa:
                print("Nenhuma tarefa encontrada.")
            else:
                for indice, tarefa in enumerate(lista_de_tarefas_ou_umaTarefa, start=1):
                    print(f'{indice}. {tarefa.strip()}')
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")


def menu():
    while True:
        print('\n=== GERENCIADOR DE TAREFAS ===')
        print('1. Adicionar Tarefa')
        print('2. Listar Tarefas')
        print('3. Sair')
        opcoes_de_escolhas = input('Escolha a opção desejada: ')

        if opcoes_de_escolhas == '1':
            descricao_da_tarefa = input('Digite a descrição da tarefa: ')
            adicionar_tarefa(descricao_da_tarefa)
            print('Tarefa adicionada com sucesso!')
        elif opcoes_de_escolhas == '2':
            print('\n=== LISTA DE TAREFAS ===')
            listar_tarefas()
        elif opcoes_de_escolhas == '3':
            print('Saindo do gerenciador de tarefas...')
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == "__main__":
    menu()