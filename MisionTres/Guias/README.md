# Actividad de Análisis de Datos con el Dataset `airquality`

## Descripción

Análisis básico de la calidad del aire utilizando el dataset `airquality`, 
el cual incluye variables como concentración de ozono, radiación solar, velocidad del viento y temperatura. 
El objetivo es explorar los datos, crear visualizaciones y aplicar un modelo de regresión lineal para predecir 
el nivel de ozono a partir de la temperatura.


La base de datos "airquality" es un conjunto de datos integrado en R, que contiene mediciones diarias sobre la calidad del aire tomadas en la ciudad de Nueva York en 1973. Esta base de datos incluye observaciones de varias variables relacionadas con el clima y la calidad del aire. Los campos que contiene son los siguientes:

- Ozone: Concentración de ozono (O3) en partes por billón (ppb) en la atmósfera.
- Solar.R: Radiación solar en langleys.
- Wind: Velocidad del viento en millas por hora (mph).
- Temp: Temperatura diaria máxima en grados Fahrenheit.
- Month: Mes en el que se realizó la medición (de 5 a 9, donde 5 es mayo y 9 es septiembre).
- Day: Día del mes en que se tomó la observación.

## Requisitos

- Tener instalado R.
- Paquetes requeridos: `lattice`.

Puedes instalar el paquete `lattice` ejecutando:

```r
install.packages("lattice")
```

### Pasos de la Actividad
1. Cargar y explorar los datos
Carga el dataset airquality y muestra un resumen de los datos.


- Cargar la base de datos airquality
```r
data("airquality")
```
- Mostrar las primeras filas del dataset
```r
head(airquality)
```

2. Limpiar los datos
- Elimina las filas que contienen valores faltantes.

# Limpiar los datos eliminando valores NA
```r
airquality_clean <- na.omit(airquality)
```

3. Crear visualizaciones de los datos
a). Histograma de la temperatura

```r
hist(airquality_clean$Temp,
     main = "Histograma de la Temperatura",
     xlab = "Temperatura (°F)",
     col = "lightblue",
     border = "black")
```

b) Boxplot de la distribución de ozono por mes

```r
boxplot(Ozone ~ Month, data = airquality_clean,
        main = "Distribución de Ozone por Mes",
        xlab = "Mes",
        ylab = "Concentración de Ozone (ppb)",
        col = "lightgreen")
```

c). Gráfico de dispersión entre ozono y temperatura por mes
```r
library(lattice)
xyplot(Ozone ~ Temp | factor(Month), data = airquality_clean,
       main = "Relación entre Ozone y Temperatura por Mes",
       xlab = "Temperatura (°F)", ylab = "Concentración de Ozone (ppb)",
       type = c("p", "r"),
       col = "blue")
```

4. Calcular la correlación entre variables

```r
cor_matrix <- cor(airquality_clean[, c("Ozone", "Solar.R", "Wind", "Temp")])
print(cor_matrix)
```

5. Aplicar un modelo de regresión lineal
Crea un modelo para predecir la concentración de ozono en función de la temperatura.

```r
modelo <- lm(Ozone ~ Temp, data = airquality_clean)
summary(modelo)
```

6. Realizar predicciones con el modelo
Predice la concentración de ozono para nuevas temperaturas.

```r
new_data <- data.frame(Temp = c(70, 80, 90))
predicciones <- predict(modelo, new_data)
print(predicciones)
```

# Cuestionario

1. ¿Cómo varía la concentración de ozono en relación con la temperatura?
2. ¿Qué tan fuerte es la correlación entre las variables del dataset?
3. ¿Qué limitaciones observas en el modelo de regresión lineal que has creado?
4. ¿Cómo podrías mejorar la precisión del modelo?