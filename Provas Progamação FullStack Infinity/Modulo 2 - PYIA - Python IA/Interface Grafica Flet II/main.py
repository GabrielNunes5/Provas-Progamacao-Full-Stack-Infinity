import flet as ft


def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campos do formulário
    nome = ft.TextField(label="Nome", width=300)
    email = ft.TextField(label="Email", width=300)
    mensagem = ft.TextField(label="Mensagem", multiline=True, width=300)

    # Função para processar o envio do formulário
    def enviar_formulario(e):
        if nome.value and email.value and mensagem.value:
            # Exibe a mensagem de confirmação e o botão "Voltar"
            page.clean()
            page.add(
                ft.Column(
                    [
                        ft.Text("Formulário enviado com sucesso!",
                                size=20, color=ft.Colors.GREEN),
                        ft.ElevatedButton(
                            "Voltar", on_click=voltar_ao_formulario)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()

    # Função para voltar ao formulário
    def voltar_ao_formulario(e):
        # Limpa os valores dos campos
        nome.value = ""
        email.value = ""
        mensagem.value = ""
        page.clean()
        page.add(form)

    # Botão de envio
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_formulario)

    # Layout do formulário
    form = ft.Column(
        [
            nome,
            email,
            mensagem,
            botao_enviar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Adiciona o formulário à página inicial
    page.add(form)


# Iniciar a aplicação
ft.app(target=main)
