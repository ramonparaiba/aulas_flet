import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Meu Primeiro App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Adiciona os componentes à página
    logo_flet = ft.Image(src="https://flet.dev/img/logo.svg", width=200, height=200)
    imagem_local = ft.Image(src="imgs/logotipo.png", width=200, height=200)


    page.add(
        logo_flet, 
        imagem_local,
        ft.Text("Inserindo imagens no app", size=30, color="blue")
        )

ft.app(main)