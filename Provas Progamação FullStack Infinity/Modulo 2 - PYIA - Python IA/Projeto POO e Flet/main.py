import flet as ft
from datetime import datetime
from gerenciador_reservas import GerenciadorReservas
from quarto import Quarto
from cliente import Cliente


def main(page: ft.Page):
    page.title = "Refúgio dos Sonhos - Sistema de Reservas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    gerenciador = GerenciadorReservas()

    # Dados iniciais para teste
    quartos = [
        Quarto(101, "Single", 150),
        Quarto(201, "Double", 250),
        Quarto(301, "Suite", 500)
    ]
    for q in quartos:
        gerenciador.adicionar_quarto(q)

    clientes = [
        Cliente("Ana Silva", "11987654321", "ana@email.com"),
        Cliente("Carlos Souza", "21987654321", "carlos@email.com")
    ]
    for c in clientes:
        gerenciador.registrar_cliente(c)

    # Controles da interface
    def carregar_quartos():
        return [ft.ListTile(
            title=ft.Text(str(quarto)),
            bgcolor=ft.Colors.GREEN_100 if quarto.disponivel else ft.Colors.RED_100
        ) for quarto in gerenciador.quartos]

    lista_quartos = ft.Column([], expand=True)

    # Tela de Clientes
    grid_clientes = ft.GridView(
        expand=True,
        runs_count=5,
        max_extent=300,
        child_aspect_ratio=2,
        spacing=10,
        padding=20
    )

    def carregar_clientes():
        grid_clientes.controls = []
        for cliente in gerenciador.clientes:
            grid_clientes.controls.append(
                ft.Card(
                    ft.Container(
                        ft.Column([
                            ft.Text(cliente.exibir_informacoes()),
                        ]),
                        padding=10
                    )
                )
            )
        page.update()

    # Tela de Novo Cliente
    nome_cliente = ft.TextField(label="Nome completo")
    telefone_cliente = ft.TextField(label="Telefone")
    email_cliente = ft.TextField(label="E-mail")

    def salvar_cliente(e):
        try:
            # Validação dos campos
            nome = nome_cliente.value.strip()
            telefone = telefone_cliente.value.strip()
            email = email_cliente.value.strip()

            # Validação do nome
            if len(nome) < 3:
                raise ValueError("Nome deve ter pelo menos 3 caracteres")

            # Validação do telefone
            if not telefone.isdigit() or len(telefone) < 8:
                raise ValueError(
                    "Telefone deve ter apenas números (mínimo 8 dígitos)")

            # Validação de e-mail
            if "@" not in email or "." not in email or email.count("@") != 1:
                raise ValueError("Formato de e-mail inválido")

            # Criação do cliente
            novo_cliente = Cliente(nome, telefone, email)
            gerenciador.registrar_cliente(novo_cliente)

            # Limpar campos
            nome_cliente.value = ""
            telefone_cliente.value = ""
            email_cliente.value = ""

            page.open(ft.SnackBar(
                content=ft.Text("Cliente cadastrado com sucesso!",
                                color=ft.Colors.WHITE),
                bgcolor=ft.Colors.GREEN,
                duration=3000
            ))
            page.update()

            # Navegar após mostrar o feedback
            carregar_clientes()
            page.go("/clientes")

        except ValueError as ve:
            page.open(ft.SnackBar(
                content=ft.Text(f"Erro: {str(ve)}",
                                color=ft.Colors.WHITE),
                bgcolor=ft.Colors.RED,
                duration=3000
            ))
            page.update()

        except Exception as ex:
            page.open(ft.SnackBar(
                content=ft.Text(f"Erro inesperado: {str(ex)}",
                                color=ft.Colors.WHITE),
                bgcolor=ft.Colors.RED,
                duration=3000
            ))
            page.update()

    # Tela de Reservas
    lista_reservas = ft.ListView(expand=True)

    def carregar_reservas():
        lista_reservas.controls = []
        for reserva in gerenciador.reservas:
            lista_reservas.controls.append(
                ft.ListTile(
                    title=ft.Text(f"Quarto {reserva.quarto.numero}"),
                    subtitle=ft.Text(
                        f"{reserva.cliente.nome} - {reserva.check_in.strftime('%d/%m/%Y')} a {reserva.check_out.strftime('%d/%m/%Y')}"),
                    trailing=ft.IconButton(
                        ft.Icons.CANCEL,
                        on_click=lambda e, r=reserva: cancelar_reserva(r)
                    )
                )
            )
        page.update()

    def cancelar_reserva(reserva):
        gerenciador.cancelar_reserva(reserva)
        carregar_reservas()
        carregar_quartos()
        page.update()

    # Date Pickers
    date_picker_checkin = ft.DatePicker()
    date_picker_checkout = ft.DatePicker()
    page.overlay.extend([date_picker_checkin, date_picker_checkout])

    txt_checkin = ft.Text("Nenhuma data selecionada")
    txt_checkout = ft.Text("Nenhuma data selecionada")

    def update_checkin(e):
        txt_checkin.value = date_picker_checkin.value.strftime(
            "%d/%m/%Y") if date_picker_checkin.value else "Nenhuma data selecionada"
        page.update()

    def update_checkout(e):
        txt_checkout.value = date_picker_checkout.value.strftime(
            "%d/%m/%Y") if date_picker_checkout.value else "Nenhuma data selecionada"
        page.update()

    date_picker_checkin.on_change = update_checkin
    date_picker_checkout.on_change = update_checkout

    # Tela de Nova Reserva
    dropdown_clientes = ft.Dropdown(label="Selecione o cliente")
    dropdown_quartos = ft.Dropdown(label="Selecione o quarto")

    def confirmar_reserva(e):
        try:
            if not dropdown_clientes.value:
                raise ValueError("Selecione um cliente!")
            if not dropdown_quartos.value:
                raise ValueError("Selecione um quarto!")
            if not date_picker_checkin.value or not date_picker_checkout.value:
                raise ValueError("Selecione ambas as datas!")

            check_in = datetime.combine(
                date_picker_checkin.value, datetime.min.time())
            check_out = datetime.combine(
                date_picker_checkout.value, datetime.min.time())

            if check_in >= check_out:
                raise ValueError("Check-out deve ser posterior ao Check-in!")

            cliente = next(c for c in gerenciador.clientes if c.id ==
                           int(dropdown_clientes.value))
            quarto = next(q for q in gerenciador.quartos if q.numero == int(
                dropdown_quartos.value))

            reserva = gerenciador.criar_reserva(
                cliente, quarto, check_in, check_out)
            if reserva:
                # Limpar formulário
                dropdown_clientes.value = None
                dropdown_quartos.value = None
                date_picker_checkin.value = None
                date_picker_checkout.value = None
                txt_checkin.value = "Nenhuma data selecionada"
                txt_checkout.value = "Nenhuma data selecionada"

                # Atualizar dados
                carregar_quartos()
                carregar_reservas()

                # Feedback e navegação
                page.snack_bar = ft.SnackBar(
                    ft.Text("Reserva criada com sucesso!",
                            color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.GREEN
                )
                page.go("/reservas")
            else:
                raise ValueError("Quarto não disponível para este período!")

        except ValueError as ve:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Erro: {str(ve)}", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.RED
            )
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Erro inesperado: {str(ex)}", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.RED
            )

        page.snack_bar.open = True
        page.update()

    # Configuração da navegação
    def navigate(e):
        index = e.control.selected_index
        if index == 0:
            page.go("/")
        elif index == 1:
            page.go("/clientes")
        elif index == 2:
            page.go("/reservas")

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(
                icon=ft.Icons.PEOPLE, label="Clientes"),
            ft.NavigationBarDestination(icon=ft.Icons.LIST, label="Reservas")
        ],
        on_change=navigate
    )

    # Configuração das rotas
    def route_change(e):
        page.views.clear()
        selected_index = 0

        if page.route == "/clientes":
            selected_index = 1
        elif page.route == "/reservas":
            selected_index = 2

        nav_bar.selected_index = selected_index

        # Tela Inicial
        if page.route == "/":
            lista_quartos.controls = carregar_quartos()
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Quartos Disponíveis")),
                        lista_quartos,
                        ft.FloatingActionButton(
                            icon=ft.Icons.ADD,
                            text="Nova Reserva",
                            on_click=lambda e: page.go("/nova-reserva")
                        )
                    ],
                    navigation_bar=nav_bar
                )
            )

        # Tela de Clientes
        elif page.route == "/clientes":
            carregar_clientes()
            page.views.append(
                ft.View(
                    "/clientes",
                    [
                        ft.AppBar(title=ft.Text("Gerenciar Clientes")),
                        grid_clientes,
                        ft.FloatingActionButton(
                            icon=ft.Icons.ADD,
                            on_click=lambda e: page.go("/novo-cliente")
                        )
                    ],
                    navigation_bar=nav_bar
                )
            )

        # Tela de Reservas
        elif page.route == "/reservas":
            carregar_reservas()
            page.views.append(
                ft.View(
                    "/reservas",
                    [
                        ft.AppBar(title=ft.Text("Reservas Ativas")),
                        lista_reservas
                    ],
                    navigation_bar=nav_bar
                )
            )

        # Tela Nova Reserva
        elif page.route == "/nova-reserva":
            # Atualizar dropdowns
            dropdown_clientes.options = [
                ft.dropdown.Option(
                    key=str(c.id),
                    text=c.exibir_informacoes()
                ) for c in gerenciador.clientes
            ]
            dropdown_quartos.options = [
                ft.dropdown.Option(
                    key=str(q.numero),
                    text=f"Quarto {q.numero} ({q.tipo}) - R${q.preco_diaria}",
                    disabled=not q.disponivel
                ) for q in gerenciador.quartos
            ]

            page.views.append(
                ft.View(
                    "/nova-reserva",
                    [
                        ft.AppBar(title=ft.Text("Nova Reserva")),
                        ft.Column([
                            ft.Text("Dados da Reserva", size=20,
                                    weight=ft.FontWeight.BOLD),
                            dropdown_clientes,
                            dropdown_quartos,
                            ft.Row([
                                ft.ElevatedButton(
                                    "Selecionar Check-in",
                                    icon=ft.Icons.CALENDAR_MONTH,
                                    on_click=lambda _: (
                                        setattr(date_picker_checkin, 'open', True), page.update())
                                ),
                                txt_checkin
                            ]),
                            ft.Row([
                                ft.ElevatedButton(
                                    "Selecionar Check-out",
                                    icon=ft.Icons.CALENDAR_MONTH,
                                    on_click=lambda _: (
                                        setattr(date_picker_checkout, 'open', True), page.update())
                                ),
                                txt_checkout
                            ]),
                            ft.ElevatedButton(
                                "Confirmar Reserva",
                                icon=ft.Icons.CHECK_CIRCLE,
                                on_click=confirmar_reserva,
                                width=250
                            )
                        ], spacing=20, expand=True)
                    ],
                    scroll=ft.ScrollMode.AUTO
                )
            )

        # Tela Novo Cliente
        elif page.route == "/novo-cliente":
            # Resetar campos
            nome_cliente.value = ""
            telefone_cliente.value = ""
            email_cliente.value = ""

            page.views.append(
                ft.View(
                    "/novo-cliente",
                    [
                        ft.AppBar(title=ft.Text("Novo Cliente")),
                        ft.Column([
                            ft.Text("Cadastrar Novo Cliente", size=20,
                                    weight=ft.FontWeight.BOLD),
                            nome_cliente,
                            telefone_cliente,
                            email_cliente,
                            ft.ElevatedButton(
                                "Salvar Cliente",
                                icon=ft.Icons.SAVE,
                                on_click=salvar_cliente,
                                width=200
                            )
                        ], spacing=20, expand=True)
                    ]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
