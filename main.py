import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
#parte 1

# Cargar el archivo CSV

file_path = 'titanik.csv'
titanic_df = pd.read_csv(file_path)

#parte 2

# Calcular la media de edad para cada género
mean_age_male = titanic_df[titanic_df['gender'] == 'male']['age'].mean()
mean_age_female = titanic_df[titanic_df['gender'] == 'female']['age'].mean()

# Mostrar las medias calculadas
print(f"Media de edad (hombres): {mean_age_male}")
print(f"Media de edad (mujeres): {mean_age_female}")

# Rellenar los valores vacíos en la columna 'age' usando la media de edad según el género
titanic_df.loc[(titanic_df['gender'] == 'male'), 'age'] = mean_age_male
titanic_df.loc[(titanic_df['gender'] == 'female'), 'age'] = mean_age_female

# Verificar que no queden valores nulos en la columna 'age'
""" print(titanic_df['age'].isnull().sum()) """

#parte 3

print("")

# Calcular las estadísticas descriptivas

# Media
mean_age = titanic_df['age'].mean()

# Mediana
median_age = titanic_df['age'].median()

# Moda
mode_age = titanic_df['age'].mode()[0]

# Rango
range_age = titanic_df['age'].max() - titanic_df['age'].min()

# Varianza
variance_age = titanic_df['age'].var()

# Desviación estándar
std_dev_age = titanic_df['age'].std()

# Mostrar las estadísticas calculadas
print(f"Media de las edades: {mean_age}")
print(f"Mediana de las edades: {median_age}")
print(f"Moda de las edades: {mode_age}")
print(f"Rango de las edades: {range_age}")
print(f"Varianza de las edades: {variance_age}")
print(f"Desviación estándar de las edades: {std_dev_age}")

#parte 4

print("")


# Calcular la tasa de supervivencia
total_passengers = len(titanic_df)
total_survivors = titanic_df['survived'].sum()
survival_rate = (total_survivors / total_passengers) * 100

# Mostrar la tasa de supervivencia
print(f"Tasa de supervivencia general: {survival_rate:.2f}%")

#parte 5

print("")


# Calcular el total de pasajeros y sobrevivientes por género
total_passengers_gender = titanic_df['gender'].value_counts()
total_survivors_gender = titanic_df[titanic_df['survived'] == 1]['gender'].value_counts()

# Calcular la tasa de supervivencia por género
survival_rate_male = (total_survivors_gender['male'] / total_passengers_gender['male']) * 100
survival_rate_female = (total_survivors_gender['female'] / total_passengers_gender['female']) * 100

# Mostrar la tasa de supervivencia por género
print(f"Tasa de supervivencia para hombres: {survival_rate_male:.2f}%")
print(f"Tasa de supervivencia para mujeres: {survival_rate_female:.2f}%")

#parte 6

print("")


# Crear histogramas de las edades por clase
plt.figure(figsize=(12, 8))

# Primera clase
plt.subplot(3, 1, 1)
plt.hist(titanic_df[titanic_df['p_class'] == 1]['age'].dropna(), bins=20, edgecolor='black')
plt.title('Histograma de Edades - Primera Clase')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')

# Segunda clase
plt.subplot(3, 1, 2)
plt.hist(titanic_df[titanic_df['p_class'] == 2]['age'].dropna(), bins=20, edgecolor='black')
plt.title('Histograma de Edades - Segunda Clase')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')

# Tercera clase
plt.subplot(3, 1, 3)
plt.hist(titanic_df[titanic_df['p_class'] == 3]['age'].dropna(), bins=20, edgecolor='black')
plt.title('Histograma de Edades - Tercera Clase')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Ajustar una distribución normal a las edades de todas las clases
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
plt.title('Distribución de la Edad con Ajuste Normal')
plt.xlabel('Edad')
plt.ylabel('Densidad de Frecuencia')
plt.show()

print(f"Parámetros de la distribución normal ajustada: media = {mu:.2f}, desviación estándar = {std:.2f}")

#parte 7

print("")


# Filtrar edades de supervivientes y no supervivientes
survived_ages = titanic_df[titanic_df['survived'] == 1]['age'].dropna()
not_survived_ages = titanic_df[titanic_df['survived'] == 0]['age'].dropna()

# Crear diagrama de caja
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