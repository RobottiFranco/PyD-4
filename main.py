import pandas as pd

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
titanic_df.loc[(titanic_df['age'].isnull()) & (titanic_df['gender'] == 'male'), 'age'] = mean_age_male
titanic_df.loc[(titanic_df['age'].isnull()) & (titanic_df['gender'] == 'female'), 'age'] = mean_age_female

# Verificar que no queden valores nulos en la columna 'age'
print(titanic_df['age'].isnull().sum())