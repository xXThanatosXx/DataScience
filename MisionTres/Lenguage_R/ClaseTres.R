df <- read.table(text = " Temperatura Velocidad Tension  Defectuosos
                              20        37.79   84.9        25.08
                              26        28.37   109.8       24.13
                              34        58.59   111.1       40.47
                              14        16.05   102.2       12.75
                              21        12.34   116.5       14.73
                              21        53.32   115.4       32.30
                              24        58.39   95.3        36.67
                              21        31.45   114.1       19.07
                              26        55.45   83.3        34.21
                              15        55.01   111.9       25.87
                              19        13.51   91.6        16.39
                              21        25.87   110.7       17.55
                              20        21.84   94.8        20.52
                              21        19.89   99.2        17.23
                              20        37.75   105.8       21.79
                              15        13.43   99.4        11.51
                              16        27.65   112.3       16.71
                              17        48.99   99.1        26.63
                              19        54.68   90.8        28.04
                              25        18.33   101         15.54
                              19        40.47   121.1       25.40
                              13        44.05   98.8        19.87
                              15        20.60   85.8        17.47
                              18        12.35   96          14.75
                              17        48.03   111.1       25.78",
                 header = TRUE)
dim(df)
#GUARDAR TABLA DE DATOS EN FORMATO CSV
#Guardar Tabla en formato CSV
write.table(df,"regresion.csv",sep = ";",quote = F,row.names = F)

# Obtener la ruta actual de trabajo
ruta_actual <- getwd()
print(ruta_actual)
#setwd("D:\\Shadow\\GitHub\\DataScience\\MisionTres\\Lenguage_R")

#carga tabla CSV
dato <- read.csv("regresion.csv",sep = ";")

#Procesamiento de tabla
attach(dato)
names(dato)

#P_value = 0.05   p > 0 no hay significancia
#p_value < 0 si hay significancia.

#Creación del modelo lineal
Modelo <-  lm(Defectuosos~Temperatura+Velocidad+Tension)
ANOVA <- aov(Modelo)
summary(ANOVA)
plot(ANOVA)


# Existen elementos significativos

# Para verificar las variables significativas
summary(Modelo)

## Retiramos la variable con el p-value mayor,
#en este caso la ordenada al origen

# Nuevo Modelo
Modelo <- lm(Defectuosos~-1+Temperatura+Velocidad+Tension)
ANOVA <- aov(Modelo)
summary(ANOVA)

# Para verificar las variables significativas
summary(Modelo)

# la Tensión no es significativa por lo que se retira

# Nuevo Modelo
Modelo <- lm(Defectuosos~-1+Temperatura+Velocidad)
ANOVA <- aov(Modelo)
summary(ANOVA)


# Para verificar las variables significativas
summary(Modelo)

#Las variables Temperatura y velocidad son significativas p_value < 0.05,
#por tanto afectan el porcentaje de la varaible (defecto), y explican el 99.3 % de la variación
#en el porcentaje de la variable (defectos).


# La temperatura y la velocidad son las variables significativas


# Los coeficientes de la ecuación de regresión
coef(Modelo)
#Defectuosos=??1*Temperatura+??2*Velocidad+??3*Tension


## Análisis de la adecuación del modelo
# Normalidad de los residuos


shapiro.test(rstandard(Modelo))

# hipotesis planteado
# h1 nula = los residuos son normales con respecto a los datos análizados

#h2 alternativa = los residuos no son normales.



# No es significativo por lo que no se puede rechazar la hipótesis nula
# Los residuos son normales

qqnorm(rstandard(Modelo))
qqline(rstandard(Modelo))
plot(Modelo)


library(car)
ncvTest(model = Modelo)
plot(Modelo)

#P value no hay significancia

"La hipotesis nula: las varianzas,
son significantes.

La hipotesis alternativa: las varianzas no
son significantes.

POr  lo tanto no se puede rechazar la hipoteis nula
y consideramos que las varianzas son iguales. POr
tanto el modelo es correcto."