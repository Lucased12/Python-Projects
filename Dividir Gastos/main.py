# Github: https://github.com/Lucased12

import json
from tkinter import Tk
from disenio import Aplicacion

class Logica:

    def __init__(self, app):
        self.app = app
        self.miembros = []  
        self.items = []     

        self.asociarEventos()
        self.cargarDatos()

    def asociarEventos(self):
        
        self.app.agregarMiembroBtn.config(command=self.agregarMiembro)
        self.app.agregarItem_btn.config(command=self.agregarItem)
        self.app.calcularTotalBtn.config(command=self.calcularTotal)
        self.app.reiniciarBtn.config(command=self.reiniciar)
        self.app.guardarArchivoBtn.config(command=self.guardarArchivoResultados)


    def guardarDatos(self, archivo="datos.json"):
        
        datos = {
            "miembros": self.miembros,
            "items": self.items
        }
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)  

    def cargarDatos(self, archivo="datos.json"):
        
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.miembros = datos["miembros"]
                self.items = datos["items"]
                self.actualizarUi()
        except FileNotFoundError:
            print("No se encontró un archivo de datos previo, iniciando desde cero.")
        except json.JSONDecodeError:
            print("Hay un problema con los datos. Reiniciando datos.")



    def actualizarUi(self):
        
        #actualizar lista de miembros
        self.app.miembrosListbox.delete(0, "end")
        for miembro in self.miembros:
            self.app.miembrosListbox.insert("end", miembro)

        #actualizar combobox de pagadores
        self.app.pagadorCombobox["values"] = self.miembros


    def validarMiembro(self, miembro):

        #verificar que ningun miembro este null o duplicado
        if not miembro:
            return "Error: El miembro no puede estar vacío."
        if miembro in self.miembros:
            return "Error: Miembro duplicado."
        return None

    def validarMonto(self, montoTexto):
        
        try:
            monto = float(montoTexto.strip())
            if monto <= 0:
                return None, "Error: El monto debe ser mayor a 0."
            return monto, None
        except ValueError:
            return None, "Error: El monto debe ser un numero, poner un numero porfis."

    def obtenerParticipantes(self):
        
        seleccionados = self.app.miembrosListbox.curselection()
        if not seleccionados:
            return None, "Error: Seleccionar al menos un miembro."
        return [self.miembros[i] for i in seleccionados], None


    def agregarMiembro(self):
       
        miembro = self.app.miembroEntry.get().strip()
        error = self.validarMiembro(miembro)
        if error:
            self.mostrar_resultado(error)
            return

        #agregar miembro a la lista
        self.miembros.append(miembro)
        self.actualizarUi()

        self.app.miembroEntry.delete(0, "end")

        self.guardarDatos()

    def agregarItem(self):
        
        descripcion = self.app.descripcionEntry.get().strip()
        monto, error = self.validarMonto(self.app.montoEntry.get())
        if error:
            self.mostrarResultado(error)
            return

        participantes, error = self.obtenerParticipantes()
        if error:
            self.mostrarResultado(error)
            return

        pagador = self.app.pagadorCombobox.get()
        if not pagador:
            self.mostrarResultado("Error: Selecciona quien pago.")
            return

        #registrar el item
        self.items.append({
            "descripcion": descripcion,
            "monto": monto,
            "pagador": pagador,
            "participantes": participantes
        })

        #limpiar entrys
        self.app.descripcionEntry.delete(0, "end")
        self.app.montoEntry.delete(0, "end")


        self.mostrarResultado(f"Ítem agregado: {descripcion} por ${monto:.2f}")
        self.guardarDatos()

    def calcularTotal(self):
        
        if not self.items:
            self.mostrarResultado("No hay ítems para calcular.")
            return

        #crear un diccionario para saber el dinero de cada uno
        deudas = {miembro: 0 for miembro in self.miembros}

        #calcular deudas
        for item in self.items:
            monto_por_persona = item["monto"] / len(item["participantes"])
            for participante in item["participantes"]:
                if participante != item["pagador"]:
                    deudas[participante] += monto_por_persona
            deudas[item["pagador"]] -= item["monto"]

        #actualizar resultados en la interfaz
        self.app.resultadosTreeview.delete(*self.app.resultadosTreeview.get_children())
        for miembro, deuda in deudas.items():
            estado = "Debe" if deuda > 0 else "Pagó de más" if deuda < 0 else "Equilibrado"
            self.app.resultadosTreeview.insert("", "end", values=(miembro, f"${abs(deuda):.2f}", estado))

    def reiniciar(self):
        
        self.miembros = []
        self.items = []
        self.actualizarUi()
        self.app.resultadosTreeview.delete(*self.app.resultadosTreeview.get_children())
        self.mostrarResultado("Datos reiniciados.")
        self.guardarDatos()

    def mostrarResultado(self, texto):
        
        self.app.resultadosText.config(state="normal")
        self.app.resultadosText.delete("1.0", "end")
        self.app.resultadosText.insert("1.0", texto)
        self.app.resultadosText.config(state="disabled")

            #Verificar-----------------------------------

    def guardarDatos(self, archivo="datos.json"):
        
        totalGastos = sum(item["monto"] for item in self.items)
        balances = self.calcularBalances()

        datos = {
            "miembros": self.miembros,
            "items": self.items,
            "calculos": {
                "totalGastos": totalGastos,
                "balances": balances
            }
        }

        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)  #para el formato

    def calcularBalances(self):
       
        deudas = {miembro: 0 for miembro in self.miembros}

        for item in self.items:
            montoPorPersona = item["monto"] / len(item["participantes"])
            for participante in item["participantes"]:
                if participante != item["pagador"]:
                    deudas[participante] += montoPorPersona
            deudas[item["pagador"]] -= item["monto"]

        balances = []
        for miembro, balance in deudas.items():
            estado = "Debe" if balance > 0 else "Pago de mas" if balance < 0 else "Equilibrado"
            balances.append({"miembro": miembro, "balance": round(balance, 2), "estado": estado})

        return balances

    def guardarArchivoResultados(self):
        
        if not self.items:
            self.mostrarResultado("Error: No hay datos para guardar.")
            return

        #generar los datos organizados
        totalGastos = sum(item["monto"] for item in self.items)
        balances = self.calcularBalances()

        datos = {
            "miembros": self.miembros,
            "items": self.items,
            "calculos": {
                "totalGastos": totalGastos,
                "balances": balances
            }
        }

        archivo = "resultadosCalculo.json"
        try:
            with open(archivo, "w") as f:
                json.dump(datos, f, indent=4)
            self.mostrarResultado(F"Archivo guardado exitosamente como {archivo}.") #para el formato json (f)
        except Exception as e:
            self.mostrarResultado(f"Error al guardar el archivo: {e}")


if __name__ == "__main__":
    root = Tk()
    app = Aplicacion(root)
    Logica(app)
    root.mainloop()
