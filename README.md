# Momento de Retroalimentación: Módulo 2 Análisis y Reporte sobre el desempeño del modelo.

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

## Análisis del grado de sesgo o bias y varianza
**SESGO O BIAS**
* __Bajo:__ Supuestos débiles con respecto a la forma funcional de la asignación de entradas a salidas
* __Alto:__ Fuertes supuestos con respecto a la forma funcional del mapeo de entradas a salidas

**VARIANZA**
* __Baja:__ Pequeños cambios en el modelo con cambios en el conjunto de datos de entrenamiento
* __Alta:__ Grandes cambios en el modelo con cambios en el conjunto de datos de entrenamiento

![image](https://user-images.githubusercontent.com/101605777/189572479-00a08a6b-e8e5-4c20-92c0-f16e657bd98c.png)

Estos fueron los promedio de sesgo y varianza de cada una de las muestras para entrenar y probar el modelo:
|Muestra|Sesgo prom.|Varianza prom.|
|-------|-----------|--------------|
|1|4408.923|223.173|
|2|5774.135|346.702|
|3|4257.437|220.319|
|4|4593.347|437.855|
|5|1588.349|223.119|

Podemos ver que en promedio se tiene menos varianza entre las diferentes pruebas y que puede ser una varianza. Por otro lado,el sesgo promedio entre muestras vemos que varía un poco más por lo que puede tratarse de que nuestro modelo tiene un sesgo un poco alto.

## Nivel de ajuste del modelo
* **Subajustado:** alto sesgo y poca varianza -> error de entrenamiento y prueba alto 
* **Sobreajustado:** bajo sesgo y alta varianza -> error de  entrenamiento bajo y error de prueba alto
* **Balanceado:** bajo sesgo y poca varianza (ideal) -> error de entrenamiento y prueba bajo


## Utiliza técnicas de regularización para mejorar el desempeño del modelo
En la siguiente tabla podemos encontrar como es que mejoro o no el modelo (__RL__) con las técnicas de regularización y ver el desempeño del modelo usando los métodos de __sklearn__ de __Lasso__ y __Rigde__ para las técnicas de __L1__ y __L2__ respectivamente para las 5 muestras aleatorias que tomamos.
| Muestra | Modelo |$r^2(Train)$ | $r^2(Test)$ |    ECM    |
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

Podemos ver que no hay una gran diferencia diferencia en cuanto al uso de técnicas de regularización tanto los método de L1 y L2 varían entre ellas y nuestro modelo original en a partir de 6 cifras decimales por lo que podemos decir que no hay una mejora tan significativa usando técnicas de regularización específicamente para nuestro, por lo que podemos concluir que nuestro modelo si es muy bueno para predecir datos de nuestro dataset y que por lo tanto es un modelo balanceado ya que posee poca varianza y poco sesgo.
