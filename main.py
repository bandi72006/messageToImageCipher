from PIL import Image

image = Image.open("image/696d616765546f436f6e766572740a.jpg")
picture = image.load()

size = image.size

values = []

for j in range(size[1]):
    for i in range(size[0]):
        values.append(picture[i, j])

