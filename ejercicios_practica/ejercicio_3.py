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
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Alumnos: Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Graficar la función utilizando "scatter"
    # utilizando "x" e "y"

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico

    fig = plt.figure(facecolor='#23425c') # Se crea una figura
    fig.suptitle('Tangente Hiperbólica', c='whitesmoke', fontsize=16, fontweight='bold') # Título superior
    
    ax = fig.add_subplot() # Se crea un subplot
    
    ax.scatter(x, y, color='gold', label='y = tanh(x)', marker='.') # Se realiza el gráfico
    
    ax.axvline(0, color='white') # Eje vertical y = 0 (ordenadas)
    ax.axhline(0, color='white') # Eje horizontal x = 0 (abscisas)
    
    ax.tick_params(axis='x', colors='whitesmoke') # Color de la línea de eje x
    ax.tick_params(axis='y', colors='whitesmoke') # Color de la línea de eje y
    ax.set_xlabel('Eje x', c='whitesmoke', fontweight='bold') # Nombre del eje x
    ax.set_ylabel('Eje y', c='whitesmoke', fontweight='bold') # Nombre del eje y
    ax.set_facecolor('#0e1a25') # Color del fondo del grafico (subplot)
    ax.grid(ls='dashed', c='whitesmoke') # Grilla
    ax.legend() # Leyenda
    
    plt.show() # Muestra el gráfico completo

    print("terminamos")