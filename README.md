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
 def guardar_click(e):
        print("click")
```
Define la función *guardar_click(e)*, que es la función que se ejecuta cuando el usuario hace clic en el botón Enviar. El parámetro *e* representa el evento del click (evento de tipo click).
#### Rastrear errores
```python
        txt_nombre.error_text = None
        txt_nombre.border_color = "#4D2A32"

        txt_control.error_text = None
        txt_control.border_color = "#4D2A32"

        txt_email.error_text = None
        txt_email.border_color = "#4D2A32"
```
Reinicia los estados de error de los campos *txt_nombre*, *txt_control* y *txt_email* antes de realizar una nueva validación. Al asignar *error_text = None*, se eliminan los mensajes de error mostrados previamente, y al restablecer *border_color = "#4D2A32"*, se devuelve el color original del borde (quitando el rojo si hubo error). Esto permite que cada vez que se presione el botón, la validación comience “limpia” y no conserve errores anteriores.
#### Variable bandera
```python
formulario_valido = True
```
Se utiliza para controlar si el formulario cumple con todas las validaciones. Inicialmente se establece en *True* asumiendo que todo está correcto; sin embargo, si durante las validaciones se detecta algún error (campo vacío, formato incorrecto, etc.), esta variable cambia a *False*.
#### Validación de nombre
```python
        if not txt_nombre.value or not txt_nombre.value.strip():
            txt_nombre.error_text = "El nombre es obligatorio"
            txt_nombre.border_color = "red"
            formulario_valido = False
```
La condición *if not txt_nombre.value or not txt_nombre.value.strip()* verifica si el usuario no escribió nada o si solo ingresó espacios en blanco. Si se cumple la condición, se muestra el mensaje “El nombre es obligatorio”, el borde del campo cambia a color rojo para indicar error visualmente y la variable *formulario_valido* se establece en *False*, impidiendo que el formulario se envíe hasta que el usuario corrija el campo.
#### Validación de número de control
```python
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
```
Primero verifica si el campo está vacío o contiene solo espacios; si es así, muestra el mensaje **“El No. de Control es obligatorio”**, cambia el borde a rojo y marca *formulario_valido = False*. Luego, con *elif*, comprueba si el valor contiene únicamente números usando *.isdigit()*; si no es numérico, muestra el mensaje **“Solo se permiten números”** y también marca error. Finalmente, en el *else*, si todo es correcto, elimina cualquier mensaje de error y restablece el color original del borde, indicando que el campo es válido.
#### Validación de email
```python
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
```
Verifica si está vacío o contiene solo espacios; si es así, muestra el mensaje **“El Gmail es obligatorio”**, cambia el borde a rojo y marca el formulario como inválido. Luego, con *elif*, usa *re.match(patron_email, txt_email.value)* para comprobar que el correo tenga un formato correcto; si no coincide con el patrón, muestra el mensaje **“Formato de correo inválido”** y también marca error. En el *else*, si el correo es válido, elimina el mensaje de error y restablece el color original del borde.

Finalmente, *if not formulario_valido:* comprueba si hubo algún error en cualquier campo; si es así, ejecuta *page.update()* para reflejar los mensajes en pantalla y return para detener la ejecución, evitando que se guarde la información hasta que todo esté correcto.
#### Obtención y validación final de datos seleccionados
```python
        carrera_seleccionada = dd_carrera.value if dd_carrera.value else "No seleccionada"
        semestre_seleccionado = dd_semestre.value if dd_semestre.value else "No seleccionado"
        seleccion_genero = genero.value if genero.value else "No especificado"
```
Obtiene los valores seleccionados en los controles *Dropdown* y *RadioGroup*. Utiliza una expresión condicional para verificar si el usuario seleccionó una opción. Si *dd_carrera.value* tiene un valor, se guarda en *carrera_seleccionada*; de lo contrario, se asigna el texto "No seleccionada". Lo mismo ocurre con *dd_semestre* y *genero*. Esto evita que se muestren valores vacíos y garantiza que siempre haya un texto definido cuando se muestre la información en el diálogo.
#### Visualización del cuadro de diálogo con los datos registrados
```python   
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
```
Define el contenido del cuadro de diálogo que se mostrará después de que el formulario sea válido. Se asigna a *dialog.content* un *ft.Container* que contiene una *ft.Column* con varios *ft.Text*, donde se muestran los datos ingresados por el usuario (nombre, número de control, correo, carrera, semestre y género). La propiedad *spacing=10* agrega espacio entre cada línea y *tight=True* ajusta el diseño para que sea más compacto, mientras que *width=400* y *padding=20* controlan el tamaño y el espacio interno del cuadro. Finalmente, *dialog.open = True* abre el diálogo y *page.update()* actualiza la interfaz para que el usuario pueda ver la información guardada en pantalla.
### Botón de Enviar
```python
 btn_enviar = ft.Button(
        content=ft.Text("Enviar", color="black", size=16),
        bgcolor=ft.Colors.GREY_500,
        width=page.width,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
        ),
        on_click=guardar_click
    )
```
Este bloque crea el botón btn_enviar utilizando *ft.Button*, el cual mostrará el texto “Enviar” con color negro y tamaño 16. Se le asigna un fondo gris *(bgcolor=ft.Colors.GREY_500)* y un ancho igual al de la página *(width=page.width)* para que ocupe todo el espacio horizontal disponible. En style se define que el botón tenga bordes rectos *(radius=0)*. Finalmente, la propiedad *on_click=guardar_click* conecta el botón con la función que valida y guarda la información cuando el usuario hace click.
### Agregar Controles a la Página
```python
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
```
Este bloque agrega todos los controles del formulario a la página y los organiza usando *ft.Column*, que hace que los elementos se muestren uno debajo del otro. Dentro de la columna se colocan los campos de nombre, número de control y correo, luego un *ft.Row* acomoda horizontalmente los dropdown de carrera y semestre, seguido del grupo de género y el botón enviar. Además, *spacing=15* agrega espacio entre los elementos, *scroll=ft.ScrollMode.AUTO* permite desplazamiento si el contenido es grande y *tight=True* ajusta el espacio interno para que el diseño sea más compacto y ordenado.
### Ejecutar la Aplicación 🚀
```python
ft.run(main)
```
* Ejecuta la función main.
* Crea la ventana o entorno web.
* Construye la interfaz gráfica.
* Mantiene la aplicación en ejecución esperando eventos (clics, entradas, etc.).
## Resultado
[Da click aquí para ver el código](./Formulario.py)

<img width="1918" height="874" alt="Captura de pantalla 2026-02-24 232443" src="https://github.com/user-attachments/assets/f508b733-5cc6-41c1-98ba-bfa21669748b" />
<img width="1916" height="863" alt="Captura de pantalla 2026-02-24 232533" src="https://github.com/user-attachments/assets/1c58bebc-f0ab-48d5-ae08-51657539d2a0" />


