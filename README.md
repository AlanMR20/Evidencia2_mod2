# Momento de Retroalimentación: Módulo 2 Análisis y Reporte sobre el desempeño del modelo.

# AÚN NO ESTÁ LISTO

## Dataset utilizado
Para esta evidencia recuperaremos una implementación previa que este caso será sobre el dataset de **Fish Market**, donde se hará un análisis del modelo que habíamos seleccionado al final y veremos el tipo de sesgo, varianza, el tipo de ajuste que tiene el modelo y al final utilizaremos una técnica de regularización para mejorar el desempeño del modelo.

### Modelo del dataset
Para este dataset recordemos que habíamos creado modelos con diferentes características, donde al final se escogió el modelo más simple que tenía mejor rendimiento para nuestra variable de interés que es el peso  del pez en gramos (__Weight__), dicho modelo posee las siguientes características:
* __Height:__ Altura del pez (cm)
* __Width:__ Anchura diagonal del pez (cm)
* __L123:__ Contiene la raíz cúbica del producto de las longitudes 1,2 y 3
* __WidthXL123:__ La interacción entre Anchura y __L123__

Por lo que nuestro modelo de regresión lineal múltiple nos quedó de la siguiente manera:
$h_{weight}=\theta_1x_{height}+\theta_2x_{width}+\theta_3x_{L123}+\theta_4x_{widthXL123}$

## Evaluación del modelo con conjuntos de entrenamiento y prueba
 Se corrieron 5 muestras aleatorias para poder entrenar, probar y validar el modelo donde se obtuvieron los siguientes rendimientos.
| Muestra | $r^2(Train)$ | $r^2(Test)$ |    ECM    |
|---------|--------------|-------------|-----------|
|    1    |    97.5444%  |   96.6240%   |  4253.56  |
|    2    |    97.6376%  |   95.7447%   |  5816.99  |
|    3    |    97.8158%  |   94.4075%   |  4191.11  |
|    4    |    97.5779%  |   95.9650%   |  4582.56  |
|    5    |    97.1935%  |   97.9089%   |  1644.08  |

Podemos ver que los datos predecidos por el modelo realmente se acercan a los valores reales; sin embargo, esta no es la única forma en la que se tiene para decir si nuestro modelo es lo suficientemente bueno como para poder confiar en las estimaciones que nos arroja de los valores. Por lo que vamos a tener que hacer un análisis sobre el sesgo o bias y la varianza de los datos obtenidos del modelo y observar el tipo de ajuste que tiene nuestro modelo.

## Análisis del grado de sesgo o bias
__Low Bias:__ Weak assumptions regarding the functional form of the mapping of inputs to outputs.
__High Bias:__ Strong assumptions regarding the functional form of the mapping of inputs to outputs

## Análisis del grado de varianza
__Low Variance:__ Small changes to the model with changes to the training dataset.
__High Variance:__ Large changes to the model with changes to the training dataset.

## Explica el nivel de ajuste del modelo: underfitt fitt overfit

## Utiliza técnicas de regularización para mejorar el desempeño del modelo
| Muestra | Tipo |$r^2(Train)$ | $r^2(Test)$ |    ECM    |
|---------|----- |-------------|-------------|-----------|
|1|RL|97.54437019% | 96.62397438%|4253.560749|
|1|L1|97.54436962%|96.62332606%|4254.377584|
|1|L2|97.54436983% | 96.62342038%|4254.258749|
|2|RL|97.63755155% | 95.74467018%|5816.989804|
|2|L1|97.63755099%|95.74364174%|5818.395669|
|2|L2|97.63755124% | 95.74383973%|5818.125017|
|3|RL| 97.81581284% |  94.40751838%|4191.107047|
|3|L1|97.81581240%|94.40784534%|4190.862020|
|3|L2|97.81581250%| 94.40791485%|4190.809927|
|4|RL|97.57792952% | 95.96497547%|4582.558173|
|4|L1|97.57792897%|95.96604281%|4581.345995|
|4|L2|97.57792902%| 95.96611975%|4581.258615|
|5|RL|97.19346661%| 97.90892849%|1644.081232|
|5|L1|97.19346615%|97.90913019%|1643.922649|
|5|L2|97.19346625%| 97.90928554%|1643.800507|
