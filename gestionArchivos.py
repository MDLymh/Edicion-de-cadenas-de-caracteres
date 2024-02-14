from tkinter import messagebox
from os import path
import pandas as pd

def procesarArchivo(rutaArchivo):
    df = pd.read_csv(rutaArchivo,sep = ',',header=None)
    print(df)

def continuarProcesarArchivo(textoRuta):
    if len(textoRuta)==0:
        messagebox.showinfo("Alerta", "El campo de ruta esta Vacio")
    elif not path.isfile(textoRuta):
        messagebox.showinfo("Alerta", "El archivo no existe o ha sido eliminado")
    else:
        procesarArchivo(textoRuta)
