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