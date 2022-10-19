#Nama   : Muvidha Fatmawati Putri
#NIM    : 21091397011
#Kelas  : A2021 MI
#1b. multi neuron (menggunakan numpy)

#inisialisasi numpy
import numpy as np

#inisialisasi variabel dengan jumlah input 10
inputs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

#panjang weights sesuai dengan panjang input, dan jumlah weights sesuai dengan jumlah neuron
weights =  [[1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0],
            [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0],
            [3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0],
            [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0],
            [5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0]]

#jumlah bias sesusai dengan jumlah neuron
biases = [2.2, 2.3, 5.5, 1.0, 0.6]

#output
layer_outputs = np.dot(weights, inputs) + biases

#print output
print(layer_outputs)