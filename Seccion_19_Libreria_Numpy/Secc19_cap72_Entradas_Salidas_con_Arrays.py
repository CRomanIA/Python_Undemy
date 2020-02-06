#Entradas y salidas de Arrays

import numpy as np

array1 = np.arange(6)
print(array1)
#Para guardar un array
np.save('array1s',array1)
print("La carga del primer array: ",np.load('array1s.npy'))

array2 = np.arange(8)
print(array2)
#Para guardar más de un array
np.savez('arrays',x=array1,y=array2)

array_recuperado = np.load('arrays.npz')

print(array_recuperado['x'])
print(array_recuperado['y'])

np.savetxt('mificheroarray.txt', array2,delimiter=',')
print(np.loadtxt('mificheroarray.txt', delimiter=','))