# **Selección de Visualizaciones y Generación de Hallazgos**

**Objetivo:**  
Selecciona tres tipos de visualizaciones apropiadas para diferentes escenarios utilizando el *DataViz Cheat Sheet* de DataCamp, y justifica cada elección con base en el propósito del análisis. Luego, genera *hallazgos clave* que podrían derivarse de cada visualización.


#### 📌 **Instrucciones:**
1. Lee los tres escenarios presentados.
2. Para cada escenario, **elige un tipo de gráfico** de la lista proporcionada en el artículo.
3. **Justifica tu elección** según el objetivo del análisis (tendencia, relación, distribución, parte-todo, flujo, etc.).
4. Describe **dos hallazgos potenciales (findings)** que podrías obtener al analizar esa visualización.


### 🔹 **Escenario 1: Evolución de ventas mensuales por región (2023-2024)**

Una empresa desea analizar cómo han evolucionado sus ventas totales durante los últimos 24 meses, comparando tres regiones: Norte, Centro y Sur. El equipo de análisis tiene datos mensuales detallados.

#### Dataset: Ventas mensuales por región (Últimos 6 meses)

| Mes        | Región Norte (USD) | Región Centro (USD) | Región Sur (USD) |
|------------|--------------------|---------------------|------------------|
| Ene 2024   | 15,000             | 18,000              | 20,000           |
| Feb 2024   | 16,500             | 17,800              | 19,500           |
| Mar 2024   | 18,000             | 18,200              | 18,000           |
| Abr 2024   | 17,500             | 19,000              | 17,000           |
| May 2024   | 19,000             | 19,500              | 16,500           |
| Jun 2024   | 21,000             | 20,000              | 15,000           |

### 🔹 **Escenario 2: Distribución del tiempo dedicado a actividades diarias por perfil de empleado**

Un estudio interno recolectó datos sobre cuántas horas al día dedican los empleados (por categoría: administrativo, técnico, gerencial) a cinco actividades: reuniones, correo, trabajo operativo, capacitación y descanso. Se busca entender cómo se distribuye su jornada laboral.


### Dataset: Horas promedio por actividad y perfil (por día)

| Perfil       | Reuniones | Correo | Trabajo Operativo | Capacitación | Descanso |
|--------------|---------|--------|-------------------|--------------|----------|
| Administrativo | 2.0     | 1.5    | 3.0               | 0.5          | 1.0      |
| Técnico        | 1.0     | 1.0    | 4.5               | 0.5          | 1.0      |
| Gerencial      | 3.5     | 1.0    | 2.0               | 1.0          | 0.5      |

### 🔹 **Escenario 3: Relación entre inversión en marketing, número de leads y tamaño del mercado por país**

Una empresa multinacional quiere explorar si existe una correlación entre su inversión en marketing digital (USD), el número de leads generados y el tamaño del mercado (PIB per cápita) en 15 países.

### Dataset: Marketing por país

| País       | Inversión Marketing (USD miles) | Leads Generados | PIB per cápita (miles USD) |
|-----------|-------------------------------|------------------|----------------------------|
| México    | 50                            | 1,200            | 15                         |
| Brasil    | 80                            | 1,800            | 12                         |
| Canadá    | 120                           | 2,000            | 50                         |
| España    | 60                            | 1,600            | 30                         |
| India     | 30                            | 900              | 8                          |
| Singapur  | 90                            | 2,200            | 65                         |