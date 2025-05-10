import flet as ft 

def main(page: ft.Page):    

    page.title = "Cards"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Titulo do Card"),
                    ft.Text("Texto do Card"),
                    ft.Row(
                        [
                            ft.TextButton("Entrar"),
                            ft.TextButton("Sair"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                ]
            ),
            width=300,
            padding=20,
            bgcolor=ft.Colors.GREEN_ACCENT,
            
        )
    )

    page.add(card)
    
ft.app(main)