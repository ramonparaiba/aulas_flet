import flet as ft
import datetime

def main(page: ft.Page):
    # Configurações da página
    page.title = "Meu Primeiro App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    dropdown = ft.Dropdown(
            label="Selecione um país",
            options=[
                ft.DropdownOption("Brasil"),
                ft.DropdownOption("Argentina"),
                ft.DropdownOption("Chile"),
            ],
    )
    radio_group = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="1", label="Opção 1"),
                ft.Radio(value="2", label="Opção 2"),
                ft.Radio(value="3", label="Opção 3"),
            ]
        )
    )

    slider = ft.Slider(
        label="Selecione um valor",
        min=0,
        max=100,
        divisions=10,
        value=50,
    )

    data_picker = ft.DatePicker(
        first_date=datetime.datetime(year=2000, month=10, day=1),
        last_date=datetime.datetime(year=2025, month=10, day=1),
                )
    botao_data = ft.ElevatedButton( "selecionar data", on_click= lambda e: page.open(data_picker))

    page.add(
        ft.Text("Formulários no Flet", size=30),
        ft.TextField(label="Login"),
        ft.TextField(label="Senha", password=True),
        dropdown,
        radio_group,
        ft.Checkbox(label="Aceito os termos e condições"),
        ft.Checkbox(label="Aceito receber notificações"),
        ft.TextField(label="Mensagem", multiline=True, min_lines = 4, max_lines=5),
        slider,
        botao_data
        )
    
ft.app(main)