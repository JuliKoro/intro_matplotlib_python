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

    # NOTA: aproveche los ejemplos de "line_plot" de clase

    # Alumnos: Se desea graficar los valores de "x" e "y" en un gráfico de línea

    # Función que se desea graficar:
    # y = x**2

    x = list(range(-10, 11, 1))

    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)

    # Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "y" en función de "x"

    # Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    # Crear acá su gráfico

    fig = plt.figure(facecolor='slategray') # Se crea una figura
    fig.suptitle('Función Cuadrática', c='whitesmoke', fontsize=16, fontweight='bold') # Título superior
    ax = fig.add_subplot() # Se crea un subplot
    ax.plot(x, y, color='springgreen', label='y = x^2') # Se realiza el gráfico
    ax.tick_params(axis='x', colors='whitesmoke') # Color de la línea de eje x
    ax.tick_params(axis='y', colors='whitesmoke') # Color de la línea de eje y
    ax.set_title('y = x^2', c='whitesmoke') # Título al subplot
    ax.set_xlabel('Eje x', c='whitesmoke', fontweight='bold') # Nombre del eje x
    ax.set_ylabel('Eje y', c='whitesmoke', fontweight='bold') # Nombre del eje y
    ax.set_facecolor('darkslategray') # Color del fondo del grafico (subplot)
    ax.grid(ls='dashed', c='whitesmoke') # Grilla
    ax.legend() # Leyenda
    plt.show() # Muestra el gráfico completo

    print("terminamos")