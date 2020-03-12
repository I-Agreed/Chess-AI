from PIL import Image
from PIL.ImageTk import PhotoImage
import os
def getImage(piece,colour):
    a = {"p":"pawn",
         "b":"bishop",
         "r":"rook",
         "kn":"knight",
         "ki":"king",
         "q":"queen"}
    b = a[piece]
    c = "sprites/"+colour+"_"+b+".png"
    image = Image.open(c)
    image = image.resize((90,90))
    tkImage = PhotoImage(image)
    return tkImage
    