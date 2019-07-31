
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image


## Read the data
data_train = np.loadtxt("myData_train.txt")
label_train = np.loadtxt("myLabel_train.txt")

data_test = np.loadtxt("myData_test.txt")
label_test = np.loadtxt("myLabel_test.txt")

C = 1
n = data_train.shape[0]
m = data_test.shape[0]
I = np.identity(n)
a = 1
b = 3
number_of_posibilities = 17

H = data_train / 255
H_test = data_test / 255

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