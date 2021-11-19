from tkinter import Entry, Tk,Text,Button,END
import random
import string

class Interfaz:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Generador de contraseñas")
        self.ventana.geometry('300x150')

        #Creamos la salida de los datos 
        self.pantalla = Text(ventana, state="disabled", width=25, height=1,background="gray",foreground="white", font=("Helvatica", 15))

        # Creamos caja para pedir datos y salida de datos
        self.datos = Text(ventana, state="normal", width=10, height=1)

        # Ubicamos las  cajas
        self.datos.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=7, pady=5)

        # Agrega los botones
        boton1= self.crearBoton("Generar")
        boton2= self.crearBoton("Limpiar")

        #Ubicar botones
        boton1.grid(row=2, column=0, padx=15, pady=5)
        boton2.grid(row=2, column=2, padx=5, pady=30)

    
    # Creamos los botones
    def crearBoton(self, valor, escribir=True):
        return Button(self.ventana, text=valor,width=10,height=1,font=("Helvatica", 10),command=lambda:self.click(valor,escribir))
    
    def click(self, escribir, valor):
        # Si valor es verdadero
        if valor:
            # Con el try except lo que haremos es validar que solo se ingresen numeros
            try:
                # Configuramos el boton de generar
                if escribir == "Generar":
                    numeros = self.datos.get("1.0", END)
                    datos= int(numeros)
                    self.limpiarPantalla()
                    self.generarContraseña(datos)
                #Configuramos el boton de limpiar pantalla
                elif escribir == "Limpiar":
                    self.limpiarPantalla()
            except:
                self.limpiarPantalla()
                dato = "Solo se adminten numeros"
                self.mostrarEnPantalla(dato)
        #Mostramos un error
        else:
            dato = "No se ha asignado un tamaño para la contraseña"
            self.mostrarEnPantalla(dato)
        return


    #Creamos la funcion de limpiar la pantalla
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

    #Creamos la funcion generar Contraseña
    def generarContraseña(self, datos):
        # Declaramos una variable llamada datos la cual va a llevar letras - digitos - signos de puntuacion
        dato = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
        password = []

        # creamos un ciclo en el cual vamos a llevar la tupla con los datos random generados en temporal
        for i in range(1, datos):
            temporal = random.choice(dato)
            password.append(temporal)
        
        # Creamos una variable resultado en la cual vamos a unir password a una string
        resultado = "".join(password)

        # Mandamos el resultado para mostrarlo en pantalla y borramos lo que esta en el recuadro de pedir datos
        self.mostrarEnPantalla(resultado)
        self.datos.delete("1.0", END)
 
    # Mostramos en pantalla el contenido
    def mostrarEnPantalla(self, resultado):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END,resultado)
        self.pantalla.configure(state="disabled")
        return

ventana_principal = Tk()
generador =  Interfaz(ventana_principal)
ventana_principal.mainloop()