#using pygoogle to download images
# create list of the images you need in a text file and you open it up here in this code

from pygoogle_image import image as pi
# opening the text file created
with open("dataset", 'rb') as data:
    for line in data:
        decoded_line = line.decode('utf=-8')

        image = decoded_line.strip()

        pi.download(keywords=image, limit=10)