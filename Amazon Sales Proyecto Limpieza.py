# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 23:39:08 2025

@author: sergi
"""

import pandas as pd

# =============================================================================
# 1) Carga de datos
# =============================================================================
# Cargamos el Excel en un DataFrame para poder explorarlo, limpiarlo y analizarlo.
sales_data = pd.read_excel('sales_data.xlsx')


# =============================================================================
#Exploración
# =============================================================================

# nº de filas/columnas, memoria, tipos y nulos por columna.
sales_data.info()

#  nos orientan sobre rangos y posibles outliers.
sales_data.describe()

# Nombres de columnas para verificar que coinciden con lo esperado por el negocio.
print(sales_data.columns)

# Muestra inicial para validar que la lectura fue correcta y el formato es el esperado.
print(sales_data.head())

# Tipos de datos: importante para decidir conversiones y prevenir errores en agregaciones.
print(sales_data.dtypes)


# =============================================================================
#Limpieza de datos
# =============================================================================


# Conteo de valores faltantes por columnaa
print(sales_data.isnull().sum())

# Observamos que "account" y "currency" tienen muchos nulos, pero pueden ser informativos;
# en cambio, "Amount" es crítico para análisis financieros (sumas/promedios).
# Decidimos ELIMINAR solo filas con Amount nulo porque:
# - Sin Amount no podemos calcular ventas totales/medias.
# - Evitamos propagar NaN en agregaciones y mantener métricas consistentes.
sales_data_clean = sales_data.dropna(subset=['Amount'])

# Verificamos nuevamente la calidad tras la limpieza para confirmar el efecto.
print(sales_data_clean.isnull().sum())


# =============================================================================
#  Filtrado de datos
# =============================================================================


# Filas cuya categoría es "Top": ejemplo de segmentación por atributo de negocio.
category_data = sales_data_clean[sales_data_clean['Category'] == 'Top']
print(category_data)

# Ventas con Amount > 1000: ejemplo de umbral para analizar tickets altos.
high_amount_data = sales_data_clean[sales_data_clean['Amount'] > 1000]
print(high_amount_data)

# Filtros compuestos: sirven para estudiar combinaciones relevantes (p. ej. campañas o packs).
filtered_data = sales_data_clean[
    (sales_data_clean['Category'] == 'Top') & (sales_data_clean['Qty'] == 3)
]


# =============================================================================
#  Agregaciones
# =============================================================================


# Ventas totales por categoría: prioriza categorías según contribución a ingresos.
category_totals = sales_data_clean.groupby('Category', as_index=False)['Amount'].sum()
category_totals = category_totals.sort_values('Amount', ascending=False)

# Promedio de Amount por Categoría y tipo de cumplimiento (Fulfilment):
fulfilment_averages = (
    sales_data_clean
    .groupby(['Category', 'Fulfilment'], as_index=False)['Amount']
    .mean()
    .sort_values('Amount', ascending=False)
)

# Promedio de Amount por Categoría y Estado del pedido (Status):
# identifica en qué estados se concentran tickets más altos/bajos.
status_averages = (
    sales_data_clean
    .groupby(['Category', 'Status'], as_index=False)['Amount']
    .mean()
    .sort_values('Amount', ascending=False)
)

# Ventas totales por Estado de envío y Cumplimiento:
# permite detectar combinaciones logísticas con mayor impacto en ventas.
total_sales_shipandfulfil = (
    sales_data_clean
    .groupby(['Courier Status', 'Fulfilment'], as_index=False)['Amount']
    .sum()
    .sort_values('Amount', ascending=False)
)

# Renombramos "Courier Status" a "Shipment" para una lectura más /estándar en reportes.
total_sales_shipandfulfil.rename(columns={'Courier Status': 'Shipment'}, inplace=True)


# =============================================================================
#  Exportación de resultados
# =============================================================================

# Promedios por categoría y estado del pedido
status_averages.to_excel('average_sales_by_category_and_status.xlsx', index=False)

# Ventas por estado de envío y cumplimiento
total_sales_shipandfulfil.to_excel('total_sales_by_ship_and_fulfil.xlsx', index=False)


















