class Picture:
    def __init__(self, width, height, framecol, desc):
        self.Width = width
        self.Height = height
        self.FrameColor = framecol
        self.Description = desc
    
    def getWidth(self):
        return self.Width
    def getHeight(self):
        return self.Height
    def getFrameColor(self):
        return self.FrameColor
    def getDescription(self):
        return self.Description
    def setDescription(self, desc):
        self.Description = desc


arr = [
    Picture(0,0,"black","") for i in range(100)
]

def ReadData():

    pictureData = [
    ]

    picture = []

    with open("Pictures.txt", "r") as f:
        counter = 0
        for line in f:

            if counter%4 == 0 and counter != 0:
                pictureData.append(Picture(int(picture[1]), int(picture[2]), picture[3], picture[0]))
                picture = []
            picture.append(line.strip())
            counter+=1

        pictureData.append(Picture(int(picture[1]), int(picture[2]), picture[3], picture[0]))

    return pictureData

data = ReadData()
w = int(input("Enter width: "))
h = int(input("Enter height: "))
fc = input("Enter frame color: ")

flag = False
for pic in data:
    if pic.getWidth() <= w and pic.getHeight() <= h and pic.getFrameColor().lower() == fc.lower():
        print("Match found! " + pic.getDescription())
        flag = not flag

if not flag:
    print("No matches found.")
    


