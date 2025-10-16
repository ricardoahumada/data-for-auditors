# DAX
https://support.microsoft.com/es-es/office/tutorial-r%C3%A1pido-aprenda-los-fundamentos-de-dax-en-30-minutos-51744643-c2a5-436a-bdf6-c895762bec1a

## ¿Qué es DAX?

**DAX** es un lenguaje de fórmulas utilizado en **Power BI**, **Power Pivot** y **Analysis Services** para crear cálculos personalizados en modelos de datos tabulares. Permite definir **medidas**, **columnas calculadas** y **tablas calculadas**.


## Conceptos Clave

1. **Medida (Measure):**  
   Cálculo dinámico que se evalúa en el contexto de la visualización (por ejemplo, total de ventas por región).

2. **Columna calculada:**  
   Nueva columna en una tabla que se calcula fila por fila (por ejemplo, margen por producto).

3. **Contexto de evaluación:**  
   - **Contexto de fila:** Se refiere a la fila actual al calcular una columna.
   - **Contexto de filtro:** Filtros aplicados por tablas dinámicas, segmentadores o relaciones.

4. **Funciones de agregación y de contexto:**  
   Esenciales para manipular cómo se calculan los valores.


## Ejemplos con Base de Datos de Ventas

Supongamos que tenemos las siguientes tablas:

- **Ventas**: `IDVenta`, `IDProducto`, `IDCliente`, `Fecha`, `Cantidad`, `PrecioUnitario`
- **Productos**: `IDProducto`, `NombreProducto`, `Categoría`, `Costo`
- **Clientes**: `IDCliente`, `Nombre`, `Región`
- **Calendario**: `Fecha`, `Año`, `Mes`, `Trimestre`


### 1. **Medidas Básicas**

```dax
Total Ventas = SUMX(Ventas, Ventas[Cantidad] * Ventas[PrecioUnitario])
```

> Calcula el total de ventas multiplicando cantidad por precio unitario.

```dax
Total Unidades Vendidas = SUM(Ventas[Cantidad])
```

> Suma total de unidades vendidas.


### 2. **Medidas con Filtros**

```dax
Ventas 2024 = CALCULATE([Total Ventas], Calendario[Año] = 2024)
```

> Ventas totales solo del año 2024.

```dax
Ventas Productos Electrónicos = 
CALCULATE(
    [Total Ventas],
    Productos[Categoría] = "Electrónica"
)
```

> Ventas solo de la categoría "Electrónica".


### 3. **Comparaciones Temporales**

```dax
Ventas Año Anterior = 
CALCULATE(
    [Total Ventas],
    SAMEPERIODLASTYEAR(Calendario[Fecha])
)
```

> Compara ventas con el mismo período del año anterior.

```dax
Crecimiento % = 
DIVIDE([Total Ventas] - [Ventas Año Anterior], [Ventas Año Anterior])
```

> Porcentaje de crecimiento interanual.


### 4. **Ranking y Top N**

```dax
Ranking Ventas por Cliente = 
RANKX(ALL(Clientes), [Total Ventas], , DESC, Dense)
```

> Asigna un ranking a cada cliente según sus ventas totales.


### 5. **Margen y Rentabilidad**

Primero, una **columna calculada** en la tabla `Ventas`:

```dax
Margen Unitario = 
RELATED(Productos[PrecioUnitario]) - RELATED(Productos[Costo])
```

Luego, una **medida**:

```dax
Margen Total = 
SUMX(Ventas, Ventas[Cantidad] * (Ventas[PrecioUnitario] - RELATED(Productos[Costo])))
```

> Calcula el margen total considerando costo y precio.


### 6. **Promedios y Acumulados**

```dax
Promedio Ventas Diarias = AVERAGEX(VALUES(Calendario[Fecha]), [Total Ventas])
```

> Promedio de ventas por día.

```dax
Ventas Acumuladas YTD = TOTALYTD([Total Ventas], Calendario[Fecha])
```

> Ventas acumuladas desde el inicio del año hasta la fecha.


## Consejos

- Usa **`CALCULATE`** para modificar el contexto de filtro.
- **`SUMX`, `AVERAGEX`, `MAXX`**, etc., son funciones iteradoras ideales para cálculos fila por fila.
- Evita usar columnas calculadas cuando puedas usar medidas (mejor rendimiento).
- Asegúrate de tener un **modelo relacional bien definido** (relaciones activas entre tablas).

---
---

# **Ejemplo KPI con DAX**

## Objetivo del KPI  
**Medir qué porcentaje de la meta mensual de ventas se ha alcanzado hasta la fecha.**

> **Fórmula del KPI:**  
> `Cumplimiento de Meta (%) = Ventas Reales / Meta Mensual`


## Estructura de la Base de Datos

Supongamos que tienes las siguientes tablas en tu modelo de Power BI:

### 1. **Ventas**  
| Fecha       | IDVendedor | Monto |
|-------------|------------|-------|
| 2025-01-05  | V01        | 1200  |
| 2025-01-12  | V02        | 900   |
| ...         | ...        | ...   |

### 2. **Metas** *(una meta por vendedor y mes)*  
| IDVendedor | Año | Mes | MetaMensual |
|------------|-----|-----|--------------|
| V01        | 2025| 1   | 10000        |
| V02        | 2025| 1   | 8000         |
| V01        | 2025| 2   | 12000        |
| ...        | ... | ... | ...          |

### 3. **Calendario** *(tabla de fechas, marcada como tabla de fechas en Power BI)*  
| Fecha       | Año | Mes | MesNombre |
|-------------|-----|-----|-----------|
| 2025-01-01  | 2025| 1   | Enero     |
| ...         | ... | ... | ...       |

### Relaciones:
- `Ventas[Fecha]` → `Calendario[Fecha]`
- `Ventas[IDVendedor]` → `Metas[IDVendedor]`
- Además, en la tabla **Metas**, creamos una columna calculada para unir año y mes:

```dax
AñoMes = Metas[Año] * 100 + Metas[Mes]
```

Y en **Calendario**:

```dax
AñoMes = Calendario[Año] * 100 + Calendario[Mes]
```

Luego creamos una relación **inactiva** (o usamos `USERELATIONSHIP` si es necesario) entre `Calendario[AñoMes]` y `Metas[AñoMes]`, o simplemente usamos filtros lógicos en DAX (más flexible).


## **Paso a Paso: Crear un KPI con DAX**

### Paso 1: Crear medida de **Ventas Reales**

```dax
Ventas Reales = SUM(Ventas[Monto])
```

> Esta medida suma todas las ventas en el contexto actual (por ejemplo, por mes, vendedor, etc.).


### Paso 2: Crear medida de **Meta Mensual**

Queremos obtener la meta correspondiente al **mes y año en contexto** y al **vendedor en contexto**.

```dax
Meta Mensual = 
CALCULATE(
    SUM(Metas[MetaMensual]),
    FILTER(
        Metas,
        Metas[IDVendedor] = SELECTEDVALUE(Ventas[IDVendedor]) ||
        ISINSCOPE(Ventas[IDVendedor]) = FALSE()
    ),
    FILTER(
        Metas,
        Metas[Año] = SELECTEDVALUE(Calendario[Año]) &&
        Metas[Mes] = SELECTEDVALUE(Calendario[Mes])
    )
)
```

#### **Alternativa:** (más robusta y eficiente):

Primero, asegúrate de tener una relación **activa** entre `Ventas[IDVendedor]` y `Metas[IDVendedor]`, y luego usa `TREATAS` o filtra por año/mes:

```dax
Meta Mensual = 
VAR AñoActual = SELECTEDVALUE(Calendario[Año])
VAR MesActual = SELECTEDVALUE(Calendario[Mes])
RETURN
CALCULATE(
    SUM(Metas[MetaMensual]),
    Metas[Año] = AñoActual,
    Metas[Mes] = MesActual,
    REMOVEFILTERS(Calendario)  // Evita conflictos de contexto de fecha
)
```

> Esta versión es más limpia y evita errores cuando no hay selección de vendedor.


### Paso 3: Crear el **KPI: % Cumplimiento de Meta**

```dax
% Cumplimiento Meta = 
DIVIDE([Ventas Reales], [Meta Mensual], 0)
```

> `DIVIDE` evita errores de división por cero. Si la meta es 0, devuelve 0.


### Paso 4: Formato y visualización

- Selecciona la medida `% Cumplimiento Meta`.
- En el panel de propiedades, cambia el formato a **Porcentaje** con 1 decimal.
- Usa un **gráfico de tarjeta**, **gráfico de barras** o **tabla** para mostrar:
   - Vendedor
   - Mes
   - Ventas Reales
   - Meta Mensual
   - % Cumplimiento Meta

> *Consejo visual**: Agrega una **línea de referencia** o usa **formato condicional** (por ejemplo, verde si >100%, rojo si <80%).


## Ejemplo de Resultado (Enero 2025)

| Vendedor | Ventas Reales | Meta Mensual | % Cumplimiento |
|----------|----------------|---------------|----------------|
| V01      | $9,200         | $10,000       | 92.0%          |
| V02      | $7,500         | $8,000        | 93.8%          |


## Buenas Prácticas

1. **Evita columnas calculadas innecesarias** → usa medidas.
2. **Usa variables (`VAR`)** para hacer el código más legible y eficiente.
3. **Prueba el KPI en distintos contextos**: por mes, trimestre, región, etc.
4. Si las metas vienen de Excel o una fuente externa, asegúrate de que estén actualizadas.
