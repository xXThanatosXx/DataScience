# Ejercicio de Práctica en R: Análisis de Datos de Ventas con un Dataset de Kaggle

**Dataset:** [Online Retail Dataset](https://www.kaggle.com/datasets/mashlyn/online-retail-dataset)  
Descárgalo y guárdalo localmente como `online_retail.csv`.

---

## Descripción

Tienes un conjunto de datos que contiene transacciones de una tienda minorista en línea que vende artículos para el hogar. El dataset incluye información como la fecha de la factura, código de producto, descripción, cantidad, precio unitario, número de cliente y país. El objetivo es utilizar R para analizar estos datos y obtener insights relevantes sobre el comportamiento de ventas.

## Instrucciones

### 1. Carga de datos

- Importa el archivo `online_retail.csv` y guárdalo en un data frame llamado `ventas`.
- Asegúrate de que las fechas se importen correctamente como objetos de tipo `Date`.

```r
# Instala el paquete tidyverse si aún no lo tienes
install.packages("tidyverse")

# Carga las librerías necesarias
library(tidyverse)
library(lubridate)  # Para manejo de fechas

# Carga los datos
ventas <- read.csv("online_retail.csv", stringsAsFactors = FALSE)

# Convertir la columna de fecha
ventas$InvoiceDate <- as.POSIXct(ventas$InvoiceDate, format="%m/%d/%Y %H:%M")

# Verifica las primeras filas
head(ventas)
```

### 2. Exploración inicial
- Visualiza las primeras y últimas 6 filas del data frame.
- Obtén un resumen estadístico de las variables numéricas.
- Verifica si hay valores perdidos (NA) en el dataset.

# Exploración de los datos
```r
head(ventas)
tail(ventas)
summary(ventas)
sum(is.na(ventas))
```

### 3. Limpieza de datos
- Si existen valores perdidos, decide cómo manejarlos (por ejemplo, eliminar filas o imputar valores).
- Elimina las transacciones con cantidades negativas o precios negativos.
- Crea una nueva columna llamada TotalPrice que sea el resultado de Quantity * UnitPrice.

```r
# Eliminar filas con valores NA
ventas <- na.omit(ventas)

# Eliminar transacciones con cantidades o precios negativos
ventas <- ventas %>% filter(Quantity > 0, UnitPrice > 0)

# Crear columna TotalPrice
ventas <- ventas %>% mutate(TotalPrice = Quantity * UnitPrice)

```
 
### 4. Análisis exploratorio
- Calcula las ventas totales mensuales y grafica su evolución a lo largo del tiempo.

```r
ventas_mensuales <- ventas %>%
  mutate(Mes = floor_date(InvoiceDate, "month")) %>%
  group_by(Mes) %>%
  summarize(VentasTotales = sum(TotalPrice))

ggplot(ventas_mensuales, aes(x = Mes, y = VentasTotales)) +
  geom_line(color = "blue") +
  labs(title = "Ventas totales mensuales", x = "Mes", y = "Ventas Totales")
```

- Realiza un histograma de la cantidad de productos vendidos por transacción.
```r
ggplot(ventas, aes(x = Quantity)) +
  geom_histogram(binwidth = 1, fill = "green", color = "black") +
  xlim(0, 50) +  # Limitar para visualizar mejor
  labs(title = "Distribución de la cantidad por transacción", x = "Cantidad", y = "Frecuencia")

```

- Identifica los 10 productos más vendidos y crea un gráfico de barras.
```r

productos_top <- ventas %>%
  group_by(Description) %>%
  summarize(CantidadVendida = sum(Quantity)) %>%
  arrange(desc(CantidadVendida)) %>%
  head(10)

ggplot(productos_top, aes(x = reorder(Description, -CantidadVendida), y = CantidadVendida)) +
  geom_bar(stat = "identity", fill = "orange") +
  coord_flip() +
  labs(title = "Top 10 productos más vendidos", x = "Producto", y = "Cantidad Vendida")
```
- Realiza una segmentación de clientes basada en el monto total gastado.

```r
clientes <- ventas %>%
  group_by(CustomerID) %>%
  summarize(MontoGastado = sum(TotalPrice))

# Definir segmentos
clientes <- clientes %>%
  mutate(Segmento = case_when(
    MontoGastado >= quantile(MontoGastado, 0.75) ~ "Alto valor",
    MontoGastado >= quantile(MontoGastado, 0.50) ~ "Medio valor",
    TRUE ~ "Bajo valor"
  ))


```

- Calcula la correlación entre la cantidad y el precio unitario.


```r
correlacion <- cor(ventas$Quantity, ventas$UnitPrice, method = "pearson")
print(paste("La correlación entre cantidad y precio unitario es:", round(correlacion, 2)))
```

- Realiza una regresión lineal simple prediciendo el monto gastado (TotalPrice) en función de la cantidad (Quantity).
```r
modelo <- lm(TotalPrice ~ Quantity, data = ventas)
summary(modelo)
```

### 5 Visualización de resultados
```r
ggplot(ventas, aes(x = Quantity, y = TotalPrice)) +
  geom_point(alpha = 0.3) +
  geom_smooth(method = "lm", col = "red") +
  xlim(0, 50) + ylim(0, 1000) +  # Limitar para visualizar mejor
  labs(title = "Relación entre cantidad y monto gastado", x = "Cantidad", y = "Monto Gastado")
```

```r
clientes %>%
  group_by(Segmento) %>%
  summarize(NumeroClientes = n()) %>%
  ggplot(aes(x = Segmento, y = NumeroClientes, fill = Segmento)) +
  geom_bar(stat = "identity") +
  labs(title = "Segmentación de clientes por valor", x = "Segmento", y = "Número de Clientes")
```