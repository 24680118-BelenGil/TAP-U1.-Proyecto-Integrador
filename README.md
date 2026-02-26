# Formulario
## Planteamiento
Desarrolla un formulario con las siguientes características:
* No enviar entradas vacías.
* Validar formato de email.
* Se incluyen control  Dropdown.
* Se incluye control radio.

Después de dar click al botón de enviar, mostrar en una ventada modal (AlertDialog) los datos recogidos en el formulario
## Desarrollo
### Librerias
```python
import flet as ft
import re
```
* **import flet as ft:** Importa la librería Flet, que permite crear interfaces gráficas en Python, redefiniendola con *ft* para mas comodidad.
* **import re:** Importa la librería de expresiones regulares, utilizada para validar el formato del correo electrónico.
  
### Definición de Patrón de Email
```python
patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```
Verifica que el correo:
* Tenga caracteres antes del @
* Contenga dominio válido
* Termine con al menos 2 letras (.com, .mx, .org, etc.)

### Función Principal
```python
def main(page: ft.Page):
```
Define la función principal representando con *page* la ventana o página de la aplicación. Además, todo el diseño y lógica se construyen dentro de esta función.

### Configuración de Página
```python
page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"  # Fondo crema de la imagen
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT
```
Establecemos el titulo de la pagina con *page.title*, definimos el color de la ventana con *page.bgcolor* y un espacio interno *page.padding*. Por último, con ayuda de *page.theme_mode = ft.ThemeMode.LIGHT*  , establecemos el modo de tema de la página en luz.
### Controles de Entrada
#### NOMBRE
```python
txt_nombre = ft.TextField(label="Nombre", expand=True, bgcolor="white")
```
Crea un cuadro de texto donde el usuario escribe su nombre. Al usar *label*, le das una instrucción clara que se desplaza al hacer clic; con *expand=True*, obligas al control a estirarse para llenar todo el ancho disponible en su contenedor; y con *bgcolor="white"*, aseguras que el campo resalte visualmente sobre el fondo.
#### NÚMERO DE CONTROL
```python
 txt_control = ft.TextField(
        label="Numero de control",
        keyboard_type=ft.KeyboardType.NUMBER,
        expand=True,
        bgcolor="white"
    )
```
Define un campo de entrada especializado para datos numéricos, con *keyboard_type=ft.KeyboardType.NUMBER*, hace que en dispositivos móviles despliega automáticamente el teclado numérico. Al igual que el anterior, se expande para ocupar el espacio disponible y mantiene un fondo blanco para contrastar con el diseño de tu interfaz.
#### E-MAIL
```python
 txt_email = ft.TextField(label="Email", expand=True, bgcolor="white")
```
Define un campo específico para capturar el correo electrónico del usuario. Como en los campos anteriores, se expande para ocupar el espacio disponible y contrasta con el diseño de la interfaz.
#### CARRERA
```python
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
```
Crea una lista desplegable (Dropdown) que permite al usuario elegir una carrera de un menú predefinido. Al usar *options*, defines las categorías disponibles (desde Sistemas hasta Contabilidad), mientras que *border_color="#4D2A32"* le da un toque personalizado con un borde color vino o marrón oscuro. Las propiedades *filled=True* y *fill_color* aseguran que el fondo sea sólido y limpio.
#### SEMESTRE
```python
dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#4D2A32",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 14)],
        bgcolor="white",
        filled=True,
        fill_color=ft.Colors.WHITE
    )
```
Crea una lista desplegable (Dropdown), para que el usuario seleccione su semestre dentro de una lista. La propiedad *options=[ft.dropdown.Option(str(i)) for i in range(1, 14)]* genera automáticamente las opciones del 1 al 13, convirtiendo cada número en texto. *label="Semestre"* muestra el nombre del campo, *expand=True* hace que ocupe el ancho disponible, *border_color="#4D2A32"* define el color del borde, y *bgcolor, filled* y *fill_color* establecen el fondo blanco del componente para mejorar su apariencia visual.
#### GÉNERO
```python
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
```
Crea un grupo de botones de opción (RadioGroup) llamado genero, que permie seleccionar una sola opción entre “Masculino” y “Femenino”. Dentro del RadioGroup, se utiliza un *ft.Row* para acomodar los botones en forma horizontal *(alignment=ft.MainAxisAlignment.START los alinea a la izquierda)*. Luego, se crea *row_genero*, que es otra fila que contiene el texto “Género:” en negrita y color personalizado, junto con el grupo de opciones. En conjunto, este bloque construye el componente visual para que el usuario seleccione su género de manera organizada y clara.
### Diágolo emergente
```python
 dialog = ft.AlertDialog(
        title=ft.Text("Información Guardada"),
        on_dismiss=lambda e: print("Dialog dismissed!"),
    )

    page.overlay.append(dialog)
```
Creamos un cuadro de diálogo emergente *(AlertDialog)* llamado **dialog**, que mostrará un mensaje con el título **“Información Guardada”** cuando se active. La propiedad *on_dismiss* define una función que se ejecuta cuando el usuario cierra el diálogo. Finalmente, *page.overlay.append(dialog)* agrega el diálogo a la capa superior de la página *(overlay)*, lo que permite que pueda mostrarse encima del contenido principal cuando se establezca *dialog.open = True*.
### Función de Guardado
```python
import flet as ft
import re
```
### Botón de Enviar
```python
import flet as ft
import re
```
### Agregar Controles a la Página
```python
import flet as ft
import re
```
### Ejecutar la Aplicación
```python
import flet as ft
import re
```
## Resultado
