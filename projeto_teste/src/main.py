import flet as ft


def main(page: ft.Page):
    
    logo_flet = ft.Image(src="https://flet.dev/img/logo.svg", width=100, height=100)
    imagem_local = ft.Image(src="https://pabloramon.com.br/wp-content/uploads/2025/04/circle_image.png", width=100, height=100)

    page.add(
        logo_flet,
        imagem_local,
        ft.Text("Inserindo imagens fle", size=30, color="blue")
        )
    page.update()


ft.app(target=main, assets_dir="assets")
