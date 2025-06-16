-- ✅ 1. Eliminar tablas si ya existen (opcional)
DROP TABLE IF EXISTS ventas;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS productos;

-- ✅ 2. Crear tabla CLIENTES
CREATE TABLE clientes (
    cliente_id INTEGER PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    ciudad VARCHAR(100),
    pais VARCHAR(50)
);

-- ✅ 3. Crear tabla PRODUCTOS
CREATE TABLE productos (
    producto_id INTEGER PRIMARY KEY,
    nombre_producto VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10,2)
);

-- ✅ 4. Crear tabla VENTAS
CREATE TABLE ventas (
    venta_id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    producto_id INTEGER,
    fecha_venta DATE,
    cantidad INTEGER
);

-- ✅ 5. Insertar datos de ejemplo

-- Clientes
INSERT INTO clientes VALUES
(1, 'Carlos Mendoza', 'carlos@example.com', 'Madrid', 'España'),
(2, 'Laura Torres', 'laura@example.com', 'Bogotá', 'Colombia'),
(3, 'Pedro Sánchez', 'pedro@example.com', 'México D.F.', 'México');

-- Productos
INSERT INTO productos VALUES
(101, 'Laptop Pro', 'Electrónica', 1200.00),
(102, 'Smartphone X', 'Móviles', 800.00),
(103, 'Reloj Inteligente', 'Wearables', 250.00);

-- Ventas
INSERT INTO ventas VALUES
(1001, 1, 101, '2024-01-10', 2),
(1002, 2, 102, '2024-01-12', 1),
(1003, 3, 103, '2024-01-15', 3);

-- ✅ 6. Consultas básicas

-- Mostrar todas las ventas
SELECT * FROM ventas;

-- Filtrar por cliente
SELECT * FROM ventas WHERE cliente_id = 2;

-- Ordenar por fecha
SELECT * FROM ventas ORDER BY fecha_venta DESC;

-- ✅ 7. Agregaciones y análisis

-- Total de ventas por cliente
SELECT v.cliente_id, c.nombre, COUNT(*) AS total_ventas
FROM ventas v
JOIN clientes c ON v.cliente_id = c.cliente_id
GROUP BY v.cliente_id, c.nombre
ORDER BY total_ventas DESC;

-- Ingresos totales por producto
SELECT p.nombre_producto, SUM(p.precio * v.cantidad) AS ingreso_total
FROM ventas v
JOIN productos p ON v.producto_id = p.producto_id
GROUP BY p.nombre_producto
ORDER BY ingreso_total DESC;

-- ✅ 8. JOINs entre tablas

-- Detalle de cada venta
SELECT 
    v.venta_id,
    c.nombre AS cliente,
    p.nombre_producto,
    p.precio,
    v.cantidad,
    (p.precio * v.cantidad) AS total
FROM ventas v
JOIN clientes c ON v.cliente_id = c.cliente_id
JOIN productos p ON v.producto_id = p.producto_id;

-- ✅ 9. Subconsultas y CTEs

-- Usando subconsulta para obtener ventas mayores al promedio
SELECT *
FROM (
    SELECT v.venta_id, p.precio * v.cantidad AS monto
    FROM ventas v
    JOIN productos p ON v.producto_id = p.producto_id
) AS ventas_detalle
WHERE monto > (SELECT AVG(precio * cantidad) FROM ventas JOIN productos ON ventas.producto_id = productos.producto_id);

-- Usando CTE
WITH ventas_detalle AS (
    SELECT v.venta_id, p.precio * v.cantidad AS monto
    FROM ventas v
    JOIN productos p ON v.producto_id = p.producto_id
)
SELECT *
FROM ventas_detalle
WHERE monto > (SELECT AVG(monto) FROM ventas_detalle);

-- ✅ 10. Tabla optimizada con sort key y dist key
DROP TABLE IF EXISTS ventas_opt;

CREATE TABLE ventas_opt (
    venta_id INTEGER PRIMARY KEY,
    cliente_id INTEGER DISTKEY,
    producto_id INTEGER,
    fecha_venta DATE SORTKEY,
    cantidad INTEGER
) DISTSTYLE KEY;

-- Copiar datos a la nueva tabla
INSERT INTO ventas_opt
SELECT venta_id, cliente_id, producto_id, fecha_venta, cantidad FROM ventas;

-- ✅ 11. Ejemplo de consulta optimizada
SELECT 
    EXTRACT(MONTH FROM fecha_venta) AS mes,
    COUNT(*) AS total_ventas,
    SUM(p.precio * v.cantidad) AS ingresos_totales
FROM ventas_opt v
JOIN productos p ON v.producto_id = p.producto_id
GROUP BY mes
ORDER BY mes;