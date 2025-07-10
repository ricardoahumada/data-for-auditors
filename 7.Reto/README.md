# Reto: “Asegurar que se facturan todos los clientes”

## Objetivo del Caso:
Auditar y validar que **todos los clientes atendidos hayan sido correctamente facturados**, identificando inconsistencias, generando insights y proponiendo mejoras a través de un Cuadro de Mando Integral (BSC) y visualización en Power BI.

## Secuencia sugerida
### 1.Extraer datos de las fuentes
#### Estructura de las tablas en PostgreSQL

```sql
-- Tabla de clientes atendidos
CREATE TABLE clientes_atendidos (
    cliente_id VARCHAR(50),
    nombre_cliente VARCHAR(100),
    fecha_atencion DATE,
    servicio VARCHAR(100)
);

-- Tabla de empleados que registraron la atención
CREATE TABLE empleados (
    empleado_id VARCHAR(50),
    nombre_empleado VARCHAR(100),
    departamento VARCHAR(100)
);
```

#### Archivo CSV – `facturas_emitidas.csv`

| factura_id | cliente_id | fecha_factura | monto | estado_pago |
|------------|-------------|----------------|--------|---------------|
| F001       | C1001       | 2025-04-01     | 250.00 | Cobrado        |
| F002       | C1003       | 2025-04-01     | 180.00 | Pendiente      |


### 2.Limpiar y transformar los datos
### 3.Análisis exploratorio y detección de inconsistencias
### 4. Definir el Balanced Scorecard (BSC)
### 5. Busca insights gráficamente con Power BI
### 6. Presentar recomendaciones
### 7. Bonus: Análisis avanzado con ML


