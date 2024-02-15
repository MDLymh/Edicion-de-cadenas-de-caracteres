def recorrido(cadenaModificar = "ATGCCACTCTA", chunk = 3, salto = 2):
    for i in range (0,len(cadenaModificar) - chunk +  1,salto):
        temp = ""
        for j in range(i, i+chunk):
            temp = temp + cadenaModificar[j]
        print(temp)
recorrido()

