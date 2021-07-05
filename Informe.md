# Base de Datos 2 - Proyecto 2
### Integrantes
- Anthony Guimarey Saavedra
- Massimo Imparato Conetta
- Sebastian Knell Noriega

## Índice
  - [Introducción](#introducción)
  - [Implementación](#implementación)
    - [Construcción del índice invertido](#construcción-del-índice-invertido)
    - [Manejo en memoria secundaria](#manejo-en-memoria-secundaria)
    - [Ejecución óptima de consultas](#ejecución-óptima-de-consultas)
  - [Prueba de uso](#prueba-de-uso)
  - [Anexos](#anexos)

## Introducción
El objetivo de este proyecto fue implementar un índice invertido para tareas de búsqueda y recuperación en documentos de texto en base al modelo de recuperación por ranking y probar su desempeño mediante consultas en lenguaje natural. Para ello se construyó una aplicación frontend que realiza una búsqueda textual relacionado a ciertos temas de interés. Los resultados de búsqueda se obtienen aplicando la similitud de coseno sobre el índice invertido. Se uso un conjunto de datos de prueba obtenido de [Kaggle](https://www.kaggle.com/datasets). Este conjunto de datos está conformado por artículos de diferentes periódicos, que incluyen New York Times, CNN, Fox News, entre otros. Las publicaciones se encuentran principalmente entre los años 2016 y 2017. De acuerdo a lo aprendido, se espera obtener un alto grado de precisión a la consulta ingresada por el usuario, es decir, del conjunto de documentos recuperados, la mayoría son documentos relevantes para el usuario.

## Implementación
## Construcción del índice invertido
Para construir el índice invertido usamos la función `buildIndex()` que se muestra a continuación.
```python
def buildIndex():
    file = pd.read_csv(DATA_FILE, encoding='UTF-8')
    termIndex = {}
    docNorms = {}
    for id, row in file.iterrows():
        text = row['title'] + ' ' + row['content']
        words = parse(text)
        
        tf = getTermFrequenies(words)
        vector = np.array([item[1] for item in tf.items()])
        docNorms[id] = np.linalg.norm(vector)

        for token in words:
            if len(token) > 0 and token in termIndex.keys():
                if id in termIndex[token].keys():
                    termIndex[token][id] += 1
                else:
                    termIndex[token][id] = 1
            else:
                termIndex[token] = {id: 1}

    termIndex = dict(sorted(termIndex.items(), key=lambda elem: elem[0]))
    writeIndex(termIndex, TERM_INDEX_FILE)
    with open(DOC_NORMS_FILE, 'w+') as outFile:
        outFile.writelines(str(docNorms))
```

Debido a que nuestra colección de documentos esta en un archivo csv, empezamos leyendo este archivo. Para ello nos ayudamos de la función `read_csv` de pandas. Luego iteramos por cada fila, que en este caso representa un documento, y tokenizamos el texto concatenando el título del documento con su contenido. Para ello se uso la función `parse` que se puede ver en [tokenizer.py](./src/tokenizer.py). Esta se encarga del proceso de tokenización utilizando la librería `nltk` así como de filtración de stopwords y stemming. Luego almacenamos estos tokens o términos en el diccionario `termIndex`. Este sera un diccionario de 2 dimensiones en el cual se almacenará para cada término un diccionario que contiene el id y la frecuencia de este para cada documento en el que aparece. Sin embargo, al escribiro a un archivo lo tratamos como el id separado por un espacio a una lista de tuplas. Además, mantenemos el diccionario `docNorms` el cual ira guardando el factor de normalización de cada documento. Para esto último nos ayudamos de la librería numpy. Finalmente, escribimos ambos archivos a disco.


## Manejo en memoria secundaria
Nuestra implementación mantiene 2 archivos en disco los cuales se cargan al correr el servidor: el índice invertido y los factores de normalización de cada documento. Inicialmente se intentó utilizar el algoritmo BSB (Blocked sort-based) para la construcción del índice. Algo de esto se puede ver en la rama dev donde llegamos a construir el índice dividido en varios archivos. Sin embargo, tuvimos problemas en el proceso de merge. 


## Ejecución óptima de consultas
Para procesar las consultas en lenguaje natural se tuvo que parsear el texto ingresado por el usuario usando la misma función `parse()` utilizada durante la construcción del índice.

## Aplicación web
Para visualizar los resultados implementamos una pequeña aplicación web usando [Flask](https://flask.palletsprojects.com/en/2.0.x/#) para el servidor y [Angular](https://angular.io/) para el front. A continuación se muestra la interfaz.
![](src/img/interface-ss.png "Interfaz de usuario")

## Prueba de uso
Se adjunta el siguiente video que muestra la funcionalidad de la aplicación.

## Conclusión

## Anexos
- Descripción de los campos en los registros del conjunto de datos

Atributo | Definición
------------ | -------------
id | Identificador único
title | Título de la publicación
publication | Diario en el que fue publicado
author | Autor que redacto el artículo
date | Fecha de publicación
year | Año de publicación
month | Mes de publicación
url | URL del artículo (no disponible para todos)
content | Contenido del artículo
