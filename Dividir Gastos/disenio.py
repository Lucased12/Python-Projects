# Github: https://github.com/Lucased12

import tkinter as tk
from tkinter import ttk, Button

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Divisor de Gastos")
        root.resizable(False, False)

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame, text="Divisor de Gastos", font=("Arial", 16)).grid(row=0, column=0, columnspan=3)

        ttk.Label(self.frame, text="Agregar Miembro:").grid(row=1, column=0, sticky=tk.W)
        self.miembroEntry = ttk.Entry(self.frame, width=20)
        self.miembroEntry.grid(row=1, column=1)
        self.agregarMiembroBtn = ttk.Button(self.frame, text="Agregar")
        self.agregarMiembroBtn.grid(row=1, column=2)

        ttk.Label(self.frame, text="Miembros:").grid(row=2, column=0, sticky=tk.W)
        self.miembrosListbox = tk.Listbox(self.frame, height=5, width=30, selectmode=tk.MULTIPLE)
        self.miembrosListbox.grid(row=3, column=0, columnspan=3)

        ttk.Label(self.frame, text="¿Quien pago?").grid(row=4, column=0, sticky=tk.W)
        self.pagadorCombobox = ttk.Combobox(self.frame, state="readonly", width=17)
        self.pagadorCombobox.grid(row=4, column=1)

        ttk.Label(self.frame, text="Descripcion del Gasto:").grid(row=5, column=0, sticky=tk.W)
        self.descripcionEntry = ttk.Entry(self.frame, width=20)
        self.descripcionEntry.grid(row=5, column=1)

        ttk.Label(self.frame, text="Monto:").grid(row=6, column=0, sticky=tk.W)
        self.montoEntry = ttk.Entry(self.frame, width=20)
        self.montoEntry.grid(row=6, column=1)

        self.agregarItem_btn = ttk.Button(self.frame, text="Agregar Item")
        self.agregarItem_btn.grid(row=7, column=0, columnspan=3)

        self.calcularTotalBtn = ttk.Button(self.frame, text="Calcular Total")
        self.calcularTotalBtn.grid(row=8, column=0, columnspan=3)

        self.reiniciarBtn = ttk.Button(self.frame, text="Reiniciar")
        self.reiniciarBtn.grid(row=9, column=0, columnspan=3)

        ttk.Label(self.frame, text="Resultados:").grid(row=10, column=0, sticky=tk.W)
        self.resultadosTreeview = ttk.Treeview(
            self.frame, columns=("Miembro", "Deuda", "Estado"), show="headings", height=9
        )
        self.resultadosTreeview.grid(row=11, column=0, columnspan=3)
        self.resultadosTreeview.heading("Miembro", text="Miembro")
        self.resultadosTreeview.heading("Deuda", text="Deuda")
        self.resultadosTreeview.heading("Estado", text="Estado")

        self.resultadosText = tk.Text(self.frame, height=5, width=50, state="disabled")
        self.resultadosText.grid(row=12, column=0, columnspan=3)

        self.guardarArchivoBtn = Button(root, text="Guardar archivo de resultados", width=25)
        self.guardarArchivoBtn.grid(row=6, column=0, pady=10)