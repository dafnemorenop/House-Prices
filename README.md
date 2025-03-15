# **House Prices: Predicción de Precios de Casas**  

Este proyecto está basado en el reto [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) de Kaggle.  

---

## **Descripción**  

**Predicción de Precios de Casas**: Este proyecto busca construir un modelo de regresión avanzado que permita predecir el precio de venta (*SalePrice*) de propiedades residenciales, utilizando características estructurales y contextuales.  

El flujo de trabajo incluye:  
- Análisis exploratorio de datos (EDA).  
- Preprocesamiento y transformación de variables.  
- Entrenamiento de modelos predictivos de aprendizaje automático.  
- Evaluación y optimización de modelos, destacando **ExtraTreesRegressor** como el más eficiente.  

Se emplea la métrica RMSLE (*Root Mean Squared Logarithmic Error*), estándar en la competencia, para evaluar el rendimiento del modelo.  

---

## **Estructura del Proyecto**  

El repositorio está organizado en las siguientes carpetas y archivos:  

- **`README.md`**: Este archivo, con la descripción y guía del proyecto.  
- **`requirements.txt`**: Archivo para instalar las dependencias necesarias con `pip install -r requirements.txt`.  
- **`data`**: Contiene los archivos relacionados con los datos de entrada y salida:  
  - `train.csv` y `test.csv`: Archivos originales de Kaggle.  
  - `Inmobiliaria_Horizonte.pkl`: Datos combinados y preprocesados.  
  - `Inmobiliaria_Horizonte_limpio.pkl`: Datos limpios tras el EDA inicial. 
  - `train.pkl` y `test.pkl`: Archivos limpios para los modelos.   

- **`docs`**: Incluye documentación adicional:  
  - `descripcion_variables.md`: Descripción detallada de las variables del conjunto de datos.  

- **`notebooks`**: Cuadernos Jupyter para el desarrollo del proyecto:  
  - `01_data_cleaning.ipynb`: Limpieza inicial y unión de datos.  
  - `02_eda_1_cleaning.ipynb`: Análisis exploratorio y limpieza de variables.  
  - `02_eda_2_transformation.ipynb`: Transformación de datos y separación en conjuntos de train/test.  
  - `03_regression_model.ipynb`: Entrenamiento y evaluación de modelos de regresión.  

- **`outputs`**: Resultados generados por los modelos:  
  - `.csv` con las predicciones de distintos modelos. 
    **Mejor modelo hasta el momento:**  
      - `predicciones_XGBRegressor.csv` 

- **`src`**: Módulos Python con funciones auxiliares:  
  - `data_processing.py`: Funciones para limpieza y preparación de datos.  
  - `data_visualization.py`: Funciones para análisis visual y transformación.  
  - `regression_model.py`: Funciones relacionadas con el entrenamiento y evaluación de modelos.  

---

## **Instalación de Librerías**  

Para que funcionen todas las métricas, asegúrate de tener instalada la última versión de scikit-learn: 1.5.2 y numpy 2.0

Para ejecutar los scripts del proyecto, instala las librerías necesarias ejecutando:  

```bash
pip install -r requirements.txt
