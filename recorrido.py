import pyarrow
import pandas as pd

def recorrido(alteraciones=pd.DataFrame(),cadenaModificar = "ATGCCACTCTA",movs={"chunk": 3,"salto" : 2}):
    df = pd.DataFrame()
    alteraciones.sort_values(by=[0])
    print(alteraciones['posicion'])
    cadenas=[]
    for i in range (0,len(cadenaModificar) - movs["chunk"] +  1,movs["salto"]):
        temp = ""
        for j in range(i, i+movs["chunk"]):
            temp = temp + cadenaModificar[j]
        cadenas.append(temp)
    df["Cadenas"] = cadenas
    df.to_csv("csv_temp.csv",index=False)

# recorrido()

