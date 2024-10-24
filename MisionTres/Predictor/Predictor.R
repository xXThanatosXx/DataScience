# Cargar el modelo de Random Forest guardado
loaded_rf_model <- readRDS("random_forest_model.rds")

# Ver los detalles del modelo cargado
print(loaded_rf_model)

# Crear un dataframe sint�tico con datos aleatorios
set.seed(123)  # Semilla para reproducibilidad
synthetic_data <- data.frame(
  Sepal.Length = runif(10, min = 4.3, max = 7.9),  # Valores aleatorios en el rango del conjunto Iris
  Sepal.Width  = runif(10, min = 2.0, max = 4.4),
  Petal.Length = runif(10, min = 1.0, max = 6.9),
  Petal.Width  = runif(10, min = 0.1, max = 2.5)
)

# Ver el dataframe sint�tico
print(synthetic_data)





# Realizar predicciones usando el modelo cargado y el dataframe sint�tico
predictions_synthetic <- predict(loaded_rf_model, synthetic_data)

# Mostrar las predicciones
print(predictions_synthetic)

# Agregar las predicciones como una nueva columna al dataframe sint�tico
synthetic_data$Predicted_Species <- predictions_synthetic

# Ver el dataframe sint�tico con las predicciones
print(synthetic_data)

# Guardar el dataframe sint�tico con las predicciones en un archivo CSV
write.csv(synthetic_data, file = "synthetic_predictions.csv", row.names = FALSE)

library(ggplot2)

# Crear un gr�fico de dispersi�n con los datos sint�ticos y las predicciones
ggplot(synthetic_data, aes(x = Sepal.Length, y = Sepal.Width, color = Predicted_Species)) +
  geom_point(size = 4) +
  theme_minimal() +
  labs(title = "Predicciones del modelo sobre datos sint�ticos",
       x = "Sepal Length",
       y = "Sepal Width",
       color = "Especies Predichas")
