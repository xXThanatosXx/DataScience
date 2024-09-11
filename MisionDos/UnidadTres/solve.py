#from google.colab import files
import pandas as pd


# Cargar archivos CSV desde tu computadora a Google Colab
#uploaded = files.upload()

# Cargar los archivos CSV
ventas_df = pd.read_csv('./MisionDos/UnidadTres/ventas.csv')
clientes_df = pd.read_csv('./MisionDos/UnidadTres/clientes.csv')

# 1. Limpieza de datos
# Revisar si hay valores nulos
ventas_nulls = ventas_df.isnull().sum()
clientes_nulls = clientes_df.isnull().sum()

# Eliminar filas con valores nulos (si existieran)
ventas_df_cleaned = ventas_df.dropna()
clientes_df_cleaned = clientes_df.dropna()

# 2. Selección de datos
# Seleccionar ventas realizadas en el año 2023
ventas_2023 = ventas_df_cleaned[ventas_df_cleaned['Fecha'].str.startswith('2023')].copy()

# Seleccionar columnas específicas
ventas_2023_selected = ventas_2023[['Producto', 'Cantidad', 'Precio']].copy()

# 3. Transformación de datos
# Calcular columna 'Total_Venta'
ventas_2023_selected.loc[:, 'Total_Venta'] = ventas_2023_selected['Cantidad'] * ventas_2023_selected['Precio']

# Clasificar productos en 'Barato' y 'Caro'
ventas_2023_selected.loc[:, 'Clasificación'] = ventas_2023_selected['Precio'].apply(lambda x: 'Barato' if x < 50 else 'Caro')

# 4. Combinación de datos
# Combinar ventas con clientes usando 'Cliente_ID'
ventas_combinadas = pd.merge(ventas_2023, clientes_df_cleaned, on='Cliente_ID')

# Asegurarnos de que la columna 'Total_Venta' está en el DataFrame combinado
ventas_combinadas['Total_Venta'] = ventas_combinadas['Cantidad'] * ventas_combinadas['Precio']

# 5. Agrupación y agregación
# Agrupar por 'Ciudad' y calcular el total de ventas
ventas_por_ciudad = ventas_combinadas.groupby('Ciudad')['Total_Venta'].sum().reset_index()

# 6. Reorganización de datos
# Usar pivot para reorganizar el DataFrame
pivot_ventas = ventas_combinadas.pivot_table(index='Nombre', columns='Producto', values='Total_Venta', aggfunc='sum')

# Resultados del ejercicio
resultados = {
    "Valores nulos en ventas": ventas_nulls,
    "Valores nulos en clientes": clientes_nulls,
    "Total ventas 2023": ventas_2023_selected['Total_Venta'].sum(),
    "Cantidad de productos Barato/Caro": ventas_2023_selected['Clasificación'].value_counts(),
    "Ciudad con mayor total de ventas": ventas_por_ciudad.loc[ventas_por_ciudad['Total_Venta'].idxmax()],
    "Cliente con mayor cantidad de compras de un solo producto": pivot_ventas.sum(axis=1).idxmax()
}

# Mostrar los resultados
print("Resultados del Ejercicio:")
for key, value in resultados.items():
    print(f"{key}: {value}")

print("\nVentas por Ciudad:")
print(ventas_por_ciudad)

print("\nVentas Reorganizadas por Cliente y Producto:")
print(pivot_ventas)
