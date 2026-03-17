import pandas as pd
import streamlit as st
import plotly.express as px

#********* CARGA DE LOS DATOS *********
ruta = 'https://github.com/juliandariogiraldoocampo/ia_taltech/raw/refs/heads/main/aeropuerto/operaciones_aereas_acumuladas.csv'
df = pd.read_csv(ruta)

df = pd.read_csv(ruta)

#** ANÁLISIS Y PROCESAMIENTO **
df_tipo_vuelo = df['TIPO_VUELO'].value_counts().reset_index()
estadisticos = df_tipo_vuelo['count'].describe()
maximo = estadisticos["max"]
minimo = estadisticos["min"]
media = estadisticos["mean"]

#CONFIGUARACIÓN DE LA PÁGINA

st.set_page_config(
    page_title="Operaciones Acumuladas",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ajuste del ancho maximo del contenedor principal a 1200 px 
st.markdown(
    '''
    <style>
        .block-container {
            max-width: 1200px;
        }
    </style>           
    ''',
    unsafe_allow_html=True
)

paleta_barras = px.colors.qualitative.Antique


st.image("avion.png")

#** VISUALIZACIÓN DE LOS DATOS **
st.title('Datos Operaciones')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Máximo", f"{maximo:.0f}", border=True)
with col2:
    st.metric("Mínimo", f"{minimo:.0f}", border=True)
with col3:
    st.metric("Medio", f"{media:.0f}", border=True)


st.subheader("Máximo")
st.write(maximo)
st.subheader("Mínimo")
st.text(minimo)
st.subheader("Media")
st.text(media)

st.metric("Máximo", f"{maximo:.0f}", border=True)
st.metric("Mínimo", f"{minimo:.0f}", border=True)
st.metric("Medio", f"{media:.0f}", border=True)

with st.expander("Datos_Operaciones"):
    st.dataframe(df)


##################################################################
#################### ANÁLISIS Y PROCESAMIENTO#####################
##################################################################

#ESTADISTICOS DE LA COLUMNA "TIPO_VUELO""

df_tipo_vuelo = df["TIPO_VUELO"].value_counts().reset_index()
df_tipo_vuelo.columns = ["TIPO_VUELO","count"]
estadisticos = df_tipo_vuelo["count"].describe()
maximo = estadisticos["max"]
minimo = estadisticos["min"]
media = estadisticos["mean"]

# TOP 5 AEROPUERTOS CON MAYOR NÚMERO DE OPERACIONES
df_top5_ops_aeropuerto = df['AEROPUERTO_OPERACION'].value_counts().reset_index().head(5)
df_top5_ops_aeropuerto.columns = ['AEROPUERTO_OPERACION', 'count']

# TOP 10 RUTAS CON MAYOR NÚMERO DE OPERACIONES
df['RUTA'] = df['ORIGEN'] + ' ▶ ' + df['DESTINO']
df_top10_rutas = df['RUTA'].value_counts().reset_index().head(10)
df_top10_rutas.columns = ['RUTA', 'CANTIDAD']

#*** VISUALIZACION DE LOS DATOS ***
st.title('Datos Operaciones')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Mínimo', f'{minimo:.0f}', border=True)
with col2:
    st.metric('Media', f'{media:.0f}', border=True)
with col3:
    st.metric('Máximo', f'{maximo:.0f}', border=True)

with st.expander("Ver Matriz de Datos"):
    st.dataframe(df)

with st.expander("Top 5 Aeropuertos con Mayor Número de Operaciones"):
    st.dataframe(df_top5_ops_aeropuerto)

# ANÁLISIS DE LOS AEROPUERTOS CON MAYOR NUMERO DE OPERACIONES 

st.dataframe(df_top5_ops_aeropuerto)
fig_barras = px.bar(
    df_top5_ops_aeropuerto,
    x="AEROPUERTO_OPERACION",
    y="count",

    title="Top 5 Aeropuertos con mayor numero de operaciones",
    labels={
        "AEROPUERTO_OPERACION": "Aeropuerto",
        "count": "Número de Operaciones"
        },
    color= "AEROPUERTO_OPERACION",
    color_discrete_sequence=paleta_barras
)
fig_barras.update_layout(showlegend=False)

#MOSTRAR LA GRAFICA DE BARRAS

st.plotly_chart(fig_barras, use_container_width=True)

## ANALISIS DE RUTAS

fig_rutas = px.bar (
    df_top10_rutas,
    x="RUTA",
    y="CANTIDAD",
    title="C",
    color= "CANTIDAD",
    color_continuous_scale="turbid"

)

fig_rutas.update_coloraxes(showscale=False)

#mostrar la grafica 

st.plotly_chart(fig_rutas, use_container_width=True)


df_top10_rutas = df_top10_rutas.sort_values("CANTIDAD",ascending=True)
