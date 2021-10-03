import folium
# A little help: add this code to a folder to open the map after running the code
a = float(input('x coordinate: '))  # Asks for the x coordinate
b = float(input('y coordinate: '))  # Asks for the y coordinate
city = str(input("Place's name: "))  # Asks for the city's name
# The city name won't change anything, just will keep the HTML more organized

# The following command will create the map.
# You should open this map as a browser tab.
# Go to the folder which contains this code and run the code
# After executing, you will see a "newmap.html". Just click on it.
new_map = folium.Map(
    location=[a, b], tiles='Stamen Terrain',
    zoom_start=16
)

# Location - Combination of both coordinates the user provided (a, b)
# Tiles - The "style" of the map. Highly recommend you to look at the documentation for more Tiles.
# Zoom Start - The zoom level after running the code. You can zoom in/out with your mouse's scroll button.
folium.Marker(
    [a, b], popup=f'<i>{city}</i>',
    tooltip='Click here'
).add_to(new_map)

new_map.save(r'.\newmap.html')
