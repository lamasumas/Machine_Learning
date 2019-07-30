
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
import random

def generateImage():
    futureImageArray = np.zeros((28,28))

    for i in range(4):
        for j in range(4):
            if random.randint(0,2) == 1:
                futureImageArray[(i*7)-1:((i-1)*7)+1:-1,(j*7)-1:((j-1)*7)+1:-1] = 255

    return futureImageArray


def saveImage(theArrayToSave):
    