# conda install folium
import folium
from folium.plugins import HeatMap
import json

m = folium.Map(location=[house_prices.latitude.mean(), house_prices.longitude.mean()])
folium.GeoJson('zipcode_king_county.geojson',name='geojson').add_to(m)
HeatMap(data=house_prices[['latitude', 'longitude', 'price_log']].groupby(['latitude', 'longitude']).mean().reset_index().values.tolist(), radius=9, max_zoom=13).add_to(m)
m

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
# como o arquivo geojson e um json, todo seu conteudo sera interpretado como texto. Alem disso e uma variavel categorica. Portanto devemos mudar o tipo da variavel zip para texto.
house_prices.zip = house_prices.zip.astype('str')
print(len(geojson.ZCTA5CE10.unique()), len(house_prices.zip.unique()))

# percorro a lista procurando algum codigo faltante em alguma das listas
print("Está no house_prices, porém não no geojson")
for i in house_prices.zip.unique():
    if i not in geojson.ZCTA5CE10.unique():
        print(i)

print("Está no geojson, porém não no house_prices")
for i in geojson.ZCTA5CE10.unique():
    if i not in house_prices.zip.unique():
        print(i)

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
# quantidade de casas que nao esta no geojson
house_prices.loc[house_prices.zip =='98033','zip'].shape[0]

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##

# Use the groupby method to 
zipcode_data = house_prices.groupby('zip').aggregate(np.mean)
zipcode_data.reset_index(inplace = True)

# load my geojson file which contains my Polygons
boundary_file = "zipcode_king_county.geojson"
with open(boundary_file, 'r') as f:
    zipcode_boundary = json.load(f)

# Initialize Folium Map again (same as before)
m1 = folium.Map(location=[house_prices.latitude.mean(), house_prices.longitude.mean()], zoom_start=10)

# Create choropleth map  
folium.Choropleth(
    geo_data=zipcode_boundary,
    name='choropleth',
    data=zipcode_data,
    columns=['zip', 'price'],
    key_on='feature.properties.ZCTA5CE10',
    fill_color='Spectral',
    fill_opacity=0.6,
    nan_fill_opacity=0,
    line_opacity=1,
    legend_name='Mean Price'
).add_to(m1)

m1

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
# Algumas referências para plotagem de mapas com o folium, incluindo o case do house-prices
# https://levelup.gitconnected.com/visualizing-housing-data-with-folium-maps-4718ed3452c2
# https://github.com/lindsallen/mapping/blob/master/dc_restaurants/dc_choropleth_wtooltip.ipynb


## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##

house_prices.loc[:,"years_since_renovation"] = house_prices.loc[:,"year_built"].max - house_prices.loc[:,"renovation_date"] host_prices.years_since_renovation.hist()
host_prices.years_since_renovation.hist()

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##

house_prices.loc[:,"age"] = house_prices.loc[:,"year_built"].max - house_prices.loc[:,"year_built"]
host_prices.age.hist()

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##

# Criando uma coluna new_cep sem o último dígito do ZIP CODE
house_prices['zip_group'] = house_prices.zip.astype(str).str[:4]

# Como cientista de dados você deverá avaliar em que medida irá continuar explorando suas dúvidas e ideias sobre os dados ou avançar para outros tópicos. Uma boa prática é manter certo controle sobre as ideias/possíveis caminhos e conclusões como fizemos nos exercícios acima.
# Iremos seguir para outras fases do processo para explorar mais dimensões do problema ao invés de detalhar as conclusões ou dúvidas levantadas na fase anterior.
# Um dimensão relevante para olhar na análise exploratória é a correlação entre as variáveis.