import pandas as pd
import itertools
import plotly.express as px
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
import category_encoders as ce
import numpy as np

def resumen_columnas(df, lista_columnas):
    """
    Esta función toma un DataFrame y una lista de columnas y devuelve un DataFrame
    con un resumen que incluye la cantidad de valores únicos, la cantidad de NaN,
    el porcentaje de NaN en 'train' y 'test', los valores únicos que están en 
    'train' y no en 'test' y viceversa, y el tipo de dato de cada columna.
    """

    # Se separa en train y test
    df_train = df[df['Dataset'] == 'train']
    df_test = df[df['Dataset'] == 'test']

    # Calcula la cantidad de valores NaN y valores únicos para cada columna 
    cantidad_nan = df[lista_columnas].isna().sum()
    cantidad_unicos = df[lista_columnas].nunique()

    # Calcula el porcentaje de NaN en 'train' y 'test'
    cantidad_total = df['Dataset'].value_counts()
    nan_train = df[df['Dataset'] == 'train'][lista_columnas].isna().sum()
    nan_test = df[df['Dataset'] == 'test'][lista_columnas].isna().sum()

    porcentaje_nan_train = (nan_train / cantidad_total['train']) * 100
    porcentaje_nan_test = (nan_test / cantidad_total['test']) * 100

    # Encontrar columnas comunes de tipo objeto en train y test
    columnas_objeto_train = df_train.select_dtypes(include=['object']).columns
    columnas_objeto_test = df_test.select_dtypes(include=['object']).columns
    columnas_comunes = set(columnas_objeto_train) & set(columnas_objeto_test)

    # Obtener valores únicos en train y no en test y viceversa
    valores_unicos_train = {}
    valores_unicos_test = {}

    for columna in columnas_comunes:
        valores_train = set(df_train[columna].dropna().unique())
        valores_test = set(df_test[columna].dropna().unique())
        
        # Valores únicos 
        solo_en_train = valores_train - valores_test
        solo_en_test = valores_test - valores_train
        
        valores_unicos_train[columna] = list(solo_en_train)
        valores_unicos_test[columna] = list(solo_en_test)

    # Obtener el tipo de dato de cada columna
    tipos_datos = df[lista_columnas].dtypes

    # Creamos el DataFrame resultado
    resultado = pd.DataFrame({
        'Tipo de Dato': tipos_datos,
        'Nº Valores Únicos': cantidad_unicos,
        'Nº de NaN': cantidad_nan,
        'Porcentaje NaN Train': porcentaje_nan_train,
        'Porcentaje NaN Test': porcentaje_nan_test,
        'Valores Únicos Train': [valores_unicos_train.get(col, []) for col in lista_columnas],
        'Valores Únicos Test': [valores_unicos_test.get(col, []) for col in lista_columnas]
    })

    return resultado



def calcular_porcentaje_coincidencias(df, col1, col2):
    """
    Calcula el porcentaje de coincidencias entre dos columnas de un DataFrame.
    """
    
    coincidencias = (df[col1] == df[col2])
    
    num_coincidencias = coincidencias.sum()
    porcentaje_coincidencias = (num_coincidencias / len(df)) * 100
    
    devolver = f"El porcentaje de coincidencias entre '{col1}' y '{col2}' es de {porcentaje_coincidencias:.2f}%."
    return devolver


def obtener_valores_unicos(df, columnas):
    """
    Esta función toma un DataFrame y una lista de columnas y devuelve un diccionario
    con las listas de valores únicos y ordenados para cada columna.
    """
    return {col: sorted(df[col].dropna().unique().tolist()) for col in columnas}




def analizar_precio_viviendas_por_variable(df, columna_agrupacion):
    """
    Analiza el precio promedio, el número de viviendas y el porcentaje de viviendas agrupados por una variable específica.
    El precio promedio es el de train, puesto que en test todos son NaN.
    """
    total_viviendas = len(df)
    
    # Agrupar los datos por la columna especificada y calcular el precio promedio y el número de viviendas
    resultado = df.groupby([columna_agrupacion]).agg(
        Precio_Promedio=('SalePrice', 'mean'),  
        Num_Viviendas=('SalePrice', 'size')     
    ).reset_index()
    
    # Calcular el número de viviendas en train y test para cada grupo
    num_train = df[df['Dataset'] == 'train'].groupby(columna_agrupacion).size().reindex(resultado[columna_agrupacion], fill_value=0)
    num_test = df[df['Dataset'] == 'test'].groupby(columna_agrupacion).size().reindex(resultado[columna_agrupacion], fill_value=0)
    
    # Calcular el porcentaje de viviendas en cada grupo
    resultado['Porcentaje_Viviendas'] = (resultado['Num_Viviendas'] / total_viviendas) * 100

      # Contar el número de viviendas por cada categoría de la columna de agrupación
    conteo = df[columna_agrupacion].value_counts().reindex(resultado[columna_agrupacion], fill_value=0)
    resultado['Num_Viviendas'] = conteo.values  

    # Agregar las columnas de números de viviendas en train y test
    resultado['Num_V_Train'] = num_train.values
    resultado['Num_V_Test'] = num_test.values

    # Ordenar el DataFrame por Precio_Promedio de forma descendente
    resultado = resultado.sort_values(by='Precio_Promedio', ascending=False)
    
    return resultado




def calcular_correlaciones(df, columnas_numericas):
    """    
    Esta función evalúa la correlación de Pearson, Spearman y Kendall para cada par de columnas
    en la lista `columnas_numericas`. Si la correlación absoluta de cualquiera de los métodos es
    mayor o igual a 0.5, se almacena el par de columnas junto con sus correlaciones en un DataFrame.
    """
    correlaciones = []

    for i, j in itertools.combinations(columnas_numericas, 2):
        corr_pearson = df[i].corr(df[j], method='pearson')
        corr_spearman = df[i].corr(df[j], method='spearman')
        corr_kendall = df[i].corr(df[j], method='kendall')

        if abs(corr_pearson) >= 0.5 or abs(corr_spearman) >= 0.5 or abs(corr_kendall) >= 0.5:
            correlaciones.append((i, j, corr_pearson, corr_spearman, corr_kendall))

    correlaciones_df = pd.DataFrame(correlaciones, columns=['Columna_1', 'Columna_2', 'Correlación_Pearson', 'Correlación_Spearman', 'Correlación_Kendall'])
    correlaciones_df = correlaciones_df.sort_values(by='Columna_1')
    
    return correlaciones_df


def label_encoding(df, columna):
    """
    Realiza una codificación tipo Label Encoding para la variable categórica, aplicando el encoding únicamente
    en el conjunto de entrenamiento (train) para evitar data leakage.
    """
    # Filtrar el conjunto de entrenamiento
    df_train = df[df['Dataset'] == 'train']
    
    # Generar un mapa de codificación (Label Encoding) en base al conjunto de entrenamiento
    categorias_unicas = df_train[columna].unique()
    mapa_codificacion = {categoria: idx for idx, categoria in enumerate(categorias_unicas)}
    
    # Aplicar el mapeo de codificación a todo el DataFrame (train y test)
    df[columna] = df[columna].map(mapa_codificacion)
    
    return df


def codificacion_ponderada(df, columna, objetivo, min_muestras=10):
    """
    Realiza una codificación de la variable categórica ponderando el precio promedio y el porcentaje de observaciones 
    por categoría utilizando únicamente el conjunto de entrenamiento (train) para el cálculo de la codificación.
    
    La variable objetivo siempre es SalePrice

    min_muestras: Umbral mínimo para aplicar el suavizado.
    

    """
    # Filtrar el conjunto de entrenamiento
    df_train = df[df['Dataset'] == 'train']
    
    # Calcular la media global del objetivo en el conjunto de entrenamiento
    media_global = df_train[objetivo].mean()
    
    # Agrupar por la columna categórica en el conjunto de entrenamiento
    agrupacion = df_train.groupby(columna)[objetivo].agg(['mean', 'count'])
    total_muestras_train = len(df_train)
    agrupacion['porcentaje'] = agrupacion['count'] / total_muestras_train  # Porcentaje de datos por categoría en train
    
    # Suavizar la media según el conteo y aplicar un ajuste basado en el porcentaje de datos
    agrupacion['suavizado'] = ((agrupacion['mean'] * agrupacion['count'] + media_global * min_muestras) / 
                               (agrupacion['count'] + min_muestras)) * agrupacion['porcentaje']
    
    # Crear un mapeo de la columna categórica a la media suavizada ponderada
    mapa_codificacion = agrupacion['suavizado'].to_dict()
    
    # Aplicar el mapeo a la columna en el DataFrame completo (df)
    df[columna] = df[columna].map(mapa_codificacion)






def visualizar_correlaciones(df, variables):
    """
    Función simplificada para visualizar las correlaciones entre un número inespecífico de variables.

    Parámetros:
    df (pd.DataFrame): El DataFrame que contiene los datos.
    variables (list): Lista de nombres de las columnas que se desean incluir en la matriz de correlación.
    """
    fig = px.imshow(
        img=round(df[variables].corr(), 1),
        text_auto=True,
        title="Correlaciones Lineales"
    )
    fig.update_layout(title_x=0.5)
    fig.show()



def visualizar_correlaciones_grandes(df, variables):
    """
    Función simplificada para visualizar las correlaciones entre un número inespecífico de variables.

    Parámetros:
    df (pd.DataFrame): El DataFrame que contiene los datos.
    variables (list): Lista de nombres de las columnas que se desean incluir en la matriz de correlación.
    """
    # Calcular la matriz de correlación
    correlacion = round(df[variables].corr(), 2)
    
    # Crear la figura con tamaño personalizado
    fig = px.imshow(
        correlacion,
        text_auto=True,
        title="Correlaciones Lineales")
    
    # Actualizar la disposición de la figura
    fig.update_layout(
        title_x=0.5,
        width=1000,  # Ancho de la figura
        height=800,  # Alto de la figura
        font=dict(size=14),  # Tamaño de fuente
        margin=dict(l=40, r=40, t=40, b=40)  # Márgenes
    )
    
    fig.show()



def aplicar_codificacion_ordinal_especifica(df, columna, categorias):
    """
    Aplica Codificación Ordinal a una columna específica del DataFrame y sobrescribe la columna .

    """

    codificador_ordinal = OrdinalEncoder(categories=[categorias])
    df[columna] = codificador_ordinal.fit_transform(df[[columna]])

    return df



# def rellenar_atributos_sotano(df, columna_atributo):
#     """
#     Rellena los valores nulos de una columna de atributos relacionados con el sótano 
#     cuando la casa no tiene sótano, asignando 'NoAplica'.

#     """
    
#     df[columna_atributo] = df[columna_atributo].where(
#         ~((df["TieneSotano"] == 0) & (df[columna_atributo].isna())),
#         other='NoAplica')

# def rellenar_atributos_categoricos_sotano(df, columna_atributo):
#     """
#     Rellena los valores nulos de una columna de atributos relacionados con el sótano 
#     cuando la casa no tiene sótano, asignando 'NoAplica'.

#     Además, verifica si existen inconsistencias, es decir, valores no nulos 
#     en casas donde 'TieneSotano' es 0, y los reemplaza por 'NoAplica'.
#     """
#     # Verificar inconsistencias
#     inconsistencias = df[(df["TieneSotano"] == 0) & (~df[columna_atributo].isna())]
#     if not inconsistencias.empty:
#         print(f"Se encontraron {len(inconsistencias)} inconsistencias en la columna '{columna_atributo}'.")
    
#     # Rellenar valores nulos e inconsistentes
#     df[columna_atributo] = df[columna_atributo].where(
#         ~((df["TieneSotano"] == 0) & (df[columna_atributo].isna())),
#         other='NoAplica'
#     )
#     # Corregir inconsistencias (valores no nulos con TieneSotano == 0)
#     df.loc[df["TieneSotano"] == 0, columna_atributo] = 'NoAplica'

# def rellenar_atributos_numericos_sotano(df, columna_atributo):
#     """
#     Rellena los valores nulos de una columna de atributos relacionados con el sótano 
#     cuando la casa no tiene sótano, asignando 0 en lugar de 'NoAplica' para valores numéricos.

#     Además, verifica si existen inconsistencias, es decir, valores no nulos 
#     en casas donde 'TieneSotano' es 0, y los reemplaza por 0.
#     """
#     # Verificar inconsistencias
#     inconsistencias = df[(df["TieneSotano"] == 0) & (~df[columna_atributo].isna())]
#     if not inconsistencias.empty:
#         print(f"Se encontraron {len(inconsistencias)} inconsistencias en la columna '{columna_atributo}'.")
    
#     # Rellenar valores nulos e inconsistentes con 0 cuando no hay sótano
#     df[columna_atributo] = df[columna_atributo].where(
#         ~((df["TieneSotano"] == 0) & (df[columna_atributo].isna())),
#         other=0
#     )
    
#     # Corregir inconsistencias (valores no nulos con TieneSotano == 0)
#     df.loc[df["TieneSotano"] == 0, columna_atributo] = 0



def rellenar_atributos_sotano(df, columna_atributo):
    """
    Rellena los valores nulos de una columna de atributos relacionados con el sótano 
    cuando la casa no tiene sótano. 

    - Si la columna es numérica, imputa valores faltantes con 0.
    - Si la columna es categórica, imputa valores faltantes con 'NoAplica'.

    Además, corrige inconsistencias: valores no nulos en filas donde 'TieneSotano' es 0.

    Parámetros:
        df: DataFrame
        columna_atributo: str, nombre de la columna a imputar.
    """
    # Determinar si la columna es numérica o categórica
    es_numerico = df[columna_atributo].dtype in ['int64', 'float64']

    # Definir el valor de imputación según el tipo de columna
    valor_imputacion = 0 if es_numerico else 'NoAplica'

    # Verificar inconsistencias
    # Se consideran inconsistencias solo si 'TieneSotano' es 0 y el valor no es ni NaN ni 0
    inconsistencias = df[(df["TieneSotano"] == 0) & (~df[columna_atributo].isin([0, np.nan]))]
    if not inconsistencias.empty:
        print(f"Se encontraron {len(inconsistencias)} inconsistencias en la columna '{columna_atributo}'.")

    # Rellenar valores nulos e inconsistentes
    df[columna_atributo] = df[columna_atributo].where(
        ~((df["TieneSotano"] == 0) & (df[columna_atributo].isna())),
        other=valor_imputacion
    )

    # Corregir inconsistencias (valores no nulos con TieneSotano == 0)
    df.loc[df["TieneSotano"] == 0, columna_atributo] = valor_imputacion




def codificacion_loo(df, columna, objetivo="SalePrice"):
    """
    Aplica codificación Leave-One-Out (LOO) a una columna categórica, sobrescribiendo la columna original.
    Se aplica sin que haya data leakage ya que está utilizando solo los datos de entrenamiento para codificar los datos de prueba. 
    Filtra el conjunto de entrenamiento y prueba, inicializa el codificador LOO, codifica el conjunto de entrenamiento 
    (ajustar y transformar) y luego codificar el conjunto de prueba (solo transformar).

    """

    df_train = df[df['Dataset'] == 'train']
    df_test = df[df['Dataset'] == 'test']
    
    loo_encoder = ce.LeaveOneOutEncoder(cols=[columna])

    df.loc[df['Dataset'] == 'train', columna] = loo_encoder.fit_transform(df_train[[columna]], df_train[objetivo])
    df.loc[df['Dataset'] == 'test', columna] = loo_encoder.transform(df_test[[columna]])

    return df



def graficar_conteo_clases(df, columna, columna_dataset='Dataset', titulo=None, colores=['turquoise', 'coral']):
    """
    Genera un gráfico de barras para contar las ocurrencias de cada clase en una columna específica.
    """
    # Contar las ocurrencias de cada clase en la columna especificada para train y test
    conteo_datos = df.groupby([columna, columna_dataset]).size().reset_index(name='count')

    if titulo is None:
        titulo = f"Conteo de {columna} en Train y Test"

    fig = px.bar(conteo_datos, x=columna, y="count", color=columna_dataset, barmode="group",
                 title=titulo, color_discrete_sequence=colores)
    fig.update_layout(xaxis_title=columna, yaxis_title='Conteo', 
                      title_x=0.5, xaxis={'categoryorder': 'total descending'})
    fig.show()


def crear_histograma(df, columna, title="Histograma", color="green", nbins=20):
    """
    Crea un histograma.
    """
    fig = px.histogram(df, x=columna, nbins=nbins, 
                       title=title, 
                       labels={columna: columna},
                       color_discrete_sequence=[color])

    fig.update_layout(
        title_x=0.5,  
        xaxis_title=columna,
        yaxis_title="Frecuencia")

    fig.show()


def boxplot_train_test(df, columna, color_columna, title="Box Plot", nbins=20):
    """
    Crea un Box Plot de train y test.
    """
    fig = px.box(df, 
                 x=columna, 
                 color=color_columna, 
                 title=title)

    fig.update_layout(
        title_x=0.5,  
        xaxis_title=columna,
        yaxis_title="Distribución"
    )

    fig.show()

def distribucion_target_con_variable(df, target, feature, title=None):
    """
    Función para generar un gráfico de caja mostrando la distribución de un target por una característica (feature) en Train.
    
    """
    if title is None:
        title = f'Distribución de {target} por {feature}'
    
    # Crear el gráfico de caja
    fig = px.box(df, x=target, y=feature, 
                 title=title, 
                 labels={feature: feature, target: target})

    fig.update_layout(
        xaxis_title=feature, 
        yaxis_title=target, 
        title_x=0.5, 
         xaxis = {'categoryorder': 'total descending'}
        )
    
    fig.show()


def distribucion_target_con_variable_vertical(df, target, feature, title=None):
    """
    Función para generar un gráfico de caja mostrando la distribución de un target por una característica (feature) en Train en vertical.
    
    """
    if title is None:
        title = f'Distribución de {target} por {feature}'

    fig = px.box(df, x=feature, y=target, 
                                  title=title, 
                 labels={target: target, feature: feature})

    fig.update_layout(
    yaxis_title= target, 
    xaxis_title=feature, 
    title_x=0.5, height=600,
    xaxis={'categoryorder': 'total descending'})

    fig.show()


def describe_train_test(df, variable):
    train_describe = df[df['Dataset'] == 'train'][variable].describe()
    test_describe = df[df['Dataset'] == 'test'][variable].describe()
    describe_train_test = pd.concat([train_describe, test_describe], axis=1)
    describe_train_test.columns = ['Train', 'Test']
    return describe_train_test