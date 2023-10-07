import tkinter as tk

def convertir_kilometros():
    try:
        kilometros = float(entrada_kilometros.get())
    
        millas = kilometros * 0.621371
    
        etiqueta_resultado.config(text=f"{kilometros} kilometros son {millas} millas")
    
    except ValueError:
        etiqueta_resultado.confi(text="Ingrese un valor numerico valido")
        

menu = tk.Tk()
menu.title("Conversor de Kilometros a Millas")
menu.geometry("300x150")

etiqueta_instruccion = tk.Label(menu, text="Ingrese la distancia en kilometros:")
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entrada_kilometros = tk.Entry(menu)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10)

boton_convertir = tk.Button(menu, text="Convertir", command=convertir_kilometros)
boton_convertir.grid(row=1, column=1, padx=10, pady=10)

etiqueta_resultado = tk.Label(menu, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

menu.mainloop()
