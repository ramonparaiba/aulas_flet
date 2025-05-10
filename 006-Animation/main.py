import flet as ft
import flet_lottie as fl

def main(page: ft.Page):    

    page.title = "Animacao"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    lo = fl.Lottie(
        src="https://raw.githubusercontent.com/xvrh/lottie-flutter/refs/heads/master/example/assets/Logo/LogoSmall.json",
        reverse=False,
        animate=True,
    )
    c1 = ft.Container(
        content=lo,
        bgcolor=ft.Colors.BLUE_50,
        padding=50,
    )
    page.add(c1)
    
    # Adiciona os componentes à página
ft.app(main)