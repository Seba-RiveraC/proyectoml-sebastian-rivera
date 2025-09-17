# Proyecto ML: Análisis de Correlación entre PIB y Esperanza de Vida

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

**Análisis de la correlación entre indicadores económicos y la esperanza de vida utilizando un pipeline de datos robusto y reproducible construido con el framework Kedro.**

---

## 📄 Descripción del Proyecto

Este proyecto implementa las primeras fases de la metodología CRISP-DM para investigar la relación entre el Producto Interno Bruto (PIB) de un país y la esperanza de vida de su población.

Utilizando el framework Kedro, se ha construido un pipeline de ingeniería de datos que automatiza el proceso de ingesta, limpieza, integración y transformación de tres fuentes de datos distintas. El resultado es una tabla maestra consolidada, la cual se utiliza para realizar un Análisis Exploratorio de Datos (EDA) en un entorno de Jupyter Notebook integrado, con el fin de descubrir patrones, correlaciones y insights iniciales.


El flujo de trabajo implementado en este proyecto sigue las mejores prácticas de un pipeline de datos:

1.  **Ingesta de Datos:** Se cargan tres datasets distintos (`countries_gdp_hist`, `life-expectancy`, `organizations_gdp_hist`) a través del **Catálogo de Datos** de Kedro, centralizando la configuración.
2.  **Limpieza y Normalización:** Se ejecutan nodos programados en Python para limpiar los nombres de las columnas y normalizar los nombres de las entidades (países y organizaciones) para permitir una futura unión.
3.  **Integración de Datos:** Los datasets de PIB se combinan y luego se unen con el de esperanza de vida utilizando el año y el nombre normalizado del país como claves.
4.  **Salida Final:** El pipeline genera una **tabla maestra** (`master_table.csv`) que contiene todos los datos limpios y consolidados, lista para ser utilizada en la fase de análisis.

Todo este proceso se ejecuta de forma automatizada con un solo comando: `kedro run`.

### Conclusiones del Análisis

El Análisis Exploratorio de Datos (EDA) realizado sobre la tabla maestra reveló una **fuerte correlación positiva** entre el PIB de un país y la esperanza de vida de sus habitantes. Los hallazgos clave son:

* Existe una clara tendencia donde a mayor riqueza de un país, mayor es la esperanza de vida de su población.
* El análisis visual sugiere que el mayor impacto del crecimiento económico en la salud se observa en países de ingresos bajos y medios.
* Esta correlación confirma la viabilidad de utilizar variables económicas para desarrollar futuros modelos de Machine Learning que puedan predecir o estimar la esperanza de vida.
