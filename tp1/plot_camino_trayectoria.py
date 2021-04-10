import matplotlib.pyplot as plt
import itertools as itt 
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

## Marcar puntos

#tamaño = np.size(t)
divisiones = int(np.size(t)/10)
lst_puntos = []
for i in range (1, 10):
	puntos = [t[divisiones*i], x[divisiones*i], y[divisiones*i], o[divisiones*i]]
	lst_puntos.append(puntos)

cycle_color=['green','blue','red','cyan','magenta','yellow','gray','orange','black']

for i in range (1,10):
	ct[0].plot(lst_puntos[i-1][1], lst_puntos[i-1][2], marker='.', color = cycle_color[i-1])
	ct[1].plot(lst_puntos[i-1][0], lst_puntos[i-1][1], marker = '.', color = cycle_color[i-1])
	ct[1].plot(lst_puntos[i-1][0], lst_puntos[i-1][2], marker = '.', color = cycle_color[i-1])
	ct[1].plot(lst_puntos[i-1][0], lst_puntos[i-1][3], marker = '.', color = cycle_color[i-1])
plt.show()