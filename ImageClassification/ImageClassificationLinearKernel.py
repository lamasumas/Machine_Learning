
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

## Read the data
data_train = np.loadtxt("data_train1.txt")
label_train = np.loadtxt("labels_train1.txt")

data_test = np.loadtxt("data_test1.txt")
label_test = np.loadtxt("labels_test1.txt")

"""
## Testing the characters 
plt.figure(figsize=(8,8))
for k in range(0,100):
    plt.subplot(10,10,k+1)
    ## Each row is a character
    imagen = data_train[k, ]
    ## Each character is 28x28 pixels
    imagen = imagen.reshape(28, 28)
    plt.imshow(imagen, cmap='gray')
    plt.axis('off')
plt.show()
"""
## Parameter  of regularization
c = 1
## Number of classes
number_of_classes = 10 
## Number of rows in data array
n = data_train.shape[0]
## Number of rows in testing array
m = data_test.shape[0]
## Identity array n x n
I = np.identity(n)

## Is in a grey scale so we normalize the data (only 0 and 1)
H = data_train / 255
H_test = data_test / 255

## Array with the labels that we have
labels = np.zeros((n,number_of_classes))

for i in range(n):
    labels[i,int(label_train[i])] = 1

## Linear kernel martrix
Omega = np.dot(H, H.T)

## Weights
W = np.linalg.solve((I/c) + Omega, labels)

Omega_test = np.dot(H_test, H.T)

## Make the predcition
actual_label_test = np.dot(Omega_test, W)
##The biggest value of the array is going to be the actual label
class_predicted = actual_label_test.argmax(axis=1)

guessed_porcentage = np.sum(class_predicted == label_test)/float(m) *100
print ('Guessed percentage = %.1f%%' % guessed_porcentage)
"""
## Show the matrix of prediction beside the actual solution
print('\nLabels predicted for testing samples')
for i in range(0,m):
    if i%10 == 9:
        print(np.argmax(actual_label_test[i])),
    else:
        print(np.argmax(actual_label_test[i]), end=" "),

print('\n')
print('Images corresponding to the above labels')
for k in range(0, 100):
    plt.subplot(10, 10, k+1)
    image = data_test[k, ]
    image = image.reshape(28, 28)
    plt.imshow(image, cmap="gray")
    plt.axis('off')
plt.show()

"""

mytest = Image.open("MyTest.png")
myTestGray = mytest.convert("L")
myTestArray = np.asanyarray(myTestGray)
H_myTest = myTestArray / 255

y = []
for i in H_myTest:
    for j in i:
        y.append(j)
Omega_my_test = np.dot(y, H.T)

## Make the predcition
my_label_test = np.dot(Omega_my_test, W)
print(np.argmax(my_label_test))



