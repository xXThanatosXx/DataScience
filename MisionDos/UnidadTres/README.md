

### DataFrames y Series

Un analista de marketing quiere analizar las ventas de productos en diferentes tiendas.

```python
import pandas as pd

# Crear una Serie de ventas de un producto en una tienda
ventas_serie = pd.Series([200, 300, 250, 400], index=['Tienda A', 'Tienda B', 'Tienda C', 'Tienda D'])

# Crear un DataFrame de ventas de varios productos en diferentes tiendas
data = {'Tienda A': [200, 210, 220],
        'Tienda B': [300, 320, 330],
        'Tienda C': [250, 260, 270]}
ventas_df = pd.DataFrame(data, index=['Producto 1', 'Producto 2', 'Producto 3'])

print(ventas_serie)
print(ventas_df)

```
### Cargar y exportar datos
Un investigador de salud necesita cargar datos de un archivo CSV que contiene información de pacientes y luego guardar un subconjunto de esos datos en otro archivo.

Local
```python
import pandas as pd

# Cargar datos desde un archivo CSV
df = pd.read_csv('datos_pacientes.csv')

# Filtrar solo las columnas relevantes
sub_df = df[['Nombre', 'Edad', 'Diagnostico']]

# Exportar el subconjunto de datos a un nuevo archivo CSV
sub_df.to_csv('pacientes_filtrados.csv', index=False)

print("El subconjunto de datos ha sido guardado en 'pacientes_filtrados.csv'.")


```
Google Colab
```python
import pandas as pd
from google.colab import files

# Subir el archivo CSV desde tu computadora
uploaded = files.upload()

# Cargar datos desde el archivo CSV subido
df = pd.read_csv('datos_pacientes.csv')

# Filtrar solo las columnas relevantes
sub_df = df[['Nombre', 'Edad', 'Diagnostico']]

# Exportar el subconjunto de datos a un nuevo archivo CSV
sub_df.to_csv('pacientes_filtrados.csv', index=False)

# Descargar el archivo CSV filtrado
files.download('pacientes_filtrados.csv')

print("El subconjunto de datos ha sido guardado y está listo para descargar.")

```

###  Indexación y selección
Un economista necesita analizar la inflación en un país seleccionando datos específicos de un DataFrame.
```python
import pandas as pd

# Crear un diccionario con los datos de inflación
datos_inflacion = {
    'Año': [2018, 2019, 2020, 2021, 2022, 2023],
    'Inflacion': [1.5, 2.0, 1.2, 3.5, 5.0, 4.3],
    'PIB': [2.5, 2.3, -1.5, 1.0, 3.0, 2.8],
    'Desempleo': [8.5, 8.2, 10.0, 9.0, 7.5, 7.0],
    'Ciudad': ['Madrid', 'Madrid', 'Madrid', 'Madrid', 'Madrid', 'Madrid']
}

# Convertir a DataFrame
inflacion_df = pd.DataFrame(datos_inflacion)

# Mostrar el DataFrame
print("DataFrame completo:")
print(inflacion_df.head())

# Seleccionar la columna de inflación de un DataFrame
inflacion = inflacion_df['Inflacion']
print("\nColumna de Inflación:")
print(inflacion)

# Seleccionar la inflación de un año específico (2023)
inflacion_2023 = inflacion_df.loc[inflacion_df['Año'] == 2023, 'Inflacion']
print("\nInflación en 2023:")
print(inflacion_2023)

# Filtrar datos de años posteriores a 2020
inflacion_post_2020 = inflacion_df[inflacion_df['Año'] > 2020]
print("\nDatos de Inflación posteriores a 2020:")
print(inflacion_post_2020)


```

### Limpieza de datos
Un científico de datos detecta que un conjunto de datos meteorológicos tiene valores faltantes que deben ser tratados.
```python
import pandas as pd

# Crear un DataFrame con datos meteorológicos, incluyendo valores faltantes
datos_meteorologicos = {
    'Fecha': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05'],
    'Temperatura_Maxima': [30.5, 31.0, None, 32.5, 33.0],
    'Temperatura_Minima': [20.1, 21.0, 19.5, None, 20.5],
    'Precipitacion': [0.0, None, 5.2, 3.1, None],
    'Humedad': [60, 65, 70, None, 75]
}

# Convertir a DataFrame
meteorologicos_df = pd.DataFrame(datos_meteorologicos)

# Mostrar el DataFrame inicial
print("DataFrame inicial:")
print(meteorologicos_df)

# Reemplazar valores nulos por la media de la columna
meteorologicos_df['Temperatura_Maxima'] = meteorologicos_df['Temperatura_Maxima'].fillna(meteorologicos_df['Temperatura_Maxima'].mean())
meteorologicos_df['Temperatura_Minima'] = meteorologicos_df['Temperatura_Minima'].fillna(meteorologicos_df['Temperatura_Minima'].mean())
meteorologicos_df['Precipitacion'] = meteorologicos_df['Precipitacion'].fillna(meteorologicos_df['Precipitacion'].mean())
meteorologicos_df['Humedad'] = meteorologicos_df['Humedad'].fillna(meteorologicos_df['Humedad'].mean())

# Mostrar el DataFrame después de reemplazar valores nulos
print("\nDataFrame después de reemplazar valores nulos con la media:")
print(meteorologicos_df)

# Eliminar filas con valores nulos (si aún quedaran)
meteorologicos_df.dropna(inplace=True)

# Eliminar duplicados (aunque en este ejemplo no se espera que haya duplicados)
meteorologicos_df.drop_duplicates(inplace=True)

# Mostrar el DataFrame final
print("\nDataFrame final después de eliminar valores nulos y duplicados:")
print(meteorologicos_df)


```

### Transformación de datos
Un analista financiero desea calcular el retorno anual de una inversión aplicando una función personalizada a los datos.

```python
import pandas as pd

# Crear un DataFrame con precios iniciales y finales de una inversión
datos_inversion = {
    'Fecha': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'Precio_Inicial': [100, 105, 102, 108, 110],
    'Precio_Final': [105, 102, 108, 110, 115]
}

# Convertir a DataFrame
df = pd.DataFrame(datos_inversion)

# Definir una función personalizada para calcular el retorno
def calcular_retorno(precio_inicial, precio_final):
    return (precio_final - precio_inicial) / precio_inicial

# Aplicar la función a cada fila del DataFrame para calcular el retorno
df['Retorno'] = df.apply(lambda row: calcular_retorno(row['Precio_Inicial'], row['Precio_Final']), axis=1)

# Mostrar el DataFrame con el cálculo del retorno
df.head()


```

### Combinación de datos

Un analista de negocios necesita combinar datos de ventas y datos de clientes para entender mejor el perfil de sus compradores.

```python
import pandas as pd

# Crear DataFrame de ventas
ventas_df = pd.DataFrame({
    'Cliente_ID': [1, 2, 3],
    'Venta_Total': [100, 200, 150]
})

# Crear DataFrame de clientes
clientes_df = pd.DataFrame({
    'Cliente_ID': [1, 2, 3],
    'Nombre': ['Juan', 'Maria', 'Pedro']
})

# Combinar ambos DataFrames en uno solo
df_combinado = pd.merge(ventas_df, clientes_df, on='Cliente_ID')

# Mostrar el DataFrame combinado
print(df_combinado)


```

### Reorganización de datos

Un analista de recursos humanos quiere reorganizar un DataFrame para comparar los salarios de empleados en diferentes departamentos.

```python
import pandas as pd

# Crear un DataFrame de salarios por departamento
data = {
    'Departamento': ['Ventas', 'Ventas', 'TI', 'TI'],
    'Empleado': ['Juan', 'Maria', 'Carlos', 'Ana'],
    'Salario': [3000, 3200, 3500, 3600]
}

df = pd.DataFrame(data)

# Usar pivot para reorganizar los datos
pivot_df = df.pivot(index='Empleado', columns='Departamento', values='Salario')

# Mostrar el DataFrame reorganizado
print(pivot_df)


```
