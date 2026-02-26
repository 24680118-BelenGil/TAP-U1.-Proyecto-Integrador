import flet as ft
import re

patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def main(page: ft.Page):

    # Configuración de página para entorno Web/Pyodide
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"  # Fondo crema de la imagen
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- CONTROLES DE ENTRADA (Subtema 1.4) ---
    txt_nombre = ft.TextField(label="Nombre", expand=True, bgcolor="white")

    txt_control = ft.TextField(
        label="Numero de control",
        keyboard_type=ft.KeyboardType.NUMBER,
        expand=True,
        bgcolor="white"
    )

    txt_email = ft.TextField(label="Email", expand=True, bgcolor="white")

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#4D2A32",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
            ft.dropdown.Option("Gestión Empresarial"),
            ft.dropdown.Option("Ingeniería Mecatrónica"),
            ft.dropdown.Option("Ingeniería Electrónica"),
            ft.dropdown.Option("Contabilidad")
        ],
        bgcolor="white",
        filled=True,
        fill_color=ft.Colors.WHITE
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#4D2A32",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 14)],
        bgcolor="white",
        filled=True,
        fill_color=ft.Colors.WHITE
    )
    
    # Contenedor para Genero
    genero = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Masculino", label="Masculino"),
                ft.Radio(value="Femenino", label="Femenino"),
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

    row_genero = ft.Row(
        [
            ft.Text("Género:", color="#4D2A32", weight=ft.FontWeight.BOLD),
            genero
        ]
    )

    dialog = ft.AlertDialog(
        title=ft.Text("Información Guardada"),
        on_dismiss=lambda e: print("Dialog dismissed!"),
    )

    page.overlay.append(dialog)

    def guardar_click(e):
        print("click")

        # Resetear estados de error previos
        txt_nombre.error_text = None
        txt_nombre.border_color = "#4D2A32"

        txt_control.error_text = None
        txt_control.border_color = "#4D2A32"

        txt_email.error_text = None
        txt_email.border_color = "#4D2A32"

        # Variable bandera
        formulario_valido = True

        # Validacion nombre
        if not txt_nombre.value or not txt_nombre.value.strip():
            txt_nombre.error_text = "El nombre es obligatorio"
            txt_nombre.border_color = "red"
            formulario_valido = False

        # Validacion numero de control
        if not txt_control.value or not txt_control.value.strip():
            txt_control.error_text = "El No. de Control es obligatorio"
            txt_control.border_color = "red"
            formulario_valido = False
        elif not txt_control.value.isdigit():
            txt_control.error_text = "Solo se permiten números"
            txt_control.border_color = "red"
            formulario_valido = False
        else:
            txt_control.error_text = None
            txt_control.border_color = "#4D2A32"

        # Validacion email
        if not txt_email.value or not txt_email.value.strip():
            txt_email.error_text = "El Gmail es obligatorio"
            txt_email.border_color = "red"
            formulario_valido = False
        elif not re.match(patron_email, txt_email.value):
            txt_email.error_text = "Formato de correo inválido (ejemplo@gmail.com)"
            txt_email.border_color = "red"
            formulario_valido = False
        else:
            txt_email.error_text = None
            txt_email.border_color = "#4D2A32"

        if not formulario_valido:
            page.update()
            return

        carrera_seleccionada = dd_carrera.value if dd_carrera.value else "No seleccionada"
        semestre_seleccionado = dd_semestre.value if dd_semestre.value else "No seleccionado"
        seleccion_genero = genero.value if genero.value else "No especificado"

        dialog.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(f"Nombre: {txt_nombre.value}"),
                    ft.Text(f"No. Control: {txt_control.value}"),
                    ft.Text(f"Gmail: {txt_email.value}"),
                    ft.Text(f"Carrera: {carrera_seleccionada}"),
                    ft.Text(f"Semestre: {semestre_seleccionado}"),
                    ft.Text(f"Género: {seleccion_genero}")
                ],
                tight=True,
                spacing=10
            ),
            width=400,
            padding=20
        )

        dialog.open = True
        page.update()

    btn_enviar = ft.Button(
        content=ft.Text("Enviar", color="black", size=16),
        bgcolor=ft.Colors.GREY_500,
        width=page.width,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
        ),
        on_click=guardar_click
    )

    page.add(
        ft.Column(
            [
                txt_nombre,
                txt_control,
                txt_email,
                ft.Row([dd_carrera, dd_semestre], spacing=10),
                row_genero,
                btn_enviar
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
            tight=True
        )
    )

ft.run(main)
