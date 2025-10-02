import plotly.express as px
import plotly.graph_objects as go

# Cargar los datos limpios del análisis anterior
df = pd.read_csv('https://github.com/ricardoahumada/data-for-auditors/raw/refs/heads/main/3.%20Procesamiento%20de%20Datos%20con%20ETLs/3.4..DataQuality/output/ventas_limpias.csv')

# Convertir fechas al tipo datetime
df['orderdate'] = pd.to_datetime(df['orderdate'])

# Conteo de estados
status_counts = df['status'].value_counts().reset_index()
status_counts.columns = ['status', 'count']

# Gráfico interactivo
fig = px.bar(status_counts, x='status', y='count', title='Distribución de Estados de Pedidos', labels={'count': 'Cantidad', 'status': 'Estado'})
fig.show()