# Clasificación con Random Forest en R

Este repositorio contiene un ejemplo de cómo entrenar un modelo de clasificación utilizando el algoritmo de **Random Forest** en R. El conjunto de datos utilizado es el famoso **Iris dataset**, que clasifica tres especies diferentes de flores basándose en cuatro características: `Sepal.Length`, `Sepal.Width`, `Petal.Length`, y `Petal.Width`.

## Requisitos

Para ejecutar el código de este proyecto, necesitas tener instalados los siguientes paquetes de R:

- `caret`
- `randomForest`
- `ggplot2`

Si no los tienes instalados, puedes hacerlo con el siguiente comando:

```r
install.packages(c("caret", "randomForest", "ggplot2"))
```

1. Cargar paquetes y datos

# Cargar los paquetes necesarios

```r
library(caret)
library(randomForest)
library(ggplot2)
```
# Cargar el conjunto de datos iris
```r
data(iris)
```
2. Dividir los datos
```r
set.seed(123)
trainIndex <- createDataPartition(iris$Species, p = 0.7, list = FALSE)
trainData <- iris[trainIndex, ]
testData <- iris[-trainIndex, ]
```
3. Entrenar el modelo Random Forest
```r
rf_model <- randomForest(Species ~ ., data = trainData)
```

4. Realizar predicciones y crear la matriz de confusión

### Realizar predicciones
```r
predictions <- predict(rf_model, testData)
```
### Matriz de confusión
```r
conf_matrix <- confusionMatrix(predictions, testData$Species)
print(conf_matrix)
```

### Graficar la matriz de confusión
```r
# Crear la tabla de la matriz de confusión
cm_table <- as.data.frame(conf_matrix$table)
```
```r
# Graficar
ggplot(data = cm_table, aes(x = Reference, y = Prediction, fill = Freq)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue") +
  geom_text(aes(label = Freq), vjust = 1) +
  theme_minimal() +
  ggtitle("Matriz de Confusión - Random Forest")
  
```

### Importancia de las variables
```r
# Graficar la importancia de las variables
importance_rf <- importance(rf_model)
var_importance <- data.frame(Variable = row.names(importance_rf), 
                             Importance = importance_rf[,1])

ggplot(var_importance, aes(x = reorder(Variable, Importance), y = Importance)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  coord_flip() +
  theme_minimal() +
  ggtitle("Importancia de las Variables - Random Forest")

```
### Almacenar el modelo
```r
# Guardar el modelo entrenado en un archivo .rds
saveRDS(rf_model, file = "random_forest_model.rds")
```


## Evaluar el modelo
```r
# Cargar el modelo de Random Forest guardado
loaded_rf_model <- readRDS("random_forest_model.rds")

# Ver los detalles del modelo cargado
print(loaded_rf_model)

# Crear un dataframe sintético con datos aleatorios
set.seed(123)  # Semilla para reproducibilidad
synthetic_data <- data.frame(
  Sepal.Length = runif(10, min = 4.3, max = 7.9),  # Valores aleatorios en el rango del conjunto Iris
  Sepal.Width  = runif(10, min = 2.0, max = 4.4),
  Petal.Length = runif(10, min = 1.0, max = 6.9),
  Petal.Width  = runif(10, min = 0.1, max = 2.5)
)

# Ver el dataframe sintético
print(synthetic_data)


# Realizar predicciones usando el modelo cargado y el dataframe sintético
predictions_synthetic <- predict(loaded_rf_model, synthetic_data)

# Mostrar las predicciones
print(predictions_synthetic)

# Agregar las predicciones como una nueva columna al dataframe sintético
synthetic_data$Predicted_Species <- predictions_synthetic

# Ver el dataframe sintético con las predicciones
print(synthetic_data)

# Guardar el dataframe sintético con las predicciones en un archivo CSV
write.csv(synthetic_data, file = "synthetic_predictions.csv", row.names = FALSE)

library(ggplot2)

# Crear un gráfico de dispersión con los datos sintéticos y las predicciones
ggplot(synthetic_data, aes(x = Sepal.Length, y = Sepal.Width, color = Predicted_Species)) +
  geom_point(size = 4) +
  theme_minimal() +
  labs(title = "Predicciones del modelo sobre datos sintéticos",
       x = "Sepal Length",
       y = "Sepal Width",
       color = "Especies Predichas")
```
