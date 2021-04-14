import matplotlib.pyplot as plt
import read_reg as rr
import numpy as np 

## Graficar el sentido de avance 
def sentido_avance (x, y):   
    tamaño = np.size(x)                                                                                                                     ## Cantidad de puntos en el registro
    divisiones = int(tamaño/5)                                                                                                              
    arrw_width = (np.max(x) - np.min(x)) * 0.005                                                                                            ## Factor para tamaño de flechas

    plt.arrow(x[0]          , y[0]          , x[1]-x[0]                 , y[1]-y[0]                 , width=arrw_width, color='g')          ## Flecha incial Verde
    plt.arrow(x[tamaño-1]   , y[tamaño-1]   , x[tamaño-1]-x[tamaño-2]   , y[tamaño-1]-y[tamaño-2]   , width=arrw_width, color='r')          ## Flecha final Roja

    for i in range(1,5):
        plt.arrow(x[i*divisiones],y[i*divisiones], x[1+i*divisiones]-x[i*divisiones],y[1+i*divisiones]-y[i*divisiones], width=arrw_width, color='k')    ## Flecha negra para el resto de puntos
######################################    

reg_name = ''
while (reg_name != 'q'): 

    ## Carga de registros
    reg_name= input('Nombre de registro a cargar: ')
    if  reg_name != 'q' :
        t, x, y, o, v, w = rr.read_reg('./log/' + reg_name + '.txt')
    else: 
        break
    ##################################

    ## Grafica de registros
    if t != -1:
        fig, gr = plt.subplots()
        gr.set_aspect('equal')
        gr.plot(x, y)
        gr.set(title='Camino de '+reg_name, xlabel='Coord. X', ylabel='Coord. Y')
        sentido_avance(x,y)
        plt.show()
    ##################################