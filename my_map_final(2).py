import folium
import pandas
data = pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
home_map = folium.Map(location =[26.653363, 85.220949],zoom_start =6 ,tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")

def color_producer(elev):
    if elev < 1000:
        return "green"
    elif elev < 2000:
        return "blue"
    else:
        return "red"
    

for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup= str(el)+" m", fill_color = color_producer(el), color = 'grey',opacity    = 0.7))
fgp = folium.FeatureGroup(name="Population")    
fgp.add_child(folium.GeoJson(data = open("115 world.json", encoding ='utf-8-sig').read(), style_function =lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
home_map.add_child(fgp)
home_map.add_child(fgv)
home_map.add_child(folium.LayerControl())

home_map.save("my_home_map.html")