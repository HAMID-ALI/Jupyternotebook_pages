import folium
home_map = folium.Map(location =[26.653363, 85.220949],zoom_start =6 ,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[26.653363, 85.220949], popup="Hi I am marker.", icon = folium.Icon(color = "green")))
home_map.add_child(fg)
home_map.save("my_home_map.html")
