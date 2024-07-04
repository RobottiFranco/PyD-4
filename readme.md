parte 1
file_path = 'titanik.csv'
titanic_df = pd.read_csv(file_path)

parte 2

Para corregir los valores vacíos en la columna "age" usando la media de las edades según el género de los pasajeros hay que:

Calcular la media de las edades para hombres y mujeres por separado.
Rellenar los valores vacíos en la columna "age" con la media correspondiente según el género del pasajero.

justificacion:
La edad de los pasajeros puede estar correlacionada con su género. Por ejemplo, en algunos casos, la media de edad de los hombres puede ser diferente de la media de edad de las mujeres en un conjunto de datos.
Al usar la media de edad específica del género, se preserva mejor la distribución original de los datos y se evita introducir sesgos significativos que podrían ocurrir si se usara una única media para todos los pasajeros.

parte 3
