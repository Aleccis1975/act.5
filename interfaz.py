import tkinter as tk
from tkinter import messagebox
from cambio import devolver_cambio, monedas  # Importar la lógica desde el archivo cambio.py

# Función para calcular y mostrar el cambio
def calcular_cambio():
    try:
        total = float(entry_total.get())  # Obtener el total pagado
        pagado = float(entry_pagado.get())  # Obtener el monto pagado

        if pagado < total:
            messagebox.showerror("Error", "El monto pagado debe ser mayor o igual al total.")
            return
        
        cambio = pagado - total  # Calcular el cambio a devolver
        resultado = devolver_cambio(cambio, monedas)
        
        # Mostrar los resultados en la interfaz
        resultado_texto = f"Vuelto: {cambio:.2f} pesos\n"
        for moneda, cantidad in resultado:
            resultado_texto += f"{cantidad} moneda(s) de {moneda} pesos\n"
        
        label_resultado.config(text=resultado_texto)
    except ValueError:
        messagebox.showerror("Error", "Introduce valores numéricos válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo del Cambio")
ventana.geometry("400x400")

# Etiqueta de instrucciones
label_instruccion = tk.Label(ventana, text="Introduce el total y el monto pagado:")
label_instruccion.pack(pady=10)

# Crear un frame para agrupar las entradas del total
frame_total = tk.Frame(ventana)
frame_total.pack(pady=5)

# Etiqueta y entrada para el total
label_total = tk.Label(frame_total, text="Total:")
label_total.pack(side="left")
entry_total = tk.Entry(frame_total)
entry_total.pack(side="left", padx=5)

# Crear un frame para agrupar las entradas del monto pagado
frame_pagado = tk.Frame(ventana)
frame_pagado.pack(pady=5)

# Etiqueta y entrada para el monto pagado
label_pagado = tk.Label(frame_pagado, text="Monto Pagado:")
label_pagado.pack(side="left")
entry_pagado = tk.Entry(frame_pagado)
entry_pagado.pack(side="left", padx=5)

# Botón para calcular el cambio
boton_calcular = tk.Button(ventana, text="Calcular Cambio", command=calcular_cambio)
boton_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
