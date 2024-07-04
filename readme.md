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
Media: La media aritmética de las edades.
Mediana: El valor central de las edades cuando están ordenadas.
Moda: El valor más frecuente en las edades.
Rango: La diferencia entre la edad máxima y la edad mínima.
Varianza: La medida de la dispersión de las edades respecto a la media.
Desviación estándar: La raíz cuadrada de la varianza, que también mide la dispersión de las edades.

#parte 4
Para calcular la tasa de supervivencia general, podemos dividir el número de sobrevivientes entre el número total de pasajeros y multiplicar por 100 para obtener el porcentaje.

Total de pasajeros: Contamos el número total de filas.
Total de sobrevivientes: Sumamos los valores en la columna survived (donde 1 indica que el pasajero sobrevivió).
Tasa de supervivencia: Dividimos el número de sobrevivientes entre el número total de pasajeros y multiplicamos por 100 para obtener el porcentaje.

#parte 5
Para calcular la tasa de supervivencia por género, necesitamos dividir el número de sobrevivientes de cada género entre el número total de pasajeros de ese género y luego multiplicar por 100 para obtener el porcentaje.

Total de pasajeros por género: Usamos value_counts() para contar el número de pasajeros de cada género.
Total de sobrevivientes por género: Filtramos el dataframe para sobrevivientes y usamos value_counts() para contar el número de sobrevivientes de cada género.
Tasa de supervivencia por género: Dividimos el número de sobrevivientes de cada género entre el número total de pasajeros de ese género y multiplicamos por 100 para obtener el porcentaje.

#parte 6
Para realizar un histograma de las edades de los pasajeros por clase y proponer un modelo para la distribución de la variable edad en el barco, seguiremos estos pasos:

Crear histogramas de las edades para cada clase de pasajero (primera, segunda y tercera).
Proponer un modelo para la distribución de la variable edad en el barco.