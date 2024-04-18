import pandas as pd
import numpy as np

# Download renabap dataset

url='https://datosabiertos.desarrollosocial.gob.ar/dataset/0d022767-9390-486a-bff4-ba53b85d730e/resource/9a951270-60dd-4f21-aa19-4ef1205620bd/download/20220131_info_publica.csv'
filename='./relevamiento-villas-y-asentamientos-AR.csv'

import requests 
with open(filename, 'wb') as f:
    resp = requests.get(url, verify=False)
    f.write(resp.content)


df = pd.read_csv(filename, index_col='id_renabap',
                 dtype={"id_renabap": 'int64',
                        "nombre_barrio": 'category',
                        "provincia": 'category',
                        "departamento": 'category',
                        "localidad": 'category',
                        "cantidad_viviendas_aproximadas": 'int64',
                        "cantidad_familias_aproximadas": 'int64',
                        "decada_de_creacion": 'category',
                        "anio_de_creacion": 'Int64',
                        "energia_electrica": 'category',
                        "efluentes_cloacales": 'category',
                        "agua_corriente": 'category',
                        "cocina": 'category',
                        "calefaccion": 'category',
                        "titulo_propiedad": 'category',
                        "clasificacion_barrio": 'category',
                        "superficie_m2": 'int64'})


# Generate tables
# Servicios
servicios = ['energia_electrica', 'calefaccion', 'agua_corriente',
             'efluentes_cloacales', 'cocina']

for nombre_servicio in servicios:
    # Energia electrica
    s = df[[nombre_servicio]].reset_index()
    s.drop(['id_renabap'], axis=1, inplace=True)
    s.drop_duplicates(inplace=True, ignore_index=True)
    # electricidad.drop(['index'], axis=1, inplace=True)
    s.reset_index(drop=True)

    s.index = s.index + 1
    s.index.name = 'id_' + nombre_servicio

    s.reset_index(inplace=True)

    outfile = nombre_servicio + '.csv'
    s.to_csv(outfile, index=False)


# Provincias
provincia = pd.Series(df['provincia'].unique())
provincia.index = provincia.index + 1

provincia.index.name = 'id_provincia'
provincia = provincia.to_frame(name='provincia').reset_index()


provincia.to_csv('provincia.csv', index=False)


departamento = df[['departamento', 'provincia']].reset_index()
departamento.drop(['id_renabap'], axis=1, inplace=True)

departamento.reset_index(inplace=True)
departamento.drop(['index'], axis=1, inplace=True)

# Add id_provincia
df2 = pd.merge(departamento, provincia, on='provincia', how='outer')

# Drop duplicate rows
df3 = df2[['id_provincia', 'departamento', 'provincia']].drop_duplicates().reset_index(drop=True)

# Set index name
df3.index = df3.index + 1
df3.index.name = 'id_departamento'
df3.reset_index(inplace=True)

# Drop provincias column
departamento_table = pd.DataFrame(df3[['id_departamento', 'id_provincia', 'departamento']])
departamento = df3.copy( )

# Save table to 'departamento.csv'
departamento.to_csv('./departamento.csv', index=False)

# Localidad

# Tabla de localidades
# id_localidad   id_departamento   nombre_localidad

# Extract departamento and provincia from dataframe, drop id_denabap
localidad = df[['provincia', 'localidad', 'departamento']].reset_index()
localidad.drop(['id_renabap'], axis=1, inplace=True)

localidad.reset_index(inplace=True)
localidad.drop(['index'], axis=1, inplace=True)

# Add id_provincia
df2 = pd.merge(localidad, departamento, on=['departamento', 'provincia'], how='outer')

# Drop duplicate rows
df3 = df2[['id_departamento', 'localidad', 'departamento']].drop_duplicates().reset_index()

# Set index name
df3.index = df3.index + 1
df3.index.name = 'id_localidad'
df3.reset_index(inplace=True)

# Drop provincias column
localidad_table = pd.DataFrame(df3[['id_localidad', 'id_departamento', 'localidad']])

# Save table to 'departamento.csv'
localidad_table.to_csv('./localidad.csv', index=False)



# Decadas

decada = df['decada_de_creacion'].reset_index()
decada.drop(['id_renabap'], axis=1, inplace=True)
decada.drop_duplicates(inplace=True)
decada.reset_index(inplace=True)
decada = decada.sort_values(by=['decada_de_creacion'])

decada.drop(['index'], axis=1, inplace=True)
decada.reset_index(inplace=True)
decada.index = decada.index +  1
decada.index.name = 'id_decada_creacion'
decada.reset_index(inplace=True)

decada = decada[['id_decada_creacion', 'decada_de_creacion']]

outfile = './decada_de_creacion.csv'

decada.to_csv(outfile, index=False)

# Titulo de propiedad
titulo_de_propiedad = df[['titulo_propiedad']].reset_index()
titulo_de_propiedad.drop(['id_renabap'], axis=1, inplace=True)
titulo_de_propiedad.drop_duplicates(inplace=True)
titulo_de_propiedad.reset_index(inplace=True)

titulo_de_propiedad.drop(['index'], axis=1, inplace=True)
titulo_de_propiedad.reset_index(inplace=True)
titulo_de_propiedad.index = titulo_de_propiedad.index +  1
titulo_de_propiedad.index.name = 'id_titulo_propiedad'
titulo_de_propiedad = titulo_de_propiedad.reset_index()

titulo_de_propiedad = titulo_de_propiedad[['id_titulo_propiedad', 'titulo_propiedad']]

outfile = './titulo_propiedad.csv'

titulo_de_propiedad.to_csv(outfile, index=False)


# Clasificacion de barrio
clasificacion_barrio = df[['clasificacion_barrio']].reset_index()
clasificacion_barrio.drop(['id_renabap'], axis=1, inplace=True)
clasificacion_barrio.drop_duplicates(inplace=True)
clasificacion_barrio.reset_index(inplace=True)
clasificacion_barrio.index = clasificacion_barrio.index + 1
clasificacion_barrio.index.name = 'id_clasificacion_barrio'

clasificacion_barrio.reset_index(inplace=True)


clasificacion_barrio = clasificacion_barrio[['id_clasificacion_barrio', 'clasificacion_barrio']]

outfile = './clasificacion_barrio.csv'

clasificacion_barrio.to_csv(outfile, index=False)

# Tabla de barrios

localidad = pd.read_csv('localidad.csv')
departamento = pd.read_csv('departamento.csv')

decada_de_creacion = pd.read_csv('decada_de_creacion.csv')
energia_electrica = pd.read_csv('energia_electrica.csv')
calefaccion = pd.read_csv('calefaccion.csv')
efluentes_cloacales = pd.read_csv('efluentes_cloacales.csv')
cocina = pd.read_csv('cocina.csv')
agua_corriente = pd.read_csv('agua_corriente.csv')

barrio = df.copy()
barrio.reset_index(inplace=True)


df1 = pd.merge(barrio, energia_electrica, on='energia_electrica', how='outer')
df1.drop_duplicates(inplace=True)
df1.reset_index(inplace=True)
df1.drop('energia_electrica', axis=1 , inplace=True)
df1.reset_index(inplace=True)


df2 = pd.merge(df1, calefaccion, on='calefaccion', how='outer')
df2.drop_duplicates(inplace=True)
# df2.reset_index(inplace=True)
df2.drop('calefaccion', axis=1, inplace=True)
# df2.reset_index(inplace=True)


df3 = pd.merge(df2, efluentes_cloacales, on='efluentes_cloacales', how='outer')
df3.drop_duplicates(inplace=True)
# df3.reset_index(inplace=True)
df3.drop('efluentes_cloacales', axis=1, inplace=True)
# df3.reset_index(inplace=True)

df4 = pd.merge(df3, cocina, on='cocina', how='outer')
df4.drop_duplicates(inplace=True)
# df4.reset_index(inplace=True)
df4.drop('cocina', axis=1, inplace=True)
# df4.reset_index(inplace=True)

df5 = pd.merge(df4, agua_corriente, on='agua_corriente', how='outer')
df5.drop_duplicates(inplace=True)
# df5.reset_index(inplace=True)
df5.drop('agua_corriente', axis=1, inplace=True)
# df5.reset_index(inplace=True)

df6 = pd.merge(df5, clasificacion_barrio, on='clasificacion_barrio', how='outer')
df6.drop_duplicates(inplace=True)
# df6.reset_index(inplace=True)
df6.drop('clasificacion_barrio', axis=1, inplace=True)
# df6.reset_index(inplace=True)


df7 = pd.merge(df6, titulo_de_propiedad, on='titulo_propiedad', how='outer')
df7.drop_duplicates(inplace=True)
# df7.reset_index(inplace=True)
df7.drop('titulo_propiedad', axis=1, inplace=True)
# df7.reset_index(inplace=True)


df8 = pd.merge(df7, decada_de_creacion, on='decada_de_creacion', how='outer')
df8.drop_duplicates(inplace=True)
# df8.reset_index(inplace=True)
df8.drop('decada_de_creacion', axis=1, inplace=True)
# df8.reset_index(inplace=True)



cols_barrio = ['id_renabap', 'id_localidad', 'id_decada_creacion',
               'id_energia_electrica', 'id_efluentes_cloacales',
               'id_agua_corriente', 'id_cocina', 'id_calefaccion',
               'id_clasificacion_barrio', 'id_titulo_propiedad',
               'nombre_barrio', 'cantidad_viviendas_aproximadas' ]


df9 = pd.merge(df8, provincia, on='provincia', how='outer')
df9.drop_duplicates(inplace=True)

#df9.drop(['index', 'level_0'], axis=1, inplace=True)


df10 = pd.merge(df9, departamento, on=['id_provincia', 'departamento'], how='outer')
df10.drop_duplicates(inplace=True)
# df10.drop('departamento_y', axis=1, inplace=True)
# df10.rename(columns={'departamento_x': 'departamento'}, inplace=True)
# df10 = pd.merge(df10, departamento, on='departamento', how='outer')
# df10.drop_duplicates(inplace=True)

df11 = pd.merge(df10, localidad, on=['id_departamento', 'localidad'], how='outer')
df11.drop_duplicates(inplace=True)

df11.drop(['provincia_x', 'index', 'level_0', 'anio_de_creacion',  'provincia_y', 'localidad'], axis=1, inplace=True)

df11.to_csv('barrio.csv', index=False)
