
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image


## Read the data
data_train = np.loadtxt("myData_train.txt")
label_train = np.loadtxt("myLabel_train.txt")

data_test = np.loadtxt("myData_test.txt")
label_test = np.loadtxt("myLabel_test.txt")

data_test_individual = np.loadtxt("onlyOne.txt")
label_test_individual = int(np.loadtxt("onlyOneLabel.txt"))
"""
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
C = 1
n = data_train.shape[0]
m = data_test.shape[0]
I = np.identity(n)

a = 1
b = 3
number_of_posibilities = 5

H = data_train // 255
H_test = data_test // 255
H_individual = data_test_individual // 255

labels = np.zeros((n, number_of_posibilities))

for i in range(n):
    labels[i, int(label_train[i])] = 1

kernel_polinomial = lambda X,Y :  (np.dot(X,Y.T) + a)**b

Omega = kernel_polinomial(H,H)
W = np.linalg.solve((I/C) + Omega, labels)

Omega_test = kernel_polinomial(H_test, H)
labels_from_test = np.dot(Omega_test, W)


# porcentaje de aciertos
predicted_class = labels_from_test.argmax(axis=1)
accuracy_percentage = np.sum(predicted_class == label_test)/float(m)*100.
print ('Accuracy = %.1f%%' % accuracy_percentage)
"""
from sklearn.metrics import confusion_matrix

mc = confusion_matrix(label_test, predicted_class)

print (u'Matriz de confusión')
print (mc)

plt.figure(figsize=(10,10))
ticks = range(17)
plt.xticks(ticks)
plt.yticks(ticks)
plt.imshow(mc,cmap="Oranges_r",interpolation='nearest')
plt.colorbar(shrink=0.8)
w, h = mc.shape
for i in range(w):
    for j in range(h):
        plt.annotate(str(mc[i][j]), xy=(j, i), 
                    horizontalalignment='center',
                    verticalalignment='center')
plt.xlabel('Etiqueta predicha')
plt.ylabel('Etiqueta')
plt.title(u'Matriz de Confusión')
plt.show()
"""
Omega_test_individual = kernel_polinomial(H_individual, H)
labels_from_test_individual = np.dot(Omega_test_individual, W)

print("The program thinks that there are " + str(labels_from_test_individual.argmax()))
print("Actually the real answer is " + str(label_test_individual))
