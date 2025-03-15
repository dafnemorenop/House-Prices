import pandas as pd
import itertools
import plotly.express as px
import matplotlib.pyplot as plt 
import seaborn as sns


def calcular_todas_correlaciones(df, threshold=0.5):
    """
    Calcula las correlaciones entre todas las variables del DataFrame,
    devolviendo las correlaciones que superen un umbral especificado,
    excluyendo las correlaciones con la variable objetivo 'SalePrice'.

    Parámetros:
    - df: DataFrame que contiene las variables a analizar.
    - threshold: Umbral para filtrar las correlaciones.

    Retorna:
    - DataFrame con las correlaciones filtradas.
    """
    # Inicializar una lista para almacenar los resultados
    resultados_lista = []

    # Iterar sobre todas las combinaciones de columnas
    for i in range(len(df.columns)):
        for j in range(i + 1, len(df.columns)):
            var1 = df.columns[i]
            var2 = df.columns[j]

            # Excluir correlaciones con las variables 'SalePrice', 'Id' y 'Dataset'
            if var1 in ['SalePrice', 'Id', 'Dataset'] or var2 in ['SalePrice', 'Id', 'Dataset']:
                continue

            # Calcular las correlaciones de Pearson, Spearman y Kendall
            corr_pearson = df[var1].corr(df[var2], method='pearson')
            corr_spearman = df[var1].corr(df[var2], method='spearman')
            corr_kendall = df[var1].corr(df[var2], method='kendall')

            # Agregar los resultados a la lista
            resultados_lista.append({
                'Variable 1': var1,
                'Variable 2': var2,
                'Correlación Pearson': corr_pearson,
                'Correlación Spearman': corr_spearman,
                'Correlación Kendall': corr_kendall
            })

    # Crear un DataFrame a partir de la lista de resultados
    resultados = pd.DataFrame(resultados_lista)

    # Filtrar los resultados para mostrar solo correlaciones que superen el umbral
    resultados_filtrados = resultados[
        (resultados['Correlación Pearson'].abs() > threshold) |
        (resultados['Correlación Spearman'].abs() > threshold) |
        (resultados['Correlación Kendall'].abs() > threshold)
    ]

    return resultados_filtrados

def calcular_correlaciones_saleprice(df, threshold=0.2):
    """
    Calcula las correlaciones entre las variables del DataFrame y la variable objetivo 'SalePrice',
    devolviendo las correlaciones positivas que superen un umbral especificado.

    Parámetros:
    - df: DataFrame que contiene las variables a analizar.
    - threshold: Umbral para filtrar las correlaciones (por defecto 0.2).

    Retorna:
    - DataFrame con las correlaciones filtradas.
    """
    # Inicializar una lista para almacenar los resultados
    resultados_lista = []

    # Iterar sobre todas las combinaciones de columnas
    for i in range(len(df.columns)):
        for j in range(i + 1, len(df.columns)):
            var1 = df.columns[i]
            var2 = df.columns[j]

            # Ignorar correlaciones con la misma variable
            if var1 == 'SalePrice' or var2 == 'SalePrice':
                corr_pearson = df[var1].corr(df[var2], method='pearson')
                corr_spearman = df[var1].corr(df[var2], method='spearman')
                corr_kendall = df[var1].corr(df[var2], method='kendall')

                # Agregar los resultados a la lista
                resultados_lista.append({
                    'Variable 1': var1,
                    'Variable 2': var2,
                    'Correlación Pearson': corr_pearson,
                    'Correlación Spearman': corr_spearman,
                    'Correlación Kendall': corr_kendall
                })

    # Crear un DataFrame a partir de la lista de resultados
    resultados = pd.DataFrame(resultados_lista)

    # Filtrar los resultados para mostrar solo correlaciones positivas con 'SalePrice' mayores al umbral
    resultados_filtrados = resultados[
        ((resultados['Correlación Pearson'] > threshold) & (resultados['Variable 1'] == 'SalePrice')) |
        ((resultados['Correlación Pearson'] > threshold) & (resultados['Variable 2'] == 'SalePrice'))
    ]

    return resultados_filtrados


def correlaciones_pearson(train):
    correlaciones = train.corr()['SalePrice'].sort_values(ascending=False)
    correlaciones_significativas = correlaciones[correlaciones.abs() > 0.2]

    plt.figure(figsize=(10, 6))
    sns.heatmap(correlaciones_significativas.to_frame(), annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title('Correlaciones Lineales con SalePrice')
    plt.show()



def comparar_variable_discreta_con_target(dataframe, variable_target, variable_comparada):
    """
    Genera gráficos de barras para comparar una variable discreta 
    (tanto numéricas como categóricas, toman un conjunto finito o numerable de valores) 
    con la target.

    """
    fig, axes = plt.subplots(1, 2, figsize=(18, 7))
    sns.countplot(x=dataframe[variable_comparada], ax=axes[0])
    sns.countplot(x=dataframe[variable_comparada], hue=dataframe[variable_target], ax=axes[1])
    plt.show()

# comparar_variable_discreta_con_target(df, "SalePrice", "aerolinea")


def comparar_variable_continua_con_target(dataframe, variable_target, variable_comparada):
    """
    Genera gráficos para comparar una variable continua con una variable objetivo.
    Para variables continuas (numéricas que pueden contener valores atípicos, 
    que pueden variar dentro de un rango específico)

    """
    fig, axes = plt.subplots(2, 2, figsize=(18, 11))
    sns.boxplot(x=dataframe[variable_comparada], ax=axes[0, 0])
    axes[0, 0].set_title(f'{variable_comparada} Boxplot')
    sns.histplot(x=dataframe[variable_comparada], ax=axes[0, 1])
    axes[0, 1].set_title(f'{variable_comparada} Histogram')
    sns.boxplot(x=dataframe[variable_target], y=dataframe[variable_comparada], ax=axes[1, 0])
    axes[1, 0].set_title(f'{variable_comparada} vs {variable_target}')
    sns.histplot(x=dataframe[variable_comparada], hue=dataframe[variable_target], ax=axes[1, 1])
    axes[1, 1].set_title(f'{variable_comparada} Histogram by {variable_target}')
    plt.tight_layout()
    plt.show()

# comparar_variable_continua_con_target(df, "SalePrice", "distancia_millas")


def calcular_cuartiles(df, variable_aplicar_cuartiles, n_inferior, n_superior):
    """
    Calcula y elimina valores atípicos de una variable en un DataFrame basándose en los cuartiles.
    
    La función calcula el primer (Q1) y tercer cuartil (Q3), el rango intercuartil (IQR) y utiliza estos valores 
    para determinar los límites inferior y superior. Luego, filtra el DataFrame para eliminar los valores atípicos
    y retorna el DataFrame limpio. También imprime la cantidad de filas eliminadas.

    """

    longitud_variable_antes = len(df[variable_aplicar_cuartiles])
    q1 = df[variable_aplicar_cuartiles].quantile(q=0.25)  # Q1
    q3 = df[variable_aplicar_cuartiles].quantile(q=0.75)  # Q3
    # Rango intercuartil (IQR)
    iqr = q3 - q1
    # Calcular los limites inferior y superior
    limite_inferior = q1 - n_inferior * iqr
    limite_superior = q3 + n_superior * iqr
    df = df[df[variable_aplicar_cuartiles].between(limite_inferior, limite_superior)]
    longitud_variable_despues = len(df[variable_aplicar_cuartiles])
    diferencia_filas = longitud_variable_antes - longitud_variable_despues
    print(f"La longitud de la variable antes era de {longitud_variable_antes}, y ahora es de {longitud_variable_despues}. Se han eliminado {diferencia_filas} filas del DF.")
    return df

# df = calcular_cuartiles(df, 'Variable_Quitar_Cuartiles', 1.5, 1.5) # n_inferior, n_superior):
# TENGO QUE TENER CUIDADO DE ELIMINAR LOS OUTLIERS SOLO DE TRAIN Y NO TEST. SI HAY OUTLIER EN TEST QUÉ HAGO???