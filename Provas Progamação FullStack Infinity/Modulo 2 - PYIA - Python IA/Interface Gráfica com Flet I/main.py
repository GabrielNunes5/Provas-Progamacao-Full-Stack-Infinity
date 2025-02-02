import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.title = "Lista de Tarefas"
    page.theme_mode = ft.ThemeMode.SYSTEM

    # Função para adicionar tarefa
    def add_task(e):
        if task_input.value.strip():  # Verifica se não está vazio
            task_list.controls.append(ft.Text(task_input.value))
            task_input.value = ""  # Limpa o campo de entrada
            page.update()

    # Campo de entrada
    task_input = ft.TextField(label="Nova Tarefa", width=300)
    # Lista de tarefas
    task_list = ft.Column()

    # Botão para adicionar tarefa
    add_button = ft.ElevatedButton("Adicionar Nova Tarefa", on_click=add_task)

    # Layout da página
    layout = ft.Column(
        controls=[
            task_input,
            add_button,
            task_list
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(layout)


ft.app(target=main)
