# Modelo predictivo para la selección de personal

Hola! Soy Ronaldo Farid Nolasco Chavez, ingeniero de sistemas de la UNI.

El presente proyecto consiste en un modelo predictivo, el cual se encarga de pronósticar si un empleado debería ser contratado o no para un puesto de trabajo en una empresa relacionada al rubro de consultoría tecnológica.

Se utilizaron las 6 etapas de la metodología CRISP-DM para la elaboración del modelo, dónde cada etapa se adaptó el proyecto con las siguientes actividades:

> Cada etapa tiene una carpeta con sus recursos propios, la cual se encuentra entre paréntesis.

1. Comprensión del negocio **(es una tarea ajena a programación)**
2. Comprensión de los datos (2-data-understanding/)
   - Lectura y procesamiento de datos
   - Etiquetado de la variable objetivo
   - Descripcion general de los datos
3. Preparación de los datos (3-data-preparation/)
   - Eliminación de columnas
   - Remplazo de valores nulos y atípicos
   - Visualización de datos
4. Modelado (4-modelling/)
   - Balanceo de datos
   - Codificación de variables categóricas
   - Normalización de variables numéricas
   - Eliminación de columnas por varianza y correlación
   - Entrenamiento y prueba de los modelos
   - Selección del mejor algoritmo
5. Evaluación (5-evaluation/)
   - Aplicación de las técnicas de validación
   - Comparación de los resultados de las técnicas de validaci
   - Selección de la mejor técnica de validación
6. Despliegue **(se encuentra en la siguiente sección)**

> Adicional a ello, hay una carpeta llamada 'results/' donde se encuentra el análisis estadístico empleado para las pruebas de normalidad y las pruebas de hipótesis (es aparte al modelo).

## Uso (despliegue)

Para poder utilizar el modelo, sigue los siguientes pasos:

1. Asegúrate de cumplir con la instalación de los siguientes programas con su versión correspondiente:

| Programa | Versión |
| ----------- | ----------- |
| Sistema operativo | Windows 10 Pro 22H2 19045.3086 |
| Anaconda | Anaconda3 2023.03-1 |
| Python | 3.10.9 64-bit |
| Visual Studio Code | 1.79.2 |
| Git | 2.40.1.windows.1 |

2. Clona el proyecto en una carpeta local utilizando el comando: `git clone https://github.com/RonaldoNolasco/personal-thesis-development.git`
2. Carga la carpeta clonada en el editor Visual Studio Code
3. Una vez cargada, accede a cualquiera de los archivos .ipynb (cada etapa tiene su notebook correspondiente).
4. Ejecuta el proyecto desde la opción Run All en la parte superior del notebook!

> Cada etapa tiene una carpeta llamada 'output/' donde se guardan los resultados de las ejecuciones de los notebooks.

## Contribución

Los forks y pull request son bienvenidos. Para cambios importantes, primero abre un issue para discutir lo que le gustaría cambiar.
