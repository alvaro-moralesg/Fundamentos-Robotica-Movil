import matplotlib.pyplot as plt
import read_reg as rr

## Cargar datos 
t, x, y, o, v, w = rr.read_reg('./log/log.txt')
if ( t == -1):
	print ('Nombre de registro incorrecto.')
	exit()
#############################

## Graficar el camino del robot
fig1, xy = plt.subplots()
xy.set_aspect('equal')
xy.plot(x,y)
xy.set(xlabel='Coordenada x', ylabel='Coordenada y', title='Camino del robot')
#fig1.savefig("./img/robot_teleop_camino.png")
#############################

##  Graficar Pose del robot
fig2, txyo = plt.subplots()
txyo.plot(t, o, color='b', label='Orientacion')
txyo.plot(t, x, color='y', label='Coord. x')
txyo.plot(t, y, color='g', label='Coord. y')
txyo.set(xlabel='Tiempo (seg)', title='Trayectoria del robot')
plt.legend()
#fig2.savefig("./img/robot_teleop_pose.png")
#############################

## Graficar la velocidad del robot
fig3, vw = plt.subplots()
vw.plot(t, v, color='g', label='Veloc. Lineal')
vw.plot(t, w, color='b', label='Veloc. Angular')
vw.set(xlabel='Tiempo (seg)', title='Velocidad Lineal y Angular del robot')
plt.legend()
#fig3.savefig("./img/robot_teleop_velocidad.png")
#############################

plt.show()