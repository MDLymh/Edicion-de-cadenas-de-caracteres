import pyarrow
import pandas as pd

def recorrido(alteraciones=pd.DataFrame(),cadenaModificar = "ATGCCACTCTA",movs={"chunk": 3,"salto" : 2}):
    
    alteraciones = alteraciones.sort_values(by='posicion')
    alteraciones = alteraciones.reset_index()
    del alteraciones["index"]
    indiceInicio=[]
    cadenas=[]
    indiceMod=[]
    indiceRel=[]
    for i in range (0,len(cadenaModificar) - movs["chunk"] +  1,movs["salto"]):
        temp = ""
        banderaPosicioAlteraciones = 0
        posicionMayor = len(alteraciones["posicion"].to_list())
        for j in range(i, i+movs["chunk"]):
            if (i <= alteraciones["posicion"][banderaPosicioAlteraciones]):
                temp = cadenaModificar[i:i +movs["chunk"] +1]
                indiceRelativo =j - i
                if j in alteraciones['posicion'].values:
                    alteracionIndex = alteraciones['posicion'].to_list().index(j)
                    if temp[indiceRelativo] ==alteraciones['referencia'][alteracionIndex]:
                        temp = list(temp)
                        temp[indiceRelativo] = alteraciones['alteracion'][alteracionIndex]
                        temp = "".join(temp)
                        indiceMod.append(j)
                        indiceRel.append(indiceRelativo)
                        indiceInicio.append(i)
                        cadenas.append(temp)
                        print(cadenas)
                        print("{}, {}, {}, {}, ".format(len(cadenas),len(indiceMod),len(indiceRel),len(indiceInicio)))
                        banderaPosicioAlteraciones += 1
            else:
                break
                
            # if j in alteraciones['posicion'].values:
            #     alteracionIndex = alteraciones['posicion'].to_list().index(j)
            #     if cadenaModificar[j] == alteraciones['referencia'][alteracionIndex]:
            #         temp = temp + alteraciones['alteracion'][alteracionIndex]
            # else:
            #     temp = temp + cadenaModificar[j]
        cadenas.append(temp)
    datos={
        "ind_ini": indiceInicio,
        "cadenas_modificadas": cadenas,
        "indice_modificado": indiceMod,
        "indice_relativo": indiceRel
    }
    #df = pd.DataFrame(datos)
    # df["indice_inicio"]= indiceInicio
    # df["cadenas_modificadas"] = cadenas
    # df["indice_modificado"] =indiceMod
    # df["indice_relativo"] = indiceRel
    #df.to_csv("csv_temp.csv",index=False)

# recorrido()

