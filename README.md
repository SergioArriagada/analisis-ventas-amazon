 Sales Data Analysis with Python and Pandas

Este proyecto implementa un flujo completo de análisis de datos de ventas utilizando **Python y Pandas**.  
El objetivo es limpiar, explorar y generar insights a partir de un dataset de ventas.

---

## Pasos realizados

1. **Exploración de datos**
   - Carga del dataset `sales_data.xlsx`.
   - Revisión de columnas, tipos de datos y valores iniciales con `.info()`, `.describe()` y `.head()`.

2. **Limpieza de datos**
   - Detección de valores nulos.
   - Eliminación de registros con `Amount` faltante.
   - Verificación de calidad de los datos limpios.

3. **Filtrado y segmentación**
   - Ventas de categoría *Top*.
   - Ventas con `Amount > 1000`.
   - Filtros con múltiples condiciones (ejemplo: categoría *Top* y cantidad = 3).

4. **Agregaciones**
   - Ventas totales por categoría.
   - Promedio de montos por categoría y cumplimiento.
   - Promedio de montos por categoría y estatus.
   - Ventas totales por estado de envío y cumplimiento.

5. **Exportación de resultados**
   - Generación de archivos Excel:
     - `average_sales_by_category_and_status.xlsx`
     - `total_sales_by_ship_and_fulfil.xlsx`

## ecnologías utilizadas
- Python
- Pandas
- Spyder
- Excel
