import matplotlib.pyplot as plt
import read_reg as rr
import numpy as np

## Lectura y carga de registro
reg_name = 'mov_circular_3'
t, x, y, o, v, w = rr.read_reg('./log/'+reg_name+'.txt')
if (t == -1):
	exit()
##############################

## Grafica camino y trayectoria
fig, ct = plt.subplots(1, 2)

ct[0].set_aspect('equal')
ct[0].plot(x,y)
ct[0].set(title='Camino')

ct[1].plot(t,x, color='g', label='Coord. X')
ct[1].plot(t,y, color='b', label='Coord. Y')
ct[1].plot(t,o, color='r', label='Orientacion')
ct[1].set(title='Trayectoria')
plt.legend()

fig.savefig('./img/camino_pose_'+reg_name+'.png')
#############################

## Toma 9 puntos del registro
divisiones = int(np.size(t)/9)
lst_puntos = []
for i in range (1, 10):
	puntos = [t[divisiones*i], x[divisiones*i], y[divisiones*i], o[divisiones*i]]
	lst_puntos.append(puntos)
#############################

## Grafica los puntos
cycle_color=['green','blue','red','cyan','magenta','yellow','gray','orange','black']
for i in range (0,9):
	ct[0].plot(lst_puntos[i][1], lst_puntos[i][2], marker = 'o', color = cycle_color[i])
	ct[1].plot(lst_puntos[i][0], lst_puntos[i][1], marker = 'o', color = cycle_color[i])
	ct[1].plot(lst_puntos[i][0], lst_puntos[i][2], marker = 'o', color = cycle_color[i])
	ct[1].plot(lst_puntos[i][0], lst_puntos[i][3], marker = 'o', color = cycle_color[i])
fig.savefig('./img/camino_pose_'+reg_name+'puntos.png')
plt.show()
#############################