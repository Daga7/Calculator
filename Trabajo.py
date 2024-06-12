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
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Lista"), numeric=False),
                        ft.DataColumn(ft.Text("Porcentaje"), numeric=False),
                        ft.DataColumn(ft.Text("Precio"), numeric=False),
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

    # Crear y colocar los widgets
    page.title = "Lista De Precios"
    page.window_width = 420
    page.window_height = 550

    input_precio_costo = ft.TextField(
        label="Ingrese el precio de costo",
        on_submit=calcular_precios  # Llama a calcular_precios cuando se presiona "Enter"
    )
    btn_calcular = ft.ElevatedButton(text="Calcular Precios", on_click=calcular_precios)
    text_resultados = ft.Column()

    # Agregar los widgets a la página
    page.add(
        input_precio_costo,
        btn_calcular,
        text_resultados,
        ft.ElevatedButton(text="Salir", color="red", on_click=lambda e: page.window_close())
    )
    
    # Centrar ORTIMARCAS SAS al final
    page.add(
        ft.Row(
            controls=[
                ft.Text(value="ORTIMARCAS SAS", color="blue", size=16, weight="bold")
            ],
            alignment="center"  # Centra el texto horizontalmente
        )
    )

# Ejecutar la aplicación Flet
ft.app(target=main)