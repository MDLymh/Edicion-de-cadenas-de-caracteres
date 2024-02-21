from tkinter import messagebox
from os import path
import pandas as pd
from recorrido import recorrido as rc

def procesarArchivo(rutaArchivo):
    df = pd.read_csv(rutaArchivo,sep = ',',index_col=False)
    cadenaModificar = df["string_a_modificar"][0]
    del df["string_a_modificar"]
    rc(df,cadenaModificar,{"chunk": 10,"salto": 5})


def continuarProcesarArchivo(textoRuta):
    if len(textoRuta)==0:
        messagebox.showinfo("Alerta", "El campo de ruta esta Vacio")
    elif not path.isfile(textoRuta):
        messagebox.showinfo("Alerta", "El archivo no existe o ha sido eliminado")
    else:
        procesarArchivo(textoRuta)
