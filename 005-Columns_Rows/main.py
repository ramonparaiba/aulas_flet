import flet as ft 

def main(page: ft.Page):    

    page.title = "Columns and Rows"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    linha = ft.Container(
        content = ft.Row(
            controls=[
                ft.Text("Linha 1"),
                ft.Text("Linha 2"),
                ft.Text("Linha 3"),
                ft.Text("Linha 4"),
                ft.Text("Linha 5"),
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor="red",
    )
    coluna = ft.Column(
        controls=[
            ft.Container(
                content=ft.Text("Seção 1", color="white"),
                padding=20,
                bgcolor="purple",
                border_radius=10,
                width=200,
            ),
            ft.Container(
                content=ft.Text("Seção 2", color="white"),
                padding=20,
                bgcolor="orange",
                border_radius=10,
                width=200,
            ),
            ft.Container(
                content=ft.Text("Seção 3", color="white"),
                padding=20,
                bgcolor="teal",
                border_radius=10,
                width=200,
            ),
        ],
        spacing=10,  # Espaçamento entre os itens
        alignment=ft.CrossAxisAlignment.CENTER,  # Alinha no centro
    )

    page.add(
        ft.Text("Estudando Linhas e Colunas"),
        linha,
        coluna
        )
    
ft.app(main)