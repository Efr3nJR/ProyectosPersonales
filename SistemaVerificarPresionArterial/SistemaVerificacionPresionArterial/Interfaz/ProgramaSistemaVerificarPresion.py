import tkinter as tk
from tkinter import messagebox

def verificar_presion_arterial():
    try:
        sys_mmhg = float(sys_entry.get())
        dia_mmhg = float(dia_entry.get())
        pulse_min = float(pulse_entry.get())

        if sys_mmhg < 90 or dia_mmhg < 60 or pulse_min < 60:
            messagebox.showinfo("Resultado", "Bajo - Consulta médica recomendada.", icon="info")
        elif sys_mmhg >= 140 or dia_mmhg >= 90 or pulse_min >= 100:
            messagebox.showinfo("Resultado", "Alto - Consulta médica recomendada.", icon="warning")
        else:
            messagebox.showinfo("Resultado", "Bien - Valores dentro del rango normal.", icon="info")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

def limpiar_campos():
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas limpiar los campos?")
    if confirmacion:
        sys_entry.delete(0, tk.END)
        dia_entry.delete(0, tk.END)
        pulse_entry.delete(0, tk.END)

def salir():
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas salir del programa?")
    if confirmacion:
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.configure(bg="DarkSlateGray3")
root.title("Verificador de Presión Arterial")
root.geometry("600x600")

# Etiqueta para indicar al usuario que ingrese información
info_label = tk.Label(root, text="Ingrese la información en los siguientes campos de texto:", font=("Arial", 14), bg="DarkSlateGray3", fg="black")
info_label.pack(pady=10)

# Crear etiquetas y campos de entrada
font_size = 14
label_font = ("Arial", font_size)
entry_font = ("Arial", font_size)
button_font = ("Arial", font_size)

sys_label = tk.Label(root, text="SYS mmHg:", font=label_font, bg="DarkSlateGray3", fg="black")
sys_label.pack(fill=tk.BOTH, expand=True)
sys_entry = tk.Entry(root, font=entry_font, justify=tk.CENTER)
sys_entry.pack(fill=tk.BOTH, expand=True)

dia_label = tk.Label(root, text="DIA mmHg:", font=label_font, bg="DarkSlateGray3", fg="black")
dia_label.pack(fill=tk.BOTH, expand=True)
dia_entry = tk.Entry(root, font=entry_font, justify=tk.CENTER)
dia_entry.pack(fill=tk.BOTH, expand=True)

pulse_label = tk.Label(root, text="Pulse/min:", font=label_font, bg="DarkSlateGray3", fg="black")
pulse_label.pack(fill=tk.BOTH, expand=True)
pulse_entry = tk.Entry(root, font=entry_font, justify=tk.CENTER)
pulse_entry.pack(fill=tk.BOTH, expand=True)

# Crear un frame para los botones
button_frame = tk.Frame(root, bg="DarkSlateGray3")
button_frame.pack(fill=tk.BOTH, expand=True)

verificar_btn = tk.Button(button_frame, text="Verificar", command=verificar_presion_arterial, font=button_font, bg="#3CB371", fg="black")
verificar_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

limpiar_btn = tk.Button(button_frame, text="Limpiar Campos", command=limpiar_campos, font=button_font, bg="#FF6347", fg="black")
limpiar_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

salir_btn = tk.Button(button_frame, text="Salir", command=salir, font=button_font, bg="#4682B4", fg="black")
salir_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Ejecutar la interfaz gráfica
root.mainloop()
