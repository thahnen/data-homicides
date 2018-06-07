from gmplot import gmplot


#####################################################################
#									  								#
#	Map the crimes to different maps (for every state of the US)	#
#									  								#
#####################################################################


# Middle of the US (from Wikipedia, they've even got an own article about it!)
gmap = gmplot.GoogleMapPlotter(39.50, -98.35, 4)

# Put all coordinates from the file in a list
coords = []

with open("./homicide-data.csv") as file:
	for line in file:
		data = [ line.split(",")[9], line.split(",")[10] ]

		# Every browser refuses to load so many (~52.000) Google Maps Markers, restrict with limit (50000 works miserbale with a lot loading time)!
		if len(coords) < 100000 and ("" not in data and "lat" not in data and "lon" not in data):
			data = [ float(data[0]), float(data[1]) ]
			coords.append(data)

# Put all elements with markers on map
lat, lon = zip(*coords)
gmap.scatter(lat, lon, "cornflowerblue", size=40, marker=True)

# Draw map to HTML file
gmap.draw("index.html")
