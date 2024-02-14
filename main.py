import gestionArchivos as ga
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from os import getlogin


FONT = "Arial 16"
PADDING =15
RUTA_FOLDER_IMG = "imgs/folder.png"

def abrirExplorador(textBox):
    archivo = filedialog.askopenfilename(title="Abrir archivo", 
                                         initialdir="C:/users/{}".format(getlogin()),
                                         filetypes=(("Archivos CSV","*.csv"),("Todos los archivos","*.*")))
    textBox.delete(0,len(textBox.get()))
    textBox.insert(0,archivo)

def main():
    ventanaRaiz = Tk()
    ventanaRaiz.title("Modificador de cadenas")
    ventanaRaiz.geometry("600x300")
    etiquetaRuta = ttk.Label(ventanaRaiz, text="Selecciona el archivo: ",font=FONT, padding=PADDING)
    frameRuta = ttk.Frame(ventanaRaiz, padding=PADDING)
    textBoxRuta = ttk.Entry(frameRuta, font = FONT)
    folderImg = ImageTk.PhotoImage(Image.open(RUTA_FOLDER_IMG))
    botonRuta = ttk.Button(frameRuta,image=folderImg, command = lambda: abrirExplorador(textBoxRuta))
    botonContinuar =ttk.Button(ventanaRaiz,text="Continuar",command= lambda: ga.continuarProcesarArchivo(textBoxRuta.get()))

    etiquetaRuta.grid(column=0,row=0)
    frameRuta.grid(column=0,row=1)
    textBoxRuta.grid(column=0,row=0)
    botonRuta.grid(column=1,row=0)
    botonContinuar.grid(column=1,row=2)

    ventanaRaiz.mainloop()


if __name__ == "__main__":
    main()