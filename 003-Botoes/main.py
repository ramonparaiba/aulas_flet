import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Meu Primeiro App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Text("Botoes no Flet"),
        ft.ElevatedButton("Botão 1", on_click=lambda e: print("Botão Elevado clicado")),
        ft.FilledButton("Botão 2", on_click=lambda e: print("Botão Preenchido clicado")),
        ft.OutlinedButton("Botão 3", on_click=lambda e: print("Botão Borda fina clicado")),
        ft.TextButton("Botão 4", on_click=lambda e: print("Botão Texto clicado")),
        ft.IconButton(icon = ft.Icons.ADD, on_click=lambda e: print("Botão Ícone clicado")),
        ft.FloatingActionButton(icon = ft.Icons.DELETE, on_click=lambda e: print("Botão Flutuante clicado")),         
        )
    
ft.app(main)