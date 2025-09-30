# **Ejercicio Práctico: Evaluación de Calidad de Datos en un Sistema Contable**  

#### **Contexto:**
La empresa *Comercializadora Solución S.A.* ha implementado un nuevo sistema de facturación. Como parte del proceso de auditoría interna, se requiere evaluar la calidad de los datos registrados en el módulo de ventas del mes de marzo 2024.

Se extrae un subconjunto de 10 registros de facturas (datos anonimizados):

| N° Factura | Fecha       | Cliente ID | Nombre Cliente | Monto (USD) | IVA (19%) | Total (USD) | Estado     |
|------------|-------------|------------|----------------|-------------|-----------|-------------|------------|
| F001       | 2024-03-05  | C101       | Juan Pérez     | 1000        | 190       | 1190        | Pagada     |
| F002       | 2024-03-06  | C102       | María López    | 850         | 161.5     | 1011.5      | Pendiente  |
| F003       | 2024-03-07  | C103       | Ana Gómez      | 1200        | 228       | 1428        | Pagada     |
| F004       | 2024-03-08  | C104       | NULL           | 500         | 95        | 595         | Pagada     |
| F005       | 2024-03-09  | C105       | Luis Torres    | 0           | 0         | 0           | Anulada    |
| F006       | 2024-03-10  | C106       | Pedro Díaz     | 750         | 142.5     | 892.5       | Pendiente  |
| F007       | 2024-03-11  | C107       | Sofía Ruiz     | 900         | 171       | 1071        | Pagada     |
| F008       | 2024-03-12  | C108       | Carlos M.      | -200        | -38       | -238        | Devolución |
| F009       | 2024-03-13  | C109       | Elena P.       | 600         | 114       | 714         | Pendiente  |
| F010       | 2024-02-28  | C110       | Roberto L.     | 400         | 76        | 476         | Pagada     |


### **Tarea para los estudiantes auditores:**

Evalúa la **calidad de los datos** según las siguientes dimensiones:


#### 1. **Completitud (Completeness)**
- ¿Todos los campos obligatorios están llenos?
- Identifica registros con valores faltantes.
- *Ejemplo:* El campo "Nombre Cliente" en F004 tiene valor `NULL`. Esto afecta la trazabilidad y puede indicar problemas de captura.


#### 2. **Precisión (Accuracy)**
- Verifica si los cálculos son correctos (por ejemplo, IVA y Total).
- Comprueba: `Total = Monto + IVA`
- *Ejemplo:* En F005, el monto es 0, pero ¿fue una transacción real o un error? Si está anulada, debería tener un registro de justificación.


#### 3. **Consistencia (Consistency)**
- ¿Los formatos de fecha son uniformes?
- ¿El estado "Anulada" coincide con un monto de 0?
- ¿Las fechas están dentro del período auditado (marzo 2024)?
- *Hallazgo:* La factura F010 tiene fecha **2024-02-28**, fuera del mes de marzo → inconsistencia temporal.


#### 4. **Validez (Validity)**
- ¿Los valores cumplen con reglas de negocio?
- ¿Puede haber montos negativos sin causa justificada?
- *Observación:* F008 tiene monto negativo (-200). Aunque puede ser una devolución, debe estar respaldado por un documento (nota de crédito).


#### 5. **Uniformidad (Uniformity)**
- ¿Los nombres de clientes siguen un formato claro?
- Ejemplo: "Carlos M." y "Elena P." usan iniciales; otros usan nombre completo. Podría dificultar búsquedas.
