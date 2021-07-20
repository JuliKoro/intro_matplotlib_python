# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Alumno: Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)
    
    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico

    fig = plt.figure(facecolor='#4d4d4d') # Se crea una figura
    fig.suptitle('Funciones Cuadráticas', c='whitesmoke', fontsize=16, fontweight='bold') # Título superior
    
    ax = fig.add_subplot() # Se crea un subplot
    
    ax.plot(x, y1, color='chartreuse', label='y = x^2') # Se realiza el gráfico 1
    ax.plot(x, y2, color='coral', label='y = x^3') # Se realiza el gráfico 2
    
    ax.axvline(0, color='white') # Eje vertical y = 0 (ordenadas)
    ax.axhline(0, color='white') # Eje horizontal x = 0 (abscisas)
    
    ax.tick_params(axis='x', colors='whitesmoke') # Color de la línea de eje x
    ax.tick_params(axis='y', colors='whitesmoke') # Color de la línea de eje y
    ax.set_xlabel('Eje x', c='whitesmoke', fontweight='bold') # Nombre del eje x
    ax.set_ylabel('Eje y', c='whitesmoke', fontweight='bold') # Nombre del eje y
    ax.set_facecolor('#1a1a1a') # Color del fondo del grafico (subplot)
    ax.grid(ls='dashed', c='whitesmoke') # Grilla
    ax.legend() # Leyenda
    
    plt.show() # Muestra el gráfico completo

    print("terminamos")