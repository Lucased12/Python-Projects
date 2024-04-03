import tkinter as tk
from plyer import notification

class AplicacionPomodoro:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro App")

        #Var para guardar los tiempos de trabajar y descansar
        self.tiempoTrabajo = tk.StringVar(value="")
        self.tiempoDescanso = tk.StringVar(value="")

        #Var para mostrar el tiempo restante en la interfaz
        self.tiempoRestante = tk.StringVar(value="00:00")

        #Var para ver si el temporizador está funcionando
        self.enFuncionamiento = False

        #Var para almacenar el tiempo restante actual
        self.tiempoRestanteActual = 0

        #Var para mantener el estado actual del temporizador (trabajar o descansar)
        self.tareaActual = None

        #Crear widgets de la interfaz
        self.crearWidgets()

    def crearWidgets(self):
        #Crear etiquetas y cajas de texto para poner los tiempos de trabajar y descansar
        self.crearEtiquetasYCajasDeTexto()
        #Crear botones
        self.crearBotones()
        #Crear etiqueta para mostrar el tiempo restante
        self.crearEtiquetaTiempo()

    def crearEtiquetasYCajasDeTexto(self):
        #Crear etiquetas y cajas de texto para los tiempos de trabajar y descansar
        tk.Label(self.master, text="Tiempo de trabajo (min):").grid(row=0, column=0)
        tk.Entry(self.master, textvariable=self.tiempoTrabajo).grid(row=0, column=1)
        tk.Label(self.master, text="Tiempo de descanso (min):").grid(row=1, column=0)
        tk.Entry(self.master, textvariable=self.tiempoDescanso).grid(row=1, column=1)

    def crearBotones(self):
        #Crear botones para iniciar, detener, reiniciar y reanudar el temporizador
        self.botonTrabajo = tk.Button(self.master, text="Empezar trabajo", command=self.iniciarTemporizadorTrabajo)
        self.botonTrabajo.grid(row=2, column=0)
        self.botonDescanso = tk.Button(self.master, text="Empezar descanso", command=self.iniciarTemporizadorDescanso)
        self.botonDescanso.grid(row=2, column=1)
        self.botonDetener = tk.Button(self.master, text="Detener", command=self.detenerTemporizador, state="disabled")
        self.botonDetener.grid(row=3, column=0, columnspan=2)
        self.botonReiniciar = tk.Button(self.master, text="Reiniciar", command=self.reiniciarTemporizador)
        self.botonReiniciar.grid(row=4, column=0, columnspan=2)
        self.botonReanudar = tk.Button(self.master, text="Reanudar", command=self.reanudarTemporizador, state="disabled")
        self.botonReanudar.grid(row=5, column=0, columnspan=2)

    def crearEtiquetaTiempo(self):
        #Crear etiqueta para mostrar el tiempo restante
        tk.Label(self.master, textvariable=self.tiempoRestante).grid(row=6, column=0, columnspan=2)

    def iniciarTemporizadorTrabajo(self):
        #Función para iniciar el temporizador de trabajar
        if not self.enFuncionamiento:
            self.enFuncionamiento = True
            self.tareaActual = "trabajo"
            self.tiempoRestanteActual = int(self.tiempoTrabajo.get()) * 60
            self.actualizarTiempo()
            self.desactivarBotones()

    def iniciarTemporizadorDescanso(self):
        #Función para iniciar el temporizador de descanso
        if not self.enFuncionamiento:
            self.enFuncionamiento = True
            self.tareaActual = "descanso"
            self.tiempoRestanteActual = int(self.tiempoDescanso.get()) * 60
            self.actualizarTiempo()
            self.desactivarBotones()

    def detenerTemporizador(self):
        #Función para detener el temporizador
        self.enFuncionamiento = False
        self.habilitarBotonReanudar()
        self.desactivarBotonDetener()

    def reiniciarTemporizador(self):
        #Función para reiniciar el temporizador
        self.enFuncionamiento = False
        self.tiempoRestante.set("00:00")
        self.habilitarBotones()
        self.desactivarBotonReanudar()

    def reanudarTemporizador(self):
        #Función para reanudar el temporizador
        self.desactivarBotones()
        self.habilitarBotonDetener()
        self.desactivarBotonReanudar()
        self.enFuncionamiento = True
        self.actualizarTiempo()

    def mostrarNotificacion(self, titulo, mensaje):
        #Función para mostrar notificación cuando el temporizador llega a cero
        notification.notify(
            title=titulo,
            message=mensaje,
            app_name="Pomodoro",
            app_icon=None,
            timeout=10
        )

    def actualizarTiempo(self):
        #Función para actualizar el tiempo restante en la interfaz
        if self.enFuncionamiento and self.tiempoRestanteActual > 0:
            mins, secs = divmod(self.tiempoRestanteActual, 60)
            formatoTiempo = '{:02d}:{:02d}'.format(mins, secs)
            self.tiempoRestante.set(formatoTiempo)
            self.tiempoRestanteActual -= 1
            self.master.after(1000, self.actualizarTiempo)
        elif self.enFuncionamiento and self.tiempoRestanteActual == 0:
            self.detenerTemporizador()
            if self.tareaActual == "trabajo":
                self.mostrarNotificacion("Trabajo Terminado", "¡Vamos a descansar un rato!")
            elif self.tareaActual == "descanso":
                self.mostrarNotificacion("Descanso Terminado", "¡Vamos a seguir trabajando!")
            self.reiniciarTemporizador()


    def desactivarBotones(self):
        #Función para deshabilitar botones mientras el temporizador está funcionando
        self.botonTrabajo.config(state="disabled")
        self.botonDescanso.config(state="disabled")
        self.botonDetener.config(state="normal")

    def habilitarBotones(self):
        #Función para habilitar botones después de detener o reiniciar el temporizador
        self.botonTrabajo.config(state="normal")
        self.botonDescanso.config(state="normal")

    def desactivarBotonDetener(self):
        #Función para deshabilitar el botón de detener
        self.botonDetener.config(state="disabled")

    def habilitarBotonDetener(self):
        #Función para habilitar el botón de detener
        self.botonDetener.config(state="normal")

    def desactivarBotonReanudar(self):
        #Función para deshabilitar el botón de reanudar
        self.botonReanudar.config(state="disabled")

    def habilitarBotonReanudar(self):
        #Función para habilitar el botón de reanudar
        self.botonReanudar.config(state="normal")

#Crear la ventana principal de la app
root = tk.Tk()
mi_app = AplicacionPomodoro(root)
root.mainloop()
