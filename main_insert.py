import pandas as pd
from datetime import datetime

#LOS INPUTS PUEDEN SER REEMPLAZADOS POR STRINGS DIRECTAMENTE
#RUTA DEL ARCHIVO EXCEL
path = input('ARCHIVO EXCEL\n')
path = path.replace("'", '')
#NOMBRE DE LA HOJA
#sheet= input('NOMBRE DE LA HOJA(OPCIONAL)\n')
sheet = 'insertarSalto'
#NOMBRE DE LA COLUMNA
#columna = input('NOMBRE DE LA COLUMNA A EVALUEAR\n')
columna = 'COLUMNA B'
#ELIMANR DUPLICADO O COPIAR UNA SOLA VEZ
#del_reg = int(input('0: Copiar si duplicados\n1: Eliminar duplicados\n'))

if path != '' and sheet!= '':
    df = pd.read_excel(io = path, sheet_name=sheet)

    index = df.index
    col = df.columns
    data = {}
    saved = []
    for j in range(0,len(col)):
            c = col[j]
            data[c] = []

    
    for i in range(0,len(index)):
        if True:#not df.iloc[i][columna] in saved:
            #saved.append(df.iloc[i][columna])
            for j in range(0,len(col)):
                c = col[j]
                data[c].append(df.iloc[i][c])
                data[c].append("")
                data[c].append("")
        
        
        elif False:#del_reg:
            try:
                index = data[columna].index(df.iloc[i][columna])

                for j in range(0,len(col)):
                    c = col[j]
                    del data[c][index]   
            
            except ValueError:
                print(ValueError)

    
    new = pd.DataFrame(data)
    new.to_excel(f'{datetime.now()}_output.xlsx', index=False)
