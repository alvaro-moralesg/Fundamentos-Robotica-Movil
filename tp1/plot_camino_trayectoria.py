import matplotlib.pyplot as plt
import numpy as np

with open('./log/log.txt','r') as fd:
	t = []
	x = []
	y = []
	o = []
	for line in fd:
		line_striped = line.strip()
		elements = line_striped.split()
		t.append(float(elements[0]))
		x.append(float(elements[1]))
		y.append(float(elements[2]))
		o.append(float(elements[3]))

## Graficos

fig, ct = plt.subplots(2)
ct[0].plot(x,y)
ct[0].set(title='Camino')
ct[1].plot(t,x, color='g', label='Coord. X')
ct[1].plot(t,y, color='b', label='Coord. Y')
ct[1].plot(t,o, color='r', label='Orientacion')
ct[1].set(title='Trayectoria')
fig.savefig("./img/camino_trayectoria.png")
plt.legend()
plt.show()

## Marcar puntos
data = [t, x, y, o]
tamaño = np.size(data,1)
divisiones = int(tamaño/9)
print(tamaño,', ',divisiones) 
puntos = []
for i in range(1,10):
	puntos[i] = [x[divisiones*i] for x in data]

print (puntos)
