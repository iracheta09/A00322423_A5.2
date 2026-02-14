# A00322423_A5.2 – Programming Exercise 2 (Static Analysis)

# Introducción

Esta actividad tuvo como propósito aplicar prácticas de pruebas estáticas y análisis de calidad en el desarrollo de software, mediante la implementación de un programa en Python para el cálculo del costo total de ventas a partir de un catálogo de productos y registros de ventas.

Se utilizaron herramientas de análisis estático como flake8 y pylint para validar el cumplimiento del estándar PEP-8, detectar problemas potenciales en el código y mejorar su calidad antes de la ejecución. Asimismo, se generaron pruebas con distintos conjuntos de datos (TC1, TC2 y TC3) para verificar el correcto funcionamiento del programa y documentar sus resultados.

## Objetivo
Implementar computeSales.py para calcular el costo total de los registros de ventas utilizando un catálogo de precios de productos.
El programa se ejecuta desde la línea de comandos, imprime los resultados en la consola y los exporta a un archivo de resultados.

## Como Ejecutar:
python computeSales.py <priceCatalogue.json> <salesRecord.json>


 Resultados Obtenidos:
## TC1 Total: 2,481.86
## TC2 Total: 166,568.23
## TC3 Total: 165,235.37


 Pruebas Flake8 y Pylint
## @iracheta09 ➜ /workspaces/A00322423_A5.2 (main) $ flake8 computeSales.py
## @iracheta09 ➜ /workspaces/A00322423_A5.2 (main) $ pylint computeSales.py
## ------------------------------------
## Your code has been rated at 10.00/10



## Conclusiones

Las pruebas estáticas permiten identificar errores, inconsistencias y oportunidades de mejora en el código sin necesidad de ejecutarlo, lo que reduce costos y tiempos en etapas posteriores del desarrollo. El uso de herramientas como flake8 y pylint contribuye a mantener estándares de codificación, mejorar la legibilidad y prevenir defectos.

La gestión del código mediante un repositorio y el uso de commits permitió mantener trazabilidad de los cambios y evidenciar el proceso de mejora continua del programa. Además, la ejecución de pruebas con distintos escenarios demostró la importancia de validar el comportamiento del sistema ante diferentes entradas.

En conjunto, esta actividad refuerza la relevancia de las prácticas de calidad temprana, el análisis estático y el control de versiones como elementos fundamentales en el desarrollo profesional de software.