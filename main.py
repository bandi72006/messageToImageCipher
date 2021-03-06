from PIL import Image

#Creates list with all ASCII characters
chars = []
for i in range(255):
    chars.append(chr(i))

mode = int(input("Enter mode:  \n 0 = create, 1 = decipher \n"))

if mode == 0: #Create
    x = 0
    y = 0
    message = input("Enter message:   ")
    image = Image.new("RGB", (10,10), color = (32,32,32))
    image.save("image/696d616765546f436f6e766572740a.png")

    image = Image.open("image/696d616765546f436f6e766572740a.png")
    picture = image.load()

    RGBTuple = []
    for char in message:
        if len(RGBTuple) == 3:
            RGBTuple = tuple(RGBTuple)
            picture[x,y] = RGBTuple
            RGBTuple = []
            x += 1
            if (x >= 10):
                x = 0
                y += 1
            if (y >= 10):
                print("Error: message too long")
                break

        RGBTuple.append(chars.index(char))
    
    #Adds last character, even if it's not complete
    for i in range(3-len(RGBTuple)):
        RGBTuple.append(0)
    RGBTuple = tuple(RGBTuple)
    picture[x,y] = RGBTuple
    RGBTuple = [] 

    image.save("image/696d616765546f436f6e766572740a.png")

elif mode == 1: #Decipher
    image = Image.open("image/696d616765546f436f6e766572740a.png")
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