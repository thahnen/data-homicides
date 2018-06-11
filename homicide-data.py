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

		# Every browser takes ages to load all (~52000) markers!
		if ("" not in data and "lat" not in data and "lon" not in data):
			data = [ float(data[0]), float(data[1]) ]
			coords.append(data)

# Put all elements with markers on map
lat, lon = zip(*coords)
gmap.scatter(lat, lon, "cornflowerblue", size=40, marker=True)

# Draw map to HTML file
gmap.draw("index.html")

# Edit Map for making it smaller, easier to load in Browser
editet_map = []
img_added = False

with open("index.html") as file:
	for line in file:
		# Test for lines
		if "<" in line:
			# Line must be part of HTML
			editet_map.append(line)
		elif "var latlng" in line:
			added = "(new google.maps.Marker({" + \
						"title: ''," + \
						"icon: img," + \
						"position:" + (line.split("=")[1]).split(";")[0] + \
				"})).setMap(map);\n"
			editet_map.append(added)
		elif "var img" in line:
			if img_added == False:
				for elem in editet_map:
					if "var map" in elem:
						editet_map[editet_map.index(elem)] = elem + line
						img_added = True
		elif line == "\n" or \
			("var marker" in line) or \
			("title: " in line) or \
			("icon: " in line) or \
			("position: " in line) or \
			("});" in line) or \
			("marker." in line):
			pass
		else:
			editet_map.append(line)

file = open("index_gen.html", "w+")
for elem in editet_map:
	file.write(elem)
file.close()
