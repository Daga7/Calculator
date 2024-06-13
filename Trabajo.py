import flet as ft


def calcular_precio(precio_costo, porcentaje):
    return precio_costo * (1 + porcentaje / 100)

def main(page: ft.Page):
    def calcular_precios(e):
        try:
            # Obtener el precio de costo desde la entrada
            precio_costo = float(input_precio_costo.value)

            # Diccionario con los nombres de las listas y sus porcentajes de ganancia
            listas = {
                "102 (12%)": {"porcentaje": "12%", "precio": calcular_precio(precio_costo, 12)},
                "102 (15%)": {"porcentaje": "15%", "precio": calcular_precio(precio_costo, 15)},
                "104": {"porcentaje": "20%", "precio": calcular_precio(precio_costo, 20)},
                "203": {"porcentaje": "10%", "precio": calcular_precio(precio_costo, 10)},
                "10": {"porcentaje": "3%", "precio": calcular_precio(precio_costo, 3)}
            }

            # Limpiar la columna de resultados antes de agregar nuevas filas
            text_resultados.controls.clear()

            # Agregar la tabla de precios
            text_resultados.controls.append(
                ft.Text("Resultados", style="headlineSmall"),  # Agrega un título para la tabla de resultados
            )
            text_resultados.controls.append(
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Lista")),
                        ft.DataColumn(ft.Text("Porcentaje")),
                        ft.DataColumn(ft.Text("Precio")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(lista)),
                                ft.DataCell(ft.Text(datos["porcentaje"])),
                                ft.DataCell(ft.Text(f"${datos['precio']:.2f}"))
                            ]
                        ) for lista, datos in listas.items()
                    ],
                )
            )
            # Actualizar la página
            page.update()
        except ValueError:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Por favor ingrese un número válido para el precio de costo."),
                on_dismiss=lambda e: page.update()
            )
            page.dialog.open = True
            page.update()

    def limpiar_campos(e=None):
        # Limpiar el valor del campo de texto 
        input_precio_costo.value = ""
        # Limpiar tablas 
        text_resultados.controls.clear()
        page.update()
        
    # Metodo para limpiar campos oprimiendo tecla 

    def on_key_down(e=ft.KeyboardEvent):
        # Limpiar el valor del campo de texto 
        if e.key == "r":
            input_precio_costo.value = ""
            # Limpiar tablas 
            text_resultados.controls.clear()
            page.update()
            

    # Configuración de la ventana
    page.title = "Lista De Precios"
    page.window_width = 420
    page.window_height = 550

    input_precio_costo = ft.TextField(
        label="Ingrese el precio de costo",
        on_submit=calcular_precios
    )
    btn_calcular = ft.ElevatedButton(text="Calcular Precios", on_click=calcular_precios)
    btn_limpiar = ft.ElevatedButton(text="Limpiar", color="red", on_click=limpiar_campos, )
    text_resultados = ft.Column()

    # Agregar los widgets a la página
    page.add(
        input_precio_costo,
        btn_calcular,
        text_resultados,
        btn_limpiar,
    )

    # Centrar ORTIMARCAS SAS al final
    page.add(
        ft.Row(
            controls=[
                ft.Text(value="ORTIMARCAS SAS", color="blue", size=16, weight="bold")
            ],
            alignment="center"
        )
    )
    
    # agregue acá el evento de presionar tecla "ESC"
    
    page.on_keyboard_event = on_key_down


# Ejecutar la aplicación Flet
ft.app(target=main)
