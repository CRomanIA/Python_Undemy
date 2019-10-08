"""Sec15cap49
    Libreria tkinter
Interfaz Grafica para visualizar y trabajar con nuestro programa
Los componentes que tiene son:
    Tk: Componente raiz
    Frame: Marco que puede contener otros widgets
    Label: Etiqueta de Texto
    Entry: Campo de Texto Sencillo para Escribir Texto Corto
    Text: Campo de Texto grande para escribir varias lineas de Texto, como un campo comentario
    Button: boton donde se pueden realizar clic
    RadioButton: Boton para elegir una opcion entre varias opciones
    CheckButton: Es un boton para marvcar de tipo "tic" (Activado/Desactivado)
    Menu: es un componente para crear los menús de las aplicaciones
    Dialogs: Es un componente para crear ventanas emergentes para mostrar informacion al usuario, 
            como alertas y confirmaciones
        """
#Libreria tkinter
import tkinter
from tkinter import messagebox
from tkinter import filedialog

#Sec14cap50 Tkinter - Componente Raiz
def Sec15cap50():
    raiz = tkinter.Tk()
    raiz.title("Mi primer titulo de raiz ")

    raiz.mainloop()
#Sec15cap50()


#Sec15cap51 Tkinter - Componente Frame
def Sec15cap51():
    raiz = tkinter.Tk()
    raiz.title("Mi Programa")
    #Creamos componente frame
    frame = tkinter.Frame(raiz)
    frame.config(bg="blue", width=400, height=300)
    
    frame.pack() ##End frame

    raiz.mainloop()##End main
#Sec15cap51()

#Sec15cap52 Tkinter - Componente label
def Sec15cap52():
    main = tkinter.Tk()
    main.title("Mi Programa")
    #Creamos componente label
    text = "wena choro"
    label = tkinter.Label(main, text= text)
    label.config(fg="green", bg="lightgrey", font=("Cortana",30)) 
    
    label.pack() ##End label 
    main.mainloop()##End main
#Sec15cap52()

#Sec15cap53 Tkinter - Componente entry (texto corto para la entrada de datos por teclado)
def Sec15cap53():
    main = tkinter.Tk()
    main.title("Mi Programa")
    #Creamos componente entry
    entry = tkinter.Entry(justify="center")
    entry2 = tkinter.Entry(justify="center", show="*") ##Para utilizar contraseñas? :O
        
    entry.pack() ##End entry 
    entry2.pack()
    main.mainloop()##End main
#Sec15cap53()

#Sec15cap54 Tkinter - Componente Texto (texto largo de varias lineas)
def Sec15cap54():
    main = tkinter.Tk()
    main.title("Mi Programa")
    #Creamos componente Text
    entry = tkinter.Text(main)
    entry.config(width=20, height=10, font=("Verdana, 15"), padx=10, fg="green" )

    entry.pack() ##End entry 
    main.mainloop()##End main
#Sec15cap54()

#Sec15cap55 Tkinter - Componente Button 
def Sec15cap55():
    main = tkinter.Tk()
    main.title("Mi Programa")
    #definimos la funcion accion
    def action():
        print("Hola mundo")
    action()
    #Creamos componente Button
    button = tkinter.Button(main, text="Ejecutar", command=action)
    button.config(fg="green")

    button.pack() ##End entry 
    main.mainloop()##End main
#Sec15cap55()

#Sec15cap56 Tkinter - Componente RadioButton 
def Sec15cap56():
    main = tkinter.Tk()
    main.title("Mi Programa")
    #definimos la funcion accion
    def select():
        print("La variable seleccionada es {}".format(option.get()))

    #Creamos componente radioButton
    option = tkinter.IntVar()
    radioButton1 = tkinter.Radiobutton(main, text="Opcion1", variable=option, value=1, command=select)
    radioButton1.pack()

    radioButton2 = tkinter.Radiobutton(main, text="Opcion2", variable=option, value=2, command=select)
    radioButton2.pack()
    
    radioButton3 = tkinter.Radiobutton(main, text="Opcion3", variable=option, value=3, command=select)
    radioButton3.pack()
    
    main.mainloop()##End main
#Sec15cap56()

#Sec15cap57 Tkinter - Componente CheckButton 
def Sec15cap57():
    main = tkinter.Tk()
    main.title("Mi Programa")
    #definimos el metodo de verificacion
    def verify():
        valor = check1.get()
        if(valor == 1):
            print("El check Está activado")
        else:
            print("El check Está desactivado")

    #Creamos componente checkButton
    check1 = tkinter.IntVar()

    button1 = tkinter.Checkbutton(main, text="opcion 1", variable=check1, onvalue=1, offvalue=0, command=verify)
    button1.pack()

    main.mainloop()##End main
#Sec15cap57()

#Sec15cap58 Tkinter - Componente messageBox 
def Sec15cap58():
    main = tkinter.Tk()
    main.title("Mi Programa")
    #Creamos metodo con notificacion
    def notify():
        tkinter.messagebox.showinfo("Titulo", "Mensaje con la info qla")
    #Creamos componente popup (Ventana de información)
    button = tkinter.Button(main, text="Pulsar para aviso", command=notify)
    button.pack()

    main.mainloop()##End main
#Sec15cap58()

#Sec15cap59 Tkinter - Componente messageBox 
def Sec15cap59():
    main = tkinter.Tk()
    main.title("Mi Programa")
    #Creamos metodo con notificacion
    def ask():
        resultado = tkinter.messagebox.askquestion("Titulo", "Mensaje con la info qla")
        if(resultado == "yes"):
            print("Si, quiero borrar el fichero")
        else:
            print("No, no quiero borrar el fichero")
    
    #Creamos componente popup (Ventana de información)
    button = tkinter.Button(main, text="Pulsar para preguntar", command=ask)
    button.pack()

    main.mainloop()##End main
#Sec15cap59()

#Sec15cap60 Tkinter - filedialog para abrir un fichero
def Sec15cap60():
    main = tkinter.Tk()
    main.title("Mi Programa")
    
    #Creamos metodo para abrir fichero
    def openfile():
        routeFile = filedialog.askopenfilename(tittle = "abrir un fichero")
        print(routeFile)

    #Creamos componente popup (Ventana de información)
    button = tkinter.Button(main, text="Pulsar para empezar", command=openfile)
    button.pack()

    main.mainloop()##End main
#Sec15cap60()