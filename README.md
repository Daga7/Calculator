# 📦 Calculadora de Lista de Precios

Aplicación de escritorio construida con [Flet](https://flet.dev/) para calcular automáticamente precios de venta a partir de un precio de costo, aplicando diferentes porcentajes de ganancia según listas predefinidas.

## ✨ Características

- ✅ Cálculo rápido de precios con porcentajes predefinidos.
- ✅ Interfaz gráfica amigable con **Flet**.
- ✅ Tabla de resultados con porcentajes y precios formateados.
- ✅ Botón para limpiar los campos y resultados.
- ✅ Soporte para limpiar campos presionando la tecla **ESC**.
- ✅ Mensajes de error si el valor ingresado no es válido.

## 📷 Vista previa

<p align="center">
  <img src="https://raw.githubusercontent.com/Daga7/Calculator/main/Preview.png" alt="Vista previa de la aplicación" width="350" style="border-radius: 10px;">
</p>

## 🛠 Requisitos

- Python **3.8+**
- Biblioteca **Flet**

Instalar dependencias con:

```bash
pip install flet
```

🛠 Instalación de `pip` (si no está instalado)

```bash
sudo apt update
sudo apt install python3-pip
```

🚀 Uso

Clonar el repositorio:

```bash
git clone https://github.com/Daga7/Calculator.git
```

Entrar al directorio:

```bash
cd Calculator
```

Ejecutar la aplicación:

```bash
python Trabajo.py
```

Ingresar el precio de costo y presionar Enter o el botón Calcular Precios.

## 📄 Estructura del código  

### 🔹 `calcular_precio`  
> Calcula el precio final aplicando un porcentaje sobre el precio de costo.

### 🔹 `main`  
> Define la interfaz gráfica, los eventos y la lógica principal de la aplicación.

### 🔹 `calcular_precios`  
> Procesa el precio ingresado y genera la tabla de resultados con los precios calculados.

### 🔹 `limpiar_campos` y `on_key_down`  
> Permiten limpiar la interfaz mediante botón o atajo de teclado (**ESC**).

---

## 📌 Atajos de teclado  

- **ESC** → Limpia el campo y la tabla de resultados.  
- **ENTER** → Calcula los precios.

---

## 📜 Licencia  

Este proyecto es de uso libre y puede ser modificado y distribuido según tus necesidades