# Proyecto-2-modulo-4

# Proyecto de Predicción de Potabilidad del Agua
## Descripción
Este proyecto tiene como objetivo predecir la potabilidad del agua utilizando el conjunto de datos water-potability-ds.csv. El objetivo es crear un modelo que pueda determinar si una muestra de agua es potable o no. El conjunto de datos y los experimentos se llevaron a cabo en un Jupyter Notebook llamado model-prediction.ipynb, la tarea es operacionalizar la creación del modelo a través de MLOps y construir un pipeline en Azure ML Studio basado en los experimentos y el informe generados por el equipo de Ciencia de Datos.
## Procedimiento
1. Identificación y categorización de las partes relevantes del Jupyter Notebook para el pipeline.
2. Diseño y creación de los componentes necesarios para el pipeline utilizando el SDK de Azure ML, en este caso se utilizaran 6 componentes donde:
    - El primer compoente se encargara de realizar un filtrado y el procesamiento del dataset descargado para tener un dataset limpio y sin valores nulos.
   
    - El segundo componente se encarga de realizar la division del data para los componentes de entrenamiento (train_dt y train_lr), validacion (Score) y evaluacion (Eval).
   
    - El tercer y cuarto componente es el encargado de realizar el entrenamiento del modelo, en este caso se realizaran dos componentes de entrenamiento (LogisticRegression y DecisionTreeClassifier).
   
    - El quito componente realizara el procedimiento de validacion (Score), este componente se utilizara dos veces para cada uno de los entrenamientos.
   
    - el sexto compoente realizara el procedimiento de evalucion (Eval), este componente se utilizara dos veces para cada uno de los entrenamientos.
   
4. Creación de un pipeline en Azure ML conectando los componentes previamente diseñados, como se puede observar en el archivo "" se crearon utilizaron 8 compoentes excluyendo el dataset, pero se utilizo dos veces el componente de validacion (Score) y evaluacion(Eval).
6. Las salidas del pipeline que se encuentran en la carpeta "pipeline_output/named-outputs" que incluyen:
    - Un gráfico de correlación de variables independientes en formato .jpg ("pipeline_output/named-outputs/pipeline_correlacion")
    - El modelo entrenado en formato .pkl ("pipeline_output/named-outputs/pipeline_modelo_dt" y "pipeline_output/named-outputs/pipeline_modelo_lr")
    - Informe de métricas de evaluación del modelo en formato .csv ("pipeline_output/named-outputs/pipeline_metrica_dt" y "pipeline_output/named-outputs/pipeline_metrica_lr")
7. Descargar las salidas del pipeline utilizando el SDK de Azure ML.
## Requisitos
- Python 3.x
- Dependencias específicas mencionadas en las instrucciones de instalación
## Uso
El uso del proyecto está detallado en las secciones específicas del proyecto del README para guiar a los usuarios sobre cómo trabajar con los datos, configurar los modelos y gestionar el pipeline.

## Créditos
Este proyecto otorga créditos y reconocimientos a los desarrolladores del conjunto de datos original: https://www.kaggle.com/datasets/sooyoungher/
