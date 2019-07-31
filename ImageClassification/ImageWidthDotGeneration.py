
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
import random

def generateImage():
    futureImageArray = np.zeros((28,28))
    number_of_groups = 0
    for i in range(4):
        for j in range(4):
            if random.randint(0,2) == 1:
                futureImageArray[(i*7)-1:((i-1)*7)+1:-1,(j*7)-1:((j-1)*7)+1:-1] = 255
                number_of_groups += 1

    return futureImageArray, number_of_groups


def saveImagePng(thePicture):
    theImage = Image.fromarray(thePicture)
    theImage = theImage.convert("L")
    theImage.save("GroupClassificationSpecificTest.jpeg")

def saveImage(allPictures, theArrayToSave):
    tempArray = [] 
    for i in theArrayToSave:
        for j in i:
            tempArray.append(j)
    allPictures.append(tempArray)    

def generateTrainFiles():
    allPictures = []
    allLabels = []
    for i in range(900):
        currentPicture, currentLabel = generateImage()
        saveImage(allPictures,currentPicture)
        allLabels.append(currentLabel)
    
    dataToSave = open("myData_train.txt", "a")
    labelsToSave = open("myLabel_train.txt", "a")
    for index in range(len(allPictures)):
        for i in allPictures[index]:
            dataToSave.write(str(int(i))+" ")
        dataToSave.write("\n")
        labelsToSave.write(str(allLabels[index]) +"\n")
        
    
    dataToSave.close()
    labelsToSave.close()

def generateOnePictureAndLabel():
    thePicture = []
   
    currentPicture, currentLabel = generateImage()
    saveImage(thePicture,currentPicture)
    saveImagePng(currentPicture)
    dataToSave = open("onlyOne.txt", "a")
    labelsToSave = open("onlyOneLabel.txt", "a")
    for index in range(len(thePicture)):
        for i in thePicture[index]:
            dataToSave.write(str(int(i))+" ")
        dataToSave.write("\n")
        labelsToSave.write(str(currentLabel) +"\n")
        
    
    dataToSave.close()
    labelsToSave.close()
   
def generateTestFiles():
    allPictures = []
    allLabels = []
    for i in range(100):
        currentPicture, currentLabel = generateImage()
        saveImage(allPictures,currentPicture)
        allLabels.append(currentLabel)
    
    dataToSave = open("myData_test.txt", "a")
    labelsToSave = open("myLabel_test.txt", "a")
    for index in range(len(allPictures)):
        for i in allPictures[index]:
            dataToSave.write(str(int(i))+" ")
        dataToSave.write("\n")
        labelsToSave.write(str(allLabels[index]) +"\n")
        
    
    dataToSave.close()
    labelsToSave.close()
   
if __name__ =="__main__":
    generateOnePictureAndLabel()