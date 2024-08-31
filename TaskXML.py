# Create a python program called taskXML.py. Write the code to Read in the movie.xml file.
# Use the iter() function to list all the child tags of the movie element.
# Use the itertext() function to print out the movie descriptions.
# Find the number of movies that are favourites and the number of movies that are not.
#'movie.xml' content below:

import xml.etree.ElementTree as ET
tree = ET.parse('movie.xml')
root = tree.getroot()

for movie in root.iter('movie'):
    print(movie.get('title'))
 