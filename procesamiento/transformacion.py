import pandas as pd

def transformar_datos(almacen_datos):

    print("  > Resumen de sobrevivientes Titanic...")
    df_titanic = almacen_datos['Titanic']
    resumen_titanic = df_titanic.groupby('2urvived').size().reset_index(name='Conteo')
    resumen_titanic['2urvived'] = resumen_titanic['2urvived'].map({0: 'No sobrevivió', 1: 'Sobrevivió'})
    almacen_datos['Titanic_Resumen'] = resumen_titanic

    print("  > Creando UniqueKey en Libros...")
    df_libros = almacen_datos['Libros']
    df_libros['UniqueKey'] = df_libros['key'].str.extract(r'(\w+)$')
    almacen_datos['Libros'] = df_libros

    print("  > Promedio de temperatura en Clima...")
    df_clima = almacen_datos['clima']
    resumen_clima = df_clima.select_dtypes(include='number').mean().reset_index()
    resumen_clima.columns = ['Columna', 'Promedio']
    almacen_datos['Clima_Resumen'] = resumen_clima

    print("  > Eliminando pasajeros menores de 10 años...")
    almacen_datos['Titanic'] = almacen_datos['Titanic'][almacen_datos['Titanic']['Age'] >= 10].reset_index(drop=True)

    return almacen_datos