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

## Evalúa el modelo con un conjunto de prueba y un conjunto de validación
## Detecta correctamente el grado de bias o sesgo: bajo medio alto
__Low Bias:__ Weak assumptions regarding the functional form of the mapping of inputs to outputs.

__High Bias:__ Strong assumptions regarding the functional form of the mapping of inputs to outputs

## Detecta correctamente el grado de varianza: bajo medio alto
__Low Variance:__ Small changes to the model with changes to the training dataset.

__High Variance:__ Large changes to the model with changes to the training dataset.

## Explica el nivel de ajuste del modelo: underfitt fitt overfit
## Utiliza técnicas de regularización para mejorar el desempeño del modelo
