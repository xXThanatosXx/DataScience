install.packages("ggplot2")
install.packages("caret")
install.packages("randomForest")

# Cargar los paquetes necesarios
library(caret)
library(randomForest)
library(ggplot2)

# Cargar el conjunto de datos iris
data(iris)

# Ver las primeras filas del conjunto de datos
head(iris)

# Fijar la semilla para reproducibilidad
set.seed(123)

# Crear índices para la partición de los datos
trainIndex <- createDataPartition(iris$Species, p = 0.7, list = FALSE)

# Dividir los datos en entrenamiento y prueba
trainData <- iris[trainIndex, ]
testData <- iris[-trainIndex, ]

# Fijar la semilla para reproducibilidad
set.seed(123)

# Crear índices para la partición de los datos
trainIndex <- createDataPartition(iris$Species, p = 0.7, list = FALSE)

# Dividir los datos en entrenamiento y prueba
trainData <- iris[trainIndex, ]
testData <- iris[-trainIndex, ]

# Entrenar el modelo Random Forest
rf_model <- randomForest(Species ~ ., data = trainData)

# Ver los detalles del modelo
print(rf_model)

# Realizar predicciones en el conjunto de prueba
predictions <- predict(rf_model, testData)

# Crear la matriz de confusión
conf_matrix <- confusionMatrix(predictions, testData$Species)

# Mostrar la matriz de confusión en texto
print(conf_matrix)

# Crear una tabla de datos de la matriz de confusión
cm_table <- as.data.frame(conf_matrix$table)

# Graficar la matriz de confusión
ggplot(data = cm_table, aes(x = Reference, y = Prediction, fill = Freq)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue") +
  geom_text(aes(label = Freq), vjust = 1) +
  theme_minimal() +
  ggtitle("Matriz de Confusión - Random Forest")

# Importancia de las variables
importance_rf <- importance(rf_model)
var_importance <- data.frame(Variable = row.names(importance_rf), 
                             Importance = importance_rf[,1])

# Graficar la importancia de las variables
ggplot(var_importance, aes(x = reorder(Variable, Importance), y = Importance)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  coord_flip() +
  theme_minimal() +
  ggtitle("Importancia de las Variables - Random Forest")

# Guardar el modelo entrenado en un archivo .rds
saveRDS(rf_model, file = "random_forest_model.rds")
