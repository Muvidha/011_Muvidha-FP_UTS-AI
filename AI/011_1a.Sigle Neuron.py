#Nama   : Muvidha Fatmawati Putri
#NIM    : 21091397011
#Kelas  : A2021 MI
#1a. single neuron (menggunakan numpy)

#set numpy
import numpy as np

#set variabel dengan input 10
inputs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

#panjang weights = panjang input, dan jumlah weights = jumlah neuron
weights = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

#jumlah bias = jumlah neuron
bias = 12
#print output
output = np.dot(weights, inputs) + bias

#output
print(output)