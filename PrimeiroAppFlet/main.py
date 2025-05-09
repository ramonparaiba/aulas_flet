import flet as ft 

def main(page: ft.Page):    

    page.title = "Meu Primeiro App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(ft.Text("Eu agora é HECKER!", size=30, color="blue"))
    # Adiciona os componentes à página
ft.app(main)