
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

def Kernel_RBF(X,Y,g):
        n = X.shape[0]
        m = Y.shape[0]
        K = np.zeros((n,m))
        for i in range(n):
                for j in range(m):
                        dif = np.linalg.norm(X[i,:]-Y[j,:])
                        K[i,j] = np.exp(-dif**2/g)
        return K

        
## Read the data
data_train = np.loadtxt("myData_train.txt")
label_train = np.loadtxt("myLabel_train.txt")

data_test = np.loadtxt("myData_test.txt")
label_test = np.loadtxt("myLabel_test.txt")

data_test_individual = np.loadtxt("onlyOne.txt")
label_test_individual = int(np.loadtxt("onlyOneLabel.txt"))

C = 1
n = data_train.shape[0]
m = data_test.shape[0]
I = np.identity(n)

D = 100
sigma = 100

a = 1
b = 3
number_of_posibilities = 5

H = data_train // 255
H_test = data_test // 255
H_individual = data_test_individual // 255

labels = np.zeros((n, number_of_posibilities))

for i in range(n):
        labels[i,int(label_train[i])] = 1
"""
## If you want to use the polinomial kernel, just uncomment this block of code
## And comment the RBF kernel block of code

kernel_polinomial = lambda X,Y:  (np.dot(X,Y.T) + a)**b

Omega = kernel_polinomial(H,H)
W = np.linalg.solve((I/C) + Omega, labels)

Omega_test = kernel_polinomial(H_test, H)
labels_from_test = np.dot(Omega_test, W)


# Percentage of right predictions
predicted_class = labels_from_test.argmax(axis=1)
accuracy_percentage = np.sum(predicted_class == label_test)/float(m)*100.
print ('Accuracy = %.1f%%' % accuracy_percentage)

Omega_test_individual = kernel_polinomial(H_individual, H)
labels_from_test_individual = np.dot(Omega_test_individual, W)

print("The program thinks that there are " + str(labels_from_test_individual.argmax()))
print("Actually the real answer is " + str(label_test_individual))

"""

## If you want to use the RBF kernel, just uncomment this block of code
## And comment the Polinomial kernel block of code

Omega = Kernel_RBF(H,H, sigma)
W = np.linalg.solve((I/D) + Omega, labels)

Omega_test = Kernel_RBF(H_test, H, sigma)
labels_from_test = np.dot(Omega_test, W)


# Percentage of right predictions
predicted_class = labels_from_test.argmax(axis=1)
accuracy_percentage = np.sum(predicted_class == label_test)/float(m)*100.
print ('Accuracy = %.1f%%' % accuracy_percentage)

Omega_test_individual = Kernel_RBF(H_individual.reshape(1,784), H,sigma)
labels_from_test_individual = np.dot(Omega_test_individual, W)

print("The program thinks that there are " + str(labels_from_test_individual.argmax()))
print("Actually the real answer is " + str(label_test_individual))
