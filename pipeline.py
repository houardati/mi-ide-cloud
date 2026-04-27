import pandas as pd
import time

from ingestion.lectura_csv import leer_datos_csv
from ingestion.leer_batch import leer_datos_batch
from ingestion.fuente_realtime import leer_clima_tiempo_real
from procesamiento.transformacion import transformar_datos  # <-- nuevo

def run_orchestator():

    almacen_datos = {}

    print("--- Lectura de csv")
    almacen_datos['Titanic'] = leer_datos_csv()

    print("--- Lectura de titulos libros")
    almacen_datos['Libros'] = leer_datos_batch('scifi')

    print("--- Lectura del clima en tiempo real")
    total_lecturas = []

    for i in range(5):
        print(f"  > instantanea {i+1}...")
        df_snap = leer_clima_tiempo_real()
        if not df_snap.empty:
            total_lecturas.append(df_snap)
        time.sleep(1)

    if total_lecturas:
        almacen_datos['clima'] = pd.concat(total_lecturas, ignore_index=True)
    else:
        almacen_datos['clima'] = pd.DataFrame()

    print("--- Resumen de datos sin transformar")
    for elemento, df in almacen_datos.items():
        print(f"\n📍 FUENTE: {elemento}")
        if not df.empty:
            print(f"Rows: {len(df)} | Columns: {list(df.columns)}")
            print(df.head(2))
        else:
            print("Empty Table (Check connection)")

    # -- Transformaciones --
    print("\n--- Ejecutando transformaciones")
    almacen_datos = transformar_datos(almacen_datos)  # <-- nuevo

    # -- Resumen final --
    print("\n--- Resumen final de almacen_datos")
    for elemento, df in almacen_datos.items():
        print(f"\n📍 ENTRADA: {elemento}")
        if not df.empty:
            print(f"Rows: {len(df)} | Columns: {list(df.columns)}")
            print(df.head(2))
        else:
            print("Empty Table")

    return almacen_datos

if __name__ == "__main__":
    results = run_orchestator()