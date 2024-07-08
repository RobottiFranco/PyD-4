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

# Calcular la media y la desviación estándar
mu = titanic_df['age'].mean()
std = titanic_df['age'].std()

# Tamaño de la muestra
n = len(titanic_df['age'].dropna())

# Error estándar de la media
sem = std / np.sqrt(n)

# Valor crítico para un nivel de confianza del 95%
confidence_level = 0.95
degrees_freedom = n - 1
t_critical = stats.t.ppf((1 + confidence_level) / 2, degrees_freedom)

# Calcular el margen de error
margin_of_error = t_critical * sem

# Calcular el intervalo de confianza
confidence_interval = (mu - margin_of_error, mu + margin_of_error)

print(f"Intervalo de confianza del 95% para la edad promedio: {confidence_interval[0]:.2f} - {confidence_interval[1]:.2f}")

# Número total de hombres y mujeres
n_male = len(titanic_df[titanic_df['gender'] == 'male'])
n_female = len(titanic_df[titanic_df['gender'] == 'female'])

# Error estándar de la media
sem_male = titanic_df[titanic_df['gender'] == 'male']['age'].std() / np.sqrt(n_male)
sem_female = titanic_df[titanic_df['gender'] == 'female']['age'].std() / np.sqrt(n_female)

# Valor crítico para un intervalo de confianza del 95%
confidence_level = 0.95
alpha = 1 - confidence_level
t_critical = stats.t.ppf(1 - alpha/2, df=n_male-1)  # Grados de libertad = n - 1

# Intervalo de confianza para hombres
ci_male_lower = mean_age_male - t_critical * sem_male
ci_male_upper = mean_age_male + t_critical * sem_male

# Intervalo de confianza para mujeres
ci_female_lower = mean_age_female - t_critical * sem_female
ci_female_upper = mean_age_female + t_critical * sem_female

# Mostrar los intervalos de confianza
print(f"Intervalo de confianza del 95% para la media de edad de los hombres: {ci_male_lower:.2f} - {ci_male_upper:.2f}")
print(f"Intervalo de confianza del 95% para la media de edad de las mujeres: {ci_female_lower:.2f} - {ci_female_upper:.2f}")

# Verificar si los intervalos están por encima de 56 años
is_male_above_56 = ci_male_lower > 56
is_female_above_56 = ci_female_lower > 56

print(f"¿La media de edad de los hombres es mayor a 56 años con un 95% de certeza? {'Sí' if is_male_above_56 else 'No'}")
print(f"¿La media de edad de las mujeres es mayor a 56 años con un 95% de certeza? {'Sí' if is_female_above_56 else 'No'}")

# Calcular la tasa de supervivencia por género
total_passengers_gender = titanic_df['gender'].value_counts()
total_survivors_gender = titanic_df.groupby('gender')['survived'].sum()

# Calcular la tasa de supervivencia por género
survival_rate_gender = (total_survivors_gender / total_passengers_gender) * 100

# Prueba para comparar las tasas de supervivencia entre hombres y mujeres
survived_male = titanic_df[titanic_df['gender'] == 'male']['survived']
survived_female = titanic_df[titanic_df['gender'] == 'female']['survived']

t_stat, p_value = stats.ttest_ind(survived_male, survived_female)

alpha = 0.01  # Nivel de significancia del 1%

if p_value < alpha:
    print("Existe una diferencia significativa en la tasa de supervivencia entre hombres y mujeres.")
else:
    print("No se puede afirmar una diferencia significativa en la tasa de supervivencia entre hombres y mujeres.")

# Calcular la tasa de supervivencia por clase
total_passengers_class = titanic_df['p_class'].value_counts()
total_survivors_class = titanic_df.groupby('p_class')['survived'].sum()

# Calcular la tasa de supervivencia por clase
survival_rate_class = (total_survivors_class / total_passengers_class) * 100

# Prueba de hipótesis para comparar las tasas de supervivencia entre las distintas clases
survived_class1 = titanic_df[titanic_df['p_class'] == 1]['survived']
survived_class2 = titanic_df[titanic_df['p_class'] == 2]['survived']
survived_class3 = titanic_df[titanic_df['p_class'] == 3]['survived']

# Comparación de la tasa de supervivencia entre las distintas clases usando prueba t de Student
t_stat1_2, p_value1_2 = stats.ttest_ind(survived_class1, survived_class2)
t_stat1_3, p_value1_3 = stats.ttest_ind(survived_class1, survived_class3)
t_stat2_3, p_value2_3 = stats.ttest_ind(survived_class2, survived_class3)

alpha = 0.01  # Nivel de significancia del 1%

# Interpretación de los resultados
if p_value1_2 < alpha or p_value1_3 < alpha or p_value2_3 < alpha:
    print("Existe una diferencia significativa en la tasa de supervivencia entre al menos dos clases.")
else:
    print("No hay suficiente evidencia para afirmar que existe una diferencia significativa en la tasa de supervivencia entre las distintas clases.")
