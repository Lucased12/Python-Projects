# Github: https://github.com/Lucased12

import tkinter as tk
import pickle

#Definir los colores utilizados en la aplicación
colorFondo = "#FCF5ED"  #Color de fondo
colorBoton = "#CE5A67"  #Color de los botones
colorTexto = "#1F1717"  #Color del texto

#Cargar notas existentes o inicializar lista vacía
try:
    with open('notas.pkl', 'rb') as f:
        notas = pickle.load(f)
except FileNotFoundError:
    notas = []

#Función para guardar las notas en un archivo
def guardarNotas():
    with open('notas.pkl', 'wb') as f:
        pickle.dump(notas, f)

#Funciones para manipular las notas
def agregarNota():
    nota = entry.get()
    notas.append(nota)
    listbox.insert(tk.END, nota)
    entry.delete(0, tk.END)
    guardarNotas()

def borrarNota():
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        listbox.delete(indice)
        notas.pop(indice)
        guardarNotas()

def editarNota():
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        notaSeleccionada = listbox.get(indice)
        entry.delete(0, tk.END)
        entry.insert(tk.END, notaSeleccionada)
        guardarButton.config(command=lambda: guardarEdicion(indice))

def guardarEdicion(indice):
    nuevaNota = entry.get()
    notas[indice] = nuevaNota
    listbox.delete(indice)
    listbox.insert(indice, nuevaNota)
    entry.delete(0, tk.END)
    guardarNotas()
    guardarButton.config(command=agregarNota)

#Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación de Notas")
root.configure(bg=colorFondo)

#Componentes de la interfaz gráfica
frame = tk.Frame(root, bg=colorFondo)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=50, bg=colorFondo, fg=colorTexto)
entry.pack(padx=5, pady=5)

buttonAgregar = tk.Button(frame, text="Agregar Nota", command=agregarNota, bg=colorBoton, fg=colorTexto)
buttonAgregar.pack(padx=5, pady=5)

buttonBorrar = tk.Button(frame, text="Borrar Nota", command=borrarNota, bg=colorBoton, fg=colorTexto)
buttonBorrar.pack(padx=5, pady=5)

buttonEditar = tk.Button(frame, text="Editar Nota", command=editarNota, bg=colorBoton, fg=colorTexto)
buttonEditar.pack(padx=5, pady=5)

listbox = tk.Listbox(frame, width=50, bg=colorFondo, fg=colorTexto)
for nota in notas:
    listbox.insert(tk.END, nota)
listbox.pack(padx=5, pady=5)

#Botón para guardar ediciones
guardarButton = tk.Button(frame, text="Guardar", command=agregarNota, bg=colorBoton, fg=colorTexto)
guardarButton.pack(padx=5, pady=5)

#Ejecutar la aplicación
root.mainloop()
