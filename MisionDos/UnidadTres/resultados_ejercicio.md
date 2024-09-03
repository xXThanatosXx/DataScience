
# Resultados del Ejercicio de Manipulación de Datos con Pandas

## Resumen de Resultados

1. **Valores nulos en los datos**:
   - No se encontraron valores nulos en ninguno de los dos DataFrames (`ventas.csv` y `clientes.csv`).

2. **Total de ventas en el año 2023**:
   - El total de ventas realizadas en el año 2023 es **1097.5**.

3. **Clasificación de productos como "Barato" y "Caro"**:
   - Productos clasificados como "Caro": 4
   - Productos clasificados como "Barato": 2

4. **Ciudad con mayor total de ventas**:
   - La ciudad con el mayor total de ventas es **Bilbao** con un total de **750.0**.

5. **Cliente con mayor cantidad de compras de un solo producto**:
   - El cliente que realizó la mayor cantidad de compras de un solo producto es **Carlos**.

## Detalles Adicionales

### Ventas por Ciudad

| Ciudad    | Total_Venta |
|-----------|-------------|
| Barcelona | 80.0        |
| Bilbao    | 750.0       |
| Madrid    | 111.0       |
| Sevilla   | 76.5        |
| Valencia  | 80.0        |

### Ventas Reorganizadas por Cliente y Producto

| Nombre | Producto A | Producto B | Producto C | Producto D |
|--------|------------|------------|------------|------------|
| Ana    | NaN        | NaN        | 60.0       | NaN        |
| Carlos | NaN        | NaN        | NaN        | 750.0      |
| Juan   | 51.0       | NaN        | NaN        | NaN        |
| Lucia  | NaN        | 80.0       | NaN        | NaN        |
| Maria  | NaN        | 80.0       | NaN        | NaN        |
| Pedro  | 76.5       | NaN        | NaN        | NaN        |

## Interpretación

- **Bilbao** destaca como la ciudad con las mayores ventas, impulsada principalmente por las compras de un solo cliente (**Carlos**) en el producto D.
- Los productos más caros (clasificados como "Caro") tienen más registros en comparación con los productos más baratos, lo que puede indicar una tendencia de los clientes a comprar productos de mayor valor.

Este análisis muestra cómo se pueden extraer insights valiosos a partir de la manipulación de datos usando Pandas en Python.
