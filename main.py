import pandas as pd
from pathlib import Path

path = input('ARCHIVO EXCEL\n')
path = path.replace("'", '')
sheet= input('HOJA\n')

    

if path != '' and sheet!= '':
    df = pd.read_excel(io = path, sheet_name=sheet)
   
elif path != '':
    df = pd.read_excel(io = path)
    index = df.index
    col = df.columns
    data = {}
    saved = []
    for j in range(0,len(col)):
            c = col[j]
            data[c] = []

    
    for i in range(0,len(index)):
        if not df.iloc[i]['COLUMNA A'] in saved:
            saved.append(df.iloc[i]['COLUMNA A'])
            for j in range(0,len(col)):
                c = col[j]
                data[c].append(df.iloc[i][c])
               
            
    new = pd.DataFrame(data)
    new.to_excel('output.xlsx', index=False)
