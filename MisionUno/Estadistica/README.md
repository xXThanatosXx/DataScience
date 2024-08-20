# Análisis Estadístico en Python

Este repositorio contiene scripts en Python para realizar un análisis estadístico básico, utilizando medidas de tendencia central, dispersión, asociación, forma y posición relativa. A continuación, se describen los comandos y funciones principales utilizados en cada uno de los scripts.

## Comandos y Funciones Utilizadas

### 1. Importación de Módulos

- numpy: Utilizado para manejar y realizar operaciones numéricas en arrays.
- scipy.stats: Proporciona herramientas estadísticas avanzadas como la moda, la asimetría y la curtosis.
- matplotlib.pyplot: Utilizado para crear gráficos y visualizaciones de datos.


- np.mean(data): Calcula la media (promedio) de los datos.
- np.median(data): Calcula la mediana, el valor central de los datos.
- stats.mode(data, keepdims=True).mode[0]: Calcula la moda, el valor más frecuente en el conjunto de dato

- np.var(data, ddof=1): Calcula la varianza, que mide la dispersión de los datos respecto a la media.
- np.std(data, ddof=1): Calcula la desviación estándar, que es la raíz cuadrada de la varianza.

- np.cov(data_x, data_y)[0, 1]: Calcula la covarianza entre dos variables, que mide cómo varían juntas.
- np.corrcoef(data_x, data_y)[0, 1]: Calcula la correlación, que mide la relación lineal normalizada entre dos variables.


- np.percentile(data, 25): Calcula el primer cuartil (Q1), que es el valor por debajo del cual se encuentra el 25% de los datos.
- np.percentile(data, 50): Calcula la mediana (Q2), que es el valor central del conjunto de datos.
- np.percentile(data, 75): Calcula el tercer cuartil (Q3), que es el valor por debajo del cual se encuentra el 75% de los datos.
- np.percentile(data, 10): Calcula el percentil 10, que es el valor por debajo del cual se encuentra el 10% de los datos.
- np.percentile(data, 90): Calcula el percentil 90, que es el valor por debajo del cual se encuentra el 90% de los datos.

### 2. Vizualización 

- plt.hist(): Crea un histograma para visualizar la distribución de los datos.
- plt.axvline(): Añade una línea vertical en la gráfica para marcar valores importantes como la media, la mediana o los cuartiles.
- plt.legend(): Muestra la leyenda en la gráfica.
- plt.title(): Establece el título de la gráfica.
- plt.xlabel() y plt.ylabel(): Etiquetan los ejes X e Y, respectivamente.
