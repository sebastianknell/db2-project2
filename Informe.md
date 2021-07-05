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
El objetivo de este proyecto fue implementar un índice invertido para tareas de búsqueda y recuperación en documentos de texto en base al modelo de recuperación por ranking y probar su desempeño mediante consultas en lenguaje natural. Para ello se construyó una aplicación frontend que interactúa con las principales operaciones del índice invertido: carga e indexación de documentos en tiempo real y búsqueda textual relacionado a ciertos temas de interés. Los resultados de búsqueda se obtienen aplicando la similitud de coseno sobre el índice invertido. Se uso un conjunto de datos de prueba obtenido de [Kaggle](https://www.kaggle.com/datasets). Este conjunto de datos está conformado por artículos de diferentes periódicos, que incluyen New York Times, CNN, Fox News, entre otros. Las publicaciones se encuentran principalmente entre los años 2016 y 2017. De acuerdo a lo aprendido, se espera obtener un alto grado de precisión a la consulta ingresada por el usuario, es decir, del conjunto de documentos recuperados, la mayoría son documentos relevantes para el usuario.

## Implementación
## Construcción del índice invertido
Para implementar el índice invertido se utilizó el modelo de recuperación por ranking. Logramos implementar las principales operaciones solicitadas: carga e indexación de documentos y búsqueda textual. A continuación se muestra la construcción del índice.
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

El método `writeIndex()` lo utilizamos para ...


## Manejo en memoria secundaria



## Ejecución óptima de consultas
Para procesar las consultas en lenguaje natural se tuvo que parsear el texto ingresado por el usuario. La funcion `parse()` realiza esta tarea. 
```python
def parse(text):
    words = word_tokenize(text.lower().strip())
    i = 0
    while i < len(words):
        if words[i] in stoplist:
            words.pop(i)
        else:
            i += 1
    for i in range(len(words)):
        words[i] = stemmer.stem(words[i])
    return words
```

## Prueba de uso
Se adjunta el siguiente video que muestra la funcionalidad de la aplicación.


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
