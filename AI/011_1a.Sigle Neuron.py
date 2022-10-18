#Nama   : Muvidha Fatmawati Putri
#NIM    : 21091397011
#Kelas  : A2021 MI
#1a. single neuron (menggunakan numpy)

#inisialisasi numpy
import numpy as np

#inisialisasi variabel dengan jumlah input 10
inputs = [12, 2, 3, 6, 4, 8, 7, 23, 10, 9]

#panjang weights sesuai dengan panjang input, dan jumlah weights sesuai dengan jumlah neuron
weights = [0.5, 0.12, 0.1, 0.9, 0.89, 0.2, 0.7, 0.8, 0.3, -0.25]

#jumlah bias sesusai dengan jumlah neuron
bias = 12
#output
output = np.dot(weights, inputs) + bias

#print output
print(output)