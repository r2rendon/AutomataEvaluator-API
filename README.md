Índice
======

[Introducción y Explicación del Proyecto
3](#introducción-y-explicación-del-proyecto)

[Composición de tecnologías utilizadas
3](#composición-de-tecnologías-utilizadas)

[Python y Módulos Pip utilizados 3](#python-y-módulos-pip-utilizados)

[Tecnologías además de Python 4](#tecnologías-además-de-python)

[Clases para la implementación de Autómatas
5](#clases-para-la-implementación-de-autómatas)

[Listado de Clases 5](#listado-de-clases)

[Composición de cada clase en la herencia
5](#composición-de-cada-clase-en-la-herencia)

[Implementaciones con enfoque a Orientación de Objetos
10](#implementaciones-con-enfoque-a-orientación-de-objetos)

[Estructura Funcional 10](#estructura-funcional)

[Composición del Front-End 11](#composición-del-front-end)

[Composición del Back-End 12](#composición-del-back-end)

[Base de Datos 12](#base-de-datos)

[Pruebas 12](#pruebas)

Introducción y Explicación del Proyecto
=======================================

Este documento presenta la explicación del primer proyecto de la clase
de Teoría de la Computación. Este documento y proyecto es presentado y
hecho por el estudiante Arturo José Rendon Chinchilla con el número de
cuenta 21741183.

El proyecto consiste en crear un programa capaz de poder crear 3 tipos
de Autómatas que son los siguientes:

-   DFA (Autómata Finito Determinístico)

-   ENFA (Autómata Épsilon Finito No-Determinístico)

-   Expresiones Regulares

Aparte de poder crear dichos tipos de Autómatas, el programa es capaz de
poder representarlos en alguna gráfica, evaluar una palabra en base a un
autómata de uno de los tipos anteriormente mencionados y poder crear la
equivalencia de esos autómatas. (Equivalencia se refiere a poder
transformar, por así decirlo, un ENFA a un DFA o una Expresión Regular
hasta llegar a un DFA, como ejemplos.)

El proyecto realizado por el estudiante esta compuesto por una
arquitectura hecha en base al Desarrollo Web, esto refiriéndose a que
tiene un Front-end, Back-end y una Base de Datos para guardar data de
los autómatas.

Composición de tecnologías utilizadas
=====================================

El proyecto fue desarrollado en el lenguaje de programación Python.
Python es un lenguaje de programación interpretado que es reconocido por
la legibilidad de su código, corta curva de aprendizaje de sintaxis y
por su gran poder y eficiencia en distintos contextos y procesos. Aparte
de Python, el proyecto utiliza tecnologías, que luego serán enlistadas,
como Flask, Angular, Firebase y entre otras. A continuación, se
presentarán las tecnologías utilizadas en este proyecto.

Python y Módulos Pip utilizados
-------------------------------

Pip es un sistema que administra paquetes para Python. Para lograr
sacarle mayor provecho a Python, se utilizaron una lista de módulos pip:

-   **Flask:** Flask es un micro-web framework escrito en Python. Es
    conocido así ya que no requiere de herramientas o librerías
    particulares. Flask fue utilizado para desarrollar al API que envía
    los datos al Cliente.

-   **Flask PyMongo:** Este módulo es una librería que permite una fácil
    conexión de un proyecto hecho en Flask a una base de datos hecha en
    MongoDB. También incluye una amplia interfaz para encontrar e
    ingresar datos y poder administrar la base de datos desde el API.

-   **Load_Dotenv:** Esta pequeña librería es utilizada para un archivo
    .env donde se encuentra información privada pero necesaria para el
    ambiente del API.

-   **Networkx:** Esta librería es utilizada para poder diseñar y
    agregar los estados y aristas a un grafico visible de los autómatas
    creados en el proyecto.

-   **Matplotlib:** Matplotlib es una librería para poder visualizar la
    grafica creada con Networkx y luego poder exportarla como un archivo
    PNG y subirlo a un storage en Firebase.

-   **Flask_CORS:** Esta librería permite una fácil adición de CORS a un
    proyecto hecho con Flask. Brinda ciertas opciones, pero la adición
    es de una línea de código (Aparte de la importación de esta).

-   **Pyrebase:** Pyrebase es utilizada para poder conectarse al
    proyecto en Firebase desde una aplicación hecha en Python. En este
    proyecto solo se hizo uso del Firebase Storage para poder guardar
    las fotos de los gráficos.

Tecnologías además de Python
----------------------------

Como el proyecto esta hecho con un enfoque al Desarrollo Web, se hizo
uso de otras tecnologías para poder representar o aportar al API hecho
en Python. A continuación, se enlistarán dichas tecnologías:

-   **Angular:** Angular es un SPA (Single Page Application) Framework
    basado en Typescript para poder crear un cliente altamente dinámico,
    potente y eficiente. Angular es la base del Front-End de dicho
    proyecto y es donde se representa el API hecho en Python.

-   **Bootstrap:** Bootstrap es una librería de CSS para poder diseñar
    una página de forma dinámica. El Cliente usa Bootstrap para poder
    brindar los estilos necesarios para una buena interfaz visual.

-   **MongoDB:** Como base de datos del proyecto se utilizo la base de
    datos No-SQL MongoDB. Esta fue escogida por su fácil implementación
    y visualización de datos ya que los documentos de Mongo son en JSON
    (JavaScript Object Notation). Al igual brinda Schemas opcionales. El
    proyecto hace uso de MongoDB Atlas que es la versión "On Cloud" de
    MongoDB.

-   **Mongo Compass:** Se hizo uso de esta aplicación hecha por MongoDB
    para poder visualizar los datos en la base de datos que se encuentra
    en la nube.

-   **Postman:** Postman es una aplicación que se utilizo para probar
    los endpoints del API previamente a ser implementados o incluidos en
    el Cliente.

Clases para la implementación de Autómatas
==========================================

Para poder brindar un esquema o un fácil uso y manejo de los Autómatas,
se utilizan clases para poder tener métodos de evaluación y de
equivalencia de los distintos tipos de Autómatas. A continuación, se
enlistará el listado de clases utilizadas:

Listado de Clases
-----------------

-   Autómata (Clase Padre)

-   DFA (Clase Hija de Autómata)

-   NFA (Clase Hija de Autómata)

-   ENFA (Clase Hija de Autómata)

Composición de cada clase en la herencia
----------------------------------------

-   **Definición de constructores**

    -   El constructor de la super clase recibe los datos necesarios de
        un autómata. De parámetros recibe el objeto de la base de datos,
        los estados de aceptación y las transiciones. Esto es ya que es
        necesario cambiar el formato de los estados de aceptación y
        transiciones para que sean utilizados correctamente en Python
        que son los siguientes:

        -   Alfabeto

        -   Estados

        -   Estado Inicial

        -   Estados de aceptación

        -   Transiciones

![](media/image2.png){width="5.166666666666667in" height="1.34375in"}

-   **Métodos:** Los métodos serán enlistados según la clase que se esté
    enlistando:

    -   **Autómata**

        -   La clase Autómata brinda únicamente el método "evaluate" el
            cual se hace override en cada de las clases hijas según el
            uso necesario.

    -   **DFA**

        -   La clase DFA hace un override el método "evaluate". En el
            caso de DFA, **evaluate** hace la evaluación de la expresión
            que se recibe en los parámetros para ver si es aceptada en
            un DFA.

![](media/image3.png){width="6.5in" height="2.7777777777777777in"}

-   ![](media/image4.png){width="6.5in"
    height="3.8152777777777778in"}**NFA:** Cabe destacar que NFA es
    utilizada únicamente cuando se realiza la equivalencia de ENFA a
    DFA. El método **evaluate** realiza dicha equivalencia. Para poder
    realizar dichas equivalencias se crearon los siguientes métodos:
    **getDFAEquivalence(), getAcceptingStates(states)** y
    **getCleanStates(states)**

    -   **getDFAEquivalence():** Este metodo recorre a partir del estado
        inicial todos los estados necesarios a partir del estado inicial
        en base a las letras del alfabeto para poder encontrar los
        estados del DFA y las transiciones de la misma. Este metodo
        devuelve una tupla de dichos elementos encontrados.

![](media/image5.png){width="6.5in" height="3.7in"}

-   **getAcceptingStates(states):** Este método recibe los estados
    sacados en la función anterior para poder encontrar los nuevos
    estados de aceptación tomando en cuenta los estados de aceptación
    del NFA.

![](media/image6.png){width="4.8125in" height="1.7916666666666667in"}

-   **getCleanStates(states):** Este método limpia los estados
    encontrados en **getDFAEquivalence()** ya que ese método devuelve
    los nuevos estados del DFA donde cada elemento de los estados del
    autómata es un arreglo.

![](media/image7.png){width="3.7916666666666665in"
height="2.0520833333333335in"}

-   ![](media/image8.png){width="5.833333333333333in"
    height="5.458333333333333in"}**ENFA:** Para evaluar un ENFA se hace
    la equivalencia hasta encontrar un DFA equivalente. Con esto ya
    presente, **evaluate** es un override para poder sacar un NFA
    equivalente. Para poder realizar dicha equivalencia, **evaluate**
    hace uso de los siguientes métodos: **getNextState(state,
    aElement)** y **getEpsilonEnclosure(state)**:

    -   **getNextState(state, aElement):** Este metodo recibe el estado
        en la iteracion de estados en **evaluate** y el elemento del
        alfabeto en la otra iteracion en **evaluate** para poder sacar
        el proceso con Cerradura Épsilon de un ENFA por cada estado.
        Saca la Cerradura Épsilon del estado, luego procede a encontrar
        a donde va el elemento de la cerradura en base a la letra del
        alfabeto y después vuelve a sacar la cerradura épsilon.

![](media/image9.png){width="6.5in" height="3.3270833333333334in"}

-   **getEpsilonEnclosure(state):** Este método es utilizado en el
    método enlistado anteriormente. Esta función realiza la cerradura
    épsilon en base al estado dado.

![](media/image10.png){width="6.5in" height="2.297222222222222in"}

Implementaciones con enfoque a Orientación de Objetos
-----------------------------------------------------

Se utiliza una herencia donde la clase padre es Autómata y los distintos
tipos de Autómatas son sus hijas. Se hace override del método
**evaluate** a la hora de querer evaluar el autómata en base al tipo del
Autómata.

Estructura Funcional
====================

![](media/image11.png){width="6.5in" height="3.1215277777777777in"}

Composición del Front-End
-------------------------

El Front-End está compuesto por un dashboard, un componente por cada
tipo de autómata, un componente de creación de autómatas y un componente
de detalle donde se detalla cualquier autómata y se evalúa el autómata
en el detalle.

![](media/image12.png){width="2.8958333333333335in"
height="6.239583333333333in"}

Composición del Back-End
------------------------

El API usa Flask como Web Framework. El API tiene los siguientes
endpoints

-   **/automatas \[GET\]**

-   **/automatas/\<type\> \[GET\]** (Encontrar los automatas según el
    tipo)

-   **/automata/\<id\> \[GET\]**

-   **/automatas/\<evalType\>/\<automataID\>/\<expression\> \[GET\]**
    (Evaluar un automata. Se envía el tipo del automata, el id del mismo
    y la expression a evaluar.)

-   **/automata \[POST\]**

El API tiene una conexión con una Base de Datos de MongoDB Atlas (En la
nube) y otra conexión con un Proyecto de Firebase para utilizar el
Storage a la hora de subir los gráficos para tenerlos en un storage en
la nube.

Base de Datos
-------------

MongoDB es la base de datos utilizada en el proyecto. La estructura
básica del Schema utilizado en la colección "Automata" es la siguiente:

![](media/image13.png){width="2.6974792213473315in"
height="1.5616983814523184in"}

Pruebas
=======

Para probar los distintos tipos de automatas se realizaron un total 15
pruebas para poder revisar la funcionalidad del API y de la
implementación de los automatas. La documentación de dichas pruebas
puede ser encontrada en el siguiente link:

-   <https://documenter.getpostman.com/view/8884890/TVCdznyh>

Anexos
======

![](media/image14.png){width="6.5in" height="3.2534722222222223in"}

![](media/image15.png){width="6.5in" height="3.2534722222222223in"}

![](media/image16.png){width="6.5in" height="3.2875in"}

![](media/image17.png){width="6.5in" height="3.270138888888889in"}

![](media/image18.png){width="6.5in" height="3.2944444444444443in"}

![](media/image19.png){width="6.5in" height="3.308333333333333in"}

![](media/image20.png){width="6.5in" height="3.2958333333333334in"}

![](media/image21.png){width="6.5in" height="5.092361111111111in"}
