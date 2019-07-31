
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
import random

number_of_possible_groups = [0,1,2,3,4]

def generateImage(number_of_groups):
    futureImageArray = np.zeros((28,28))
    counter_iterations = 0
    counter_groups_written = 0
    for i in range(2):
        for j in range(2):
            if number_of_groups - counter_groups_written == 0:
                break
            elif 4 - counter_iterations <= number_of_groups - counter_groups_written :
                futureImageArray[(i*14)-1:((i-1)*14)+1:-1,(j*14)-1:((j-1)*14)+1:-1] = 255
                counter_groups_written += 1
            else:
                if random.randint(0,2) == 1:
                    futureImageArray[(i*14)-1:((i-1)*14)+1:-1,(j*14)-1:((j-1)*14)+1:-1] = 255
                    counter_groups_written += 1

            counter_iterations += 1

    return futureImageArray, number_of_groups

def generateImageTest():
    futureImageArray = np.zeros((28,28))
    number_of_groups = 0
    for i in range(2):
        for j in range(2):
            if random.randint(0,2) == 1:
                futureImageArray[(i*14)-1:((i-1)*14)+1:-1,(j*14)-1:((j-1)*14)+1:-1] = 255
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
    copy_possible_groups = number_of_possible_groups.copy()
    for i in range(16000):
        group_number_selected = copy_possible_groups[random.randint(0, (len(copy_possible_groups)-1))]
        copy_possible_groups.remove(group_number_selected)
        if len(copy_possible_groups) == 0:
            copy_possible_groups = number_of_possible_groups.copy()
        currentPicture, currentLabel = generateImage(group_number_selected)
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
    currentPicture, currentLabel = generateImageTest()
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
        currentPicture, currentLabel = generateImageTest()
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
    generateTestFiles()
    generateTrainFiles()