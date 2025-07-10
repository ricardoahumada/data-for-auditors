# Reto: “El error que no vimos venir”

En una empresa líder en servicios corporativos, todo parecía funcionar bien. Los equipos atendían a cientos de clientes cada día, las facturas se generaban automáticamente y los informes mostraban una alta tasa de cobro. Pero algo pasaba desapercibido…

Un día, durante una auditoría rutinaria, se descubrió un error silencioso pero costoso: **un porcentaje significativo de clientes nunca había sido facturado**, a pesar de haber recibido los servicios contratados. No era fraude, ni mala intención. Era un fallo en el proceso de integración entre atención y facturación que, mes tras mes, estaba dejando dinero sobre la mesa.

La empresa no solo perdió ingresos, sino también confianza en sus sistemas internos. La pregunta que quedó en el aire fue:

> _¿Cómo podemos asegurarnos de que esto no vuelva a suceder?_

## Tu Misión:

Como parte del equipo de datos y auditoría, tu desafío es claro:  
**Analizar los procesos actuales, identificar inconsistencias y construir una solución que garantice que todos los clientes atendidos sean correctamente facturados.**

Usarás herramientas modernas de análisis de datos, desde limpieza y visualización hasta machine learning, y crearás un Cuadro de Mando Integral (BSC) que permita monitorear el éxito del proceso en tiempo real.

Este reto no solo te pondrá a prueba como analista…  
Te convertirá en un **protector del valor de los datos** dentro de la organización.

## Objetivo:
Auditar y validar que **todos los clientes atendidos hayan sido correctamente facturados**, identificando inconsistencias, generando insights y proponiendo mejoras a través de un Cuadro de Mando Integral (BSC) y visualización en Power BI.

## ¿Qué vas a hacer?

1. **Extraer datos** de múltiples fuentes.
2. **Limpiar y transformar** información para detectar errores.
3. Realizar un **análisis exploratorio** para encontrar inconsistencias.
4. **Definir un BSC** para medir el desempeño del proceso.
5. Generar un **dashboard interactivo en Power BI**.
6. Aplicar **Machine Learning** para predecir patrones ocultos.
7. Presentar **recomendaciones accionables** basadas en tus hallazgos.


## Secuencia sugerida
### 1. Extraer datos de las fuentes
- Las atención a clientes se guargan en  una base de datos en PostgreSQL, con la siguiente estructura:

```sql
-- Tabla de clientes atendidos
CREATE TABLE clientes_atendidos (
    cliente_id VARCHAR(50),
    nombre_cliente VARCHAR(100),
    fecha_atencion DATE,
    servicio VARCHAR(100)
);
```

- Las facturas emitidas se almacenan en archivos CSV: `facturas_emitidas.csv`

| factura_id | cliente_id | fecha_factura | monto | estado_pago |
|------------|-------------|----------------|--------|---------------|
| F001       | C1001       | 2025-04-01     | 250.00 | Cobrado        |
| F002       | C1003       | 2025-04-01     | 180.00 | Pendiente      |


### 2. Limpiar y transformar los datos
### 3. Análisis exploratorio y detección de inconsistencias
### 4. Definir el Balanced Scorecard (BSC)
### 5. Busca insights gráficamente con Power BI
### 6. Presentar recomendaciones
### 7. Bonus: Realizar un análisis avanzado con ML


## Modo de trabajo y entrega
Serás parte de un equipo de 4 integrantes con compentencias complementarias

Al final del reto deberás subir tu solución en el campus del curso.

## Criterios de evluación
1. Calidad del análisis de datos
2. Diseño y relevancia del Cuadro de Mando Integral (BSC)
3. Calidad del dashboard en Power BI
4. Claridad y fundamento de las recomendaciones
5. Bonus: Aplicación de Machine Learning (KMeans)

