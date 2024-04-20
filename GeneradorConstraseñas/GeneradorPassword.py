import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import random
import string

def validar_longitud(longitud):
    if not longitud.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico para la longitud.")
        return False
    return True

def validar_tipos_caracteres(longitud, tipos_caracteres, contraseña_generada):
    caracteres_encontrados = {tipo: False for tipo in tipos_caracteres}
    for caracter in contraseña_generada:
        for tipo in tipos_caracteres:
            if tipo == "mayúsculas" and caracter in string.ascii_uppercase:
                caracteres_encontrados["mayúsculas"] = True
            elif tipo == "minúsculas" and caracter in string.ascii_lowercase:
                caracteres_encontrados["minúsculas"] = True
            elif tipo == "números" and caracter in string.digits:
                caracteres_encontrados["números"] = True
            elif tipo == "especiales" and caracter in string.punctuation:
                caracteres_encontrados["especiales"] = True

    for tipo, encontrado in caracteres_encontrados.items():
        if not encontrado:
            return False
    return True

def limpiar_campos():
    longitud_string.delete(0, tk.END)
    for opcion in opciones:
        combo_boxes[opcion].set("No")
    txt_output.delete('1.0', tk.END)
    desactivar_exportar()

def salir_del_sistema():
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir del sistema?"):
        window.destroy()

def generar_string(tipos_caracteres, longitud):
    caracteres = ""
    if "mayúsculas" in tipos_caracteres:
        caracteres += string.ascii_uppercase
    if "minúsculas" in tipos_caracteres:
        caracteres += string.ascii_lowercase
    if "números" in tipos_caracteres:
        caracteres += string.digits
    if "especiales" in tipos_caracteres:
        caracteres += string.punctuation
    contraseña_generada = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña_generada

def generar_contraseña():
    longitud = longitud_string.get()
    if not validar_longitud(longitud):
        return
    
    longitud = int(longitud)
    tipos_caracteres = []
    for opcion in opciones:
        if combo_boxes[opcion].get() == "Sí":
            tipos_caracteres.append(opcion)
    
    if not tipos_caracteres:
        messagebox.showerror("Error", "Por favor, selecciona al menos un tipo de caracteres.")
        return
    correcto = False
    cantidad_opc = len(tipos_caracteres)
    while correcto != True:
        contraseña_generada = generar_string(tipos_caracteres, longitud)
        if (cantidad_opc > longitud) or (validar_tipos_caracteres(longitud, tipos_caracteres, contraseña_generada)):
            correcto = True
       
    txt_output.delete('1.0', tk.END)  # Limpiar el panel de texto antes de agregar la nueva contraseña
    txt_output.insert(tk.END, contraseña_generada)
    activar_exportar()

def activar_exportar():
    btn_exportar.config(state="normal")

def desactivar_exportar():
    btn_exportar.config(state="disabled")

def exportar_contraseña():
    contraseña_generada = txt_output.get("1.0", tk.END).strip()  # Obtener la contraseña generada del panel de texto
    if not contraseña_generada:
        messagebox.showerror("Error", "No hay contraseña generada para exportar.")
        return

    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "w") as file:
            file.write(contraseña_generada)
        messagebox.showinfo("Éxito", f"Contraseña exportada correctamente en:\n{archivo}")

def main_window():
    global longitud_string, opciones, combo_boxes, txt_output, window, btn_exportar

    window = tk.Tk()
    window.title("Generador de Contraseñas")
    window.geometry("850x425")
    window.resizable(False, False)
    window["bg"] = "DarkSlateGray3"
    
    # Crear y posicionar los widgets
    font_style = ("Arial", 12, "bold")  # Estilo de fuente: (Fuente, Tamaño, Estilo)
    
    lbl_longstring = tk.Label(window, text="Longitud Deseada:", bg="DarkSlateGray3", font=font_style)
    lbl_longstring.grid(row=0, column=0, padx=10, pady=5, sticky="W")
    longitud_string = tk.Entry(window, font=font_style)
    longitud_string.grid(row=0, column=1, padx=10, pady=5, sticky="W")
    
    lbl_type = tk.Label(window, text="Tipo de Caracteres:", bg="DarkSlateGray3", font=font_style)
    lbl_type.grid(row=1, column=0, padx=10, pady=5, sticky="W")

    opciones = ["mayúsculas", "minúsculas", "números", "especiales"]
    combo_boxes = {}
    for index, opcion in enumerate(opciones):
        lbl_opcion = tk.Label(window, text=f"{opcion.capitalize()}:", bg="DarkSlateGray3", font=font_style)
        lbl_opcion.grid(row=2+index, column=0, padx=10, pady=5, sticky="W")
        combo_boxes[opcion] = ttk.Combobox(window, values=["Sí","No"], width=5, font=font_style, state="readonly")
        combo_boxes[opcion].set("No")  
        combo_boxes[opcion].grid(row=2+index, column=1, padx=10, pady=5, sticky="W")

    btn_generar = tk.Button(window, text="Generar", command=generar_contraseña, font=font_style)
    btn_generar.grid(row=7, column=0, padx=10, pady=10, sticky="WE")

    btn_exportar = tk.Button(window, text="Exportar Contraseña", command=exportar_contraseña, font=font_style, state=tk.DISABLED)
    btn_exportar.grid(row=7, column=1, padx=10, pady=10, sticky="WE")

    btn_limpiar = tk.Button(window, text="Limpiar Campos", command=limpiar_campos, font=font_style)
    btn_limpiar.grid(row=8, column=0, columnspan=2, pady=5, sticky="WE")

    btn_salir = tk.Button(window, text="Salir del Sistema", command=salir_del_sistema, font=font_style)
    btn_salir.grid(row=9, column=0, columnspan=2, pady=5, sticky="WE")

    txt_output = tk.Text(window, height=10, width=50,  fg="blue", font=font_style)
    txt_output.grid(row=0, column=2, rowspan=10, padx=10, pady=5, sticky="NSWE")

    window.mainloop()

if __name__ == "__main__":
    main_window()
