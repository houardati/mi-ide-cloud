# mi-ide-cloud
# Documentación de Transformaciones de Datos - Pipeline de Ingesta

Este proyecto implementa un orquestador de datos que integra múltiples fuentes (CSV, API Batch y Tiempo Real) y aplica una serie de transformaciones lógicas antes de consolidar el almacén de datos final.

## 1. Transformaciones Aplicadas (`transformacion.py`)

Se han implementado cuatro procesos de limpieza y enriquecimiento en la función `transformar_datos`:

### A. Enriquecimiento de Librería (UniqueKey)
* **Entrada:** `almacen_datos['Libros']`
* **Acción:** Se crea una nueva columna llamada `UniqueKey`.
* **Lógica:** Se extrae el identificador alfanumérico final de la columna original `key` utilizando expresiones regulares (`(\w+)$`).
* **Resultado:** La entrada `Libros` se actualiza incluyendo esta nueva llave única para cada ejemplar.

### B. Resumen de Temperatura (Clima)
* **Entrada:** `almacen_datos['clima']`
* **Acción:** Generación de una tabla resumen con promedios.
* **Lógica:** Se seleccionan únicamente las columnas de tipo numérico y se calcula su media aritmética.
* **Resultado:** Se crea una nueva entrada en el almacén llamada `Clima_Resumen`.

### C. Limpieza de Datos Titanic
* **Entrada:** `almacen_datos['Titanic']`
* **Acción:** Filtrado de registros por edad.
* **Lógica:** Se eliminan todas las filas donde la columna `Age` sea menor a 10 años. Se realiza un reset del índice para mantener la integridad.
* **Resultado:** La entrada `Titanic` se actualiza conservando solo pasajeros de 10 años o más.

### D. Reporte de Sobrevivientes
* **Entrada:** `almacen_datos['Titanic']`
* **Acción:** Mapeo y conteo de categorías.
* **Lógica:** Se agrupan los datos por la columna de supervivencia, renombrando los valores numéricos a etiquetas legibles ("Sobrevivió" / "No sobrevivió").
* **Resultado:** Se almacena en `Titanic_Resumen`.

## 2. Orquestador de Ejecución (`main.py`)

El orquestador gestiona el flujo completo del pipeline:

1.  **Ingesta Multi-fuente:**
    * Lectura de archivos CSV (Titanic).
    * Consulta a API de libros en modo Batch.
    * Captura de 5 instantáneas de clima en tiempo real con intervalos de 1 segundo.
2.  **Visualización Inicial:** Muestra un resumen técnico (filas y columnas) de los datos brutos.
3.  **Ejecución de Transformaciones:** Llama de forma centralizada a la lógica definida en `transformacion.py`.
4.  **Resumen Final:** Despliega en consola el estado actual del `almacen_datos`, listando todas las entradas disponibles, incluyendo las nuevas tablas de resumen creadas.

---
**Nota:** Todas las transformaciones aseguran la actualización directa del diccionario `almacen_datos`, facilitando la disponibilidad de la información para procesos posteriores de análisis o carga.