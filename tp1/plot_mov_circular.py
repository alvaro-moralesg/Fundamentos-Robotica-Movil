import matplotlib.pyplot as plt
import read_reg as rr
import numpy as np 

## Grafica el sentido de avance 

def sentido_avance (x, y):                                                 
    tamaño = np.size(x)
    divisiones = int(tamaño/5)
    arrw_width = (np.max(x) - np.min(x)) * 0.005
    print(divisiones, ' ', np.size(x))
    plt.arrow(x[0],y[0], x[1]-x[0],y[1]-y[0], width=arrw_width, color='g')
    plt.arrow(x[tamaño-1],y[tamaño-1], x[tamaño-1]-x[tamaño-2],y[tamaño-1]-y[tamaño-2], width=arrw_width, color='r')
    for i in range(1,5):
        plt.arrow(x[i*divisiones],y[i*divisiones], x[1+i*divisiones]-x[i*divisiones],y[1+i*divisiones]-y[i*divisiones], width=arrw_width, color='k')
    
reg_name = ''
while (reg_name != 'q'): 

    ## Carga de registros
    reg_name= input('Nombre de registro a cargar: ')
    if  reg_name != 'q' :
        flag_open, t, x, y, o = rr.read_reg('./log/' + reg_name + '.txt')
    else: 
        break
    #######################

    ## Grafica de registros
    if flag_open == False:
        fig, gr = plt.subplots()
        gr.plot(x, y)
        gr.set(title='Camino de '+reg_name, xlabel='Coord. X', ylabel='Coord. Y')
        sentido_avance(x,y)
        plt.show()
    #######################