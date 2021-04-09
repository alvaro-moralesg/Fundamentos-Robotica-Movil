import matplotlib.pyplot as plt

## Cargar datos en una lista de listas
with open('./log/log.txt','r') as fd:
	t = []
	x = []
	y = []
	o = []
	v = []
	w = []
	for line in fd:
		line_stripped = line.strip()
		elements = line_stripped.split()
		t.append(float(elements[0]))
		x.append(float(elements[1]))
		y.append(float(elements[2]))
		o.append(float(elements[3]))
		v.append(float(elements[4]))
		w.append(float(elements[5]))

## Graficar el camino del robot

fig1, xy = plt.subplots()
xy.plot(x,y)
xy.set(xlabel='Coordenada x', ylabel='Coordenada y', title='Camino del robot')
fig1.savefig("./img/camino_robot.png")

##  Graficar la trayectoria del robot

fig2, txyo = plt.subplots()
txyo.plot(t, o, color='b', label='Orientacion')
txyo.plot(t, x, color='y', label='Coord. x')
txyo.plot(t, y, color='g', label='Coord. y')
txyo.set(xlabel='Tiempo (seg)', title='Trayectoria del robot')
fig2.savefig("./img/trayectoria_robot.png")
plt.legend()

## Graficar la velocidad del robot

fig3, vw = plt.subplots()
vw.plot(t, v, color='g', label='Veloc. Lineal')
vw.plot(t, w, color='b', label='Veloc. Angular')
vw.set(xlabel='Tiempo (seg)', title='Velocidad Lineal y Angular del robot')
fig3.savefig("./img/velocidades.png")
plt.legend()

## Plot

plt.show()
