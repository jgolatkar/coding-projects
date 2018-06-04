#!/usr/bin/env python3

import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
names = list(data["NAME"])

# marker color as per elevation
def color_generator(elev):
	if elev < 1000:
		return 'green'
	elif 1000 <= elev < 3000:
		return 'orange'
	else:
		return 'red'

# default map setup
map = folium.Map(location=[39.099,-94.57],zoom_start=5)
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")
# placing circular markers
for lt,ln,el,nm in zip(lat,lon,elev,names):
	fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6,
	popup = folium.Popup(nm+" "+str(el)+" m",parse_html=True),
 	color = color_generator(el),fill=True,fill_color = color_generator(el),
	fill_opacity = 0.7))
# adding GeoJson Layer
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20000000
else 'yellow' if 20000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('web_map.html')

