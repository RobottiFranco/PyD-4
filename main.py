import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, mode
import numpy as np
from scipy import stats

# Cargar el archivo CSV
file_path = 'titanik.csv'
titanic_df = pd.read_csv(file_path)

# Calcular la media de edad para cada género
mean_age_male = titanic_df.loc[titanic_df['gender'] == 'male', 'age'].mean()
mean_age_female = titanic_df.loc[titanic_df['gender'] == 'female', 'age'].mean()

# Rellenar los valores vacíos en la columna 'age' usando la media de edad según el género
titanic_df.loc[titanic_df['gender'] == 'male', 'age'].fillna(mean_age_male, inplace=True)
titanic_df.loc[titanic_df['gender'] == 'female', 'age'].fillna(mean_age_female, inplace=True)

# Calcular estadísticas descriptivas básicas
age_descriptive_stats = titanic_df['age'].describe()

# Calcular la moda
mode_age = titanic_df['age'].mode().iloc[0]

# Calcular el rango
range_age = titanic_df['age'].max() - titanic_df['age'].min()

# Calcular la varianza
variance_age = titanic_df['age'].var()

# Crear un nuevo DataFrame con las estadísticas ordenadas
ordered_stats_df = pd.DataFrame({
    'mean': age_descriptive_stats['mean'],
    '50%': age_descriptive_stats['50%'],
    'mode': mode_age,
    'range': range_age,
    'variance': variance_age,
    'std': age_descriptive_stats['std'],
}, index=[0])

# Mostrar las estadísticas en el orden
print("Estadísticas descriptivas de las edades:")
for index, row in ordered_stats_df.iterrows():
    for stat, value in row.items():
        print(f"{stat}: {value}")


# Calcular la tasa de supervivencia
total_passengers = len(titanic_df)
total_survivors = titanic_df['survived'].sum()
survival_rate = (total_survivors / total_passengers) * 100

# Mostrar la tasa de supervivencia
print(f"Tasa de supervivencia general: {survival_rate:.2f}%")

# Calcular el total de pasajeros y sobrevivientes por género
total_passengers_gender = titanic_df['gender'].value_counts()
total_survivors_gender = titanic_df.groupby('gender')['survived'].sum()

# Calcular la tasa de supervivencia por género
survival_rate_gender = (total_survivors_gender / total_passengers_gender) * 100

# Mostrar la tasa de supervivencia por género
print(f"Tasa de supervivencia por género:")
print(survival_rate_gender)

# Crear histogramas de las edades por clase usando matplotlib
plt.figure(figsize=(12, 8))

for i, p_class in enumerate([1, 2, 3], start=1):
    plt.subplot(3, 1, i)
    plt.hist(titanic_df[titanic_df['p_class'] == p_class]['age'].dropna(), bins=20, edgecolor='black')
    plt.title(f'Histograma de Edades - Clase {p_class}')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Ajustar una distribución normal a las edades usando scipy
ages_all = titanic_df['age'].dropna()
mu, std = norm.fit(ages_all)

# Crear una secuencia de valores para la distribución ajustada
xmin, xmax = min(ages_all), max(ages_all)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

# Dibujar el histograma y la distribución ajustada
plt.figure(figsize=(8, 6))
plt.hist(ages_all, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')
plt.plot(x, p, 'k', linewidth=2)
plt.title('Distribución de la Edad con Ajuste Normal (Scipy)')
plt.xlabel('Edad')
plt.ylabel('Densidad de Frecuencia')
plt.show()

print(f"Parámetros de la distribución normal ajustada: media = {mu:.2f}, desviación estándar = {std:.2f}")

# Filtrar edades de supervivientes y no supervivientes
survived_ages = titanic_df[titanic_df['survived'] == 1]['age'].dropna()
not_survived_ages = titanic_df[titanic_df['survived'] == 0]['age'].dropna()

# Crear diagrama de caja usando matplotlib
plt.figure(figsize=(10, 6))

# Diagrama de caja para supervivientes
plt.subplot(1, 2, 1)
plt.boxplot(survived_ages, vert=False)
plt.title('Edades de los Supervivientes')
plt.xlabel('Edad')
plt.ylabel('Supervivientes')

# Diagrama de caja para no supervivientes
plt.subplot(1, 2, 2)
plt.boxplot(not_survived_ages, vert=False)
plt.title('Edades de los No Supervivientes')
plt.xlabel('Edad')
plt.ylabel('No Supervivientes')

plt.tight_layout()
plt.show()
