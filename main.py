from PIL import Image

#Creates list with all ASCII characters
chars = []
for i in range(255):
    chars.append(chr(i))

mode = int(input("Enter mode:  \n 0 = create, 1 = decipher \n"))

if mode == 0: #Create
    print("Work in progress")

elif mode == 1:
    image = Image.open("image/696d616765546f436f6e766572740a.jpg")
    picture = image.load()

    size = image.size

    values = []

    for j in range(size[1]):
        for i in range(size[0]):
            values.append(picture[i, j])

    message = []
    for colour in values:
        for RGB in colour:
            message.append(chars[RGB])
    
    message = "".join(message)
    print(message)