import pandas as pd

def leer_datos_csv():
    sourse="Titanic.csv"
    df=pd.read_csv(sourse)
    print(f'total lineas importadas: {len(df)}')
    return df