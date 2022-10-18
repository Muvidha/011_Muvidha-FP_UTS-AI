#Nama   : Muvidha Fatmawati Putri
#NIM    : 21091397011
#Kelas  : A2021 MI
#1b. multi neuron (menggunakan numpy)

#inisialisasi numpy
import numpy as np

#inisialisasi variabel dengan jumlah input 10
inputs = [6.0, 2.0, 11.0, 12.0, 8.0, 9.0, 1.0, 7.0, 18.0, 14.0]

#panjang weights sesuai dengan panjang input, dan jumlah weights sesuai dengan jumlah neuron
weights = [[0.6, 0.8, 0.4, 0.2, 0.3, 0.5, 0.7, 0.1, 0.0, -0.8],
           [1.0, 11.00, 0.22, 3.2, 1.2, 8.3, 5.4, 1.49, 5.79, 3.29],
           [0.64, 7.6, 3.7, 0.26, 8.24, -0.30, -0.38, 0.56, 0.34, -3.1],
           [1.89, 9.29, 0.24, 3.3, 6.2, 4.50, 9.23, 7.7, 0.35, 0.32],
           [9.0, 5.3, 0.11, 2.2, -0.63, -0.84, 7.7, -2.1, 0.41, -0.26]]

#jumlah bias sesusai dengan jumlah neuron
biases = [12.2, 20.3, 15.5, 13.0, 10.6]

#output
layer_outputs = np.dot(weights, inputs) + biases

#print output
print(layer_outputs)