import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import learning_curve
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error, root_mean_squared_log_error, make_scorer


def graficar_curva_aprendizaje_rmsle(modelo, X, y):
    # Crear el scorer para RMSLE. greater_is_better=False: RMSLE es más bajo cuando es mejor
    rmsle_scorer = make_scorer(root_mean_squared_log_error, greater_is_better=False)
    
    train_sizes, train_scores, test_scores = learning_curve(
        modelo, X, y, cv=5, n_jobs=-1,
        train_sizes=np.linspace(0.1, 1.0, 10),
        scoring=rmsle_scorer
    )

    # Convertir las puntuaciones a positivas (ya que están como valores negativos)
    train_scores_mean = -np.mean(train_scores, axis=1)
    test_scores_mean = -np.mean(test_scores, axis=1)
    train_scores_std = np.std(-train_scores, axis=1)
    test_scores_std = np.std(-test_scores, axis=1)

    # Graficar la curva de aprendizaje
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_scores_mean, 'o-', color='r', label='Puntuación de Entrenamiento (RMSLE)')
    plt.plot(train_sizes, test_scores_mean, 'o-', color='g', label='Puntuación de Validación (RMSLE)')
    
    # Rellenar las áreas de desviación estándar
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1, color='r')
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color='g')

    plt.title(f'Curva de Aprendizaje (RMSLE): {modelo.__class__.__name__}')
    plt.xlabel('Tamaño del Conjunto de Entrenamiento')
    plt.ylabel('RMSLE')
    plt.legend(loc='best')
    plt.grid()
    plt.show()


def feature_importances(model, X_train, top_n=30, ascending=False, palette="viridis"):
    """
    Grafica las importancias de características de un modelo.

    Parámetros:
    - model: Modelo entrenado que contiene las importancias de características.
    - X_train: Conjunto de entrenamiento utilizado, que contiene los nombres de las características.
    - top_n: Número de características a mostrar (por defecto, 30).
    - ascending: Orden de las características, False para las más importantes, True para las menos.
    - palette: Paleta de colores para el gráfico (por defecto, "viridis").
    """
    # Obtener las importancias de características
    importances = model.feature_importances_

    # Crear el DataFrame
    df_importances = pd.DataFrame(data=zip(X_train.columns, importances),
                                  columns=["Columnas", "Importancia"])

    # Ordenar y seleccionar el top_n
    df_importances = df_importances.sort_values("Importancia", ascending=ascending)
    df_top_importances = df_importances.head(top_n)

    # Definir el título
    title = f"Las {top_n} características {'menos' if ascending else 'más'} importantes"
    
    # Graficar
    plt.figure(figsize=(10, 6))
    plt.title(title)
    sns.barplot(x="Importancia", y="Columnas", data=df_top_importances, palette=palette, hue="Columnas", legend=False)
    plt.grid()
    plt.show()


def calcular_metricas_rendimiento(modelo, X_val, y_val, yhat):
    """
    Calcula las métricas de rendimiento R², MAE, RMSE, MSE, RMSLE para evaluar la precisión
    de un modelo de regresión utilizando las predicciones y los valores reales.

    """
    r2 = r2_score(y_val, yhat)  # R²: Coeficiente de determinación
    mae = mean_absolute_error(y_val, yhat)  # MAE: Error absoluto medio
    rmse = root_mean_squared_error(y_val, yhat)  # RMSE: Raíz del error cuadrático medio
    mse = rmse ** 2  # MSE: Error cuadrático medio
    rmsle = root_mean_squared_log_error(y_val, yhat)  # RMSLE: Error cuadrático medio logarítmico

    return pd.DataFrame([[str(modelo), r2, mae, rmse, mse, rmsle]],
                        columns=["Modelo", "R²", "MAE", "RMSE", "MSE", "RMSLE"])


def revisar_predicciones(predicciones, test, df_predicciones, train=None):
    """
    Valida las predicciones generadas por un modelo, asegurando la consistencia y la integridad de los datos.
        
    """

    # Validar que el número de predicciones coincida con los datos de prueba
    if len(predicciones) != len(test):
        raise ValueError("Cantidad de predicciones incorrecta.")
    else:
        print("Coincide el número de predicciones del modelo con las proporcionadas.")
    
    # Validar que no haya valores nulos en la columna 'SalePrice'
    if df_predicciones['SalePrice'].isnull().any():
        raise ValueError("Existen valores nulos en la columna 'SalePrice'.")
    else:
        print("No hay valores nulos en SalePrice.")
    
    # Validar que no haya duplicados en la columna 'Id'
    if df_predicciones['Id'].duplicated().any():
        raise ValueError("La columna 'Id' contiene duplicados.")
    else:
        print("La columna 'Id' no tiene duplicados.")
    
    # Validar que no haya valores negativos en la columna 'SalePrice'
    if (df_predicciones['SalePrice'] < 0).any():
        raise ValueError("Existen valores negativos en las predicciones.")
    else:
        print("No hay valores negativos en SalePrice.")

    if train is not None and 'SalePrice' in train.columns:
            comparacion = pd.concat([
                df_predicciones['SalePrice'].describe().to_frame(name="Predicciones"),
                train['SalePrice'].describe().to_frame(name="Entrenamiento")
            ], axis=1)
            print("\nComparación estadística entre predicciones y entrenamiento:")
            print(comparacion)
