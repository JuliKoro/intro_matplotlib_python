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
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Alumnos: Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    fig = plt.figure(facecolor='#235c5c') # Se crea una figura
    fig.suptitle('Funciones', c='whitesmoke', fontsize=16, fontweight='bold') # Título superior
    
    ax1 = fig.add_subplot(2, 2, 1) # Se crea el subplot para y1=x^2
    ax2 = fig.add_subplot(2, 2, 2) # Se crea el subplot para y2=x^3
    ax3 = fig.add_subplot(2, 2, 3) # Se crea el subplot para y3=x^4
    ax4 = fig.add_subplot(2, 2, 4) # Se crea el subplot para y4=sqr(x)

    # Gráfico y1
    ax1.plot(x, y1, color='gold', label='y = x^2') # Se realiza el gráfico
    
    ax1.axvline(0, color='white') # Eje vertical y = 0 (ordenadas)
    ax1.axhline(0, color='white') # Eje horizontal x = 0 (abscisas)
    
    ax1.tick_params(axis='x', colors='whitesmoke') # Color de la línea de eje x
    ax1.tick_params(axis='y', colors='whitesmoke') # Color de la línea de eje y
    ax1.set_xlabel('Eje x', c='whitesmoke', fontweight='bold') # Nombre del eje x
    ax1.set_ylabel('Eje y', c='whitesmoke', fontweight='bold') # Nombre del eje y
    ax1.set_facecolor('#153737') # Color del fondo del grafico (subplot)
    ax1.set_title('Función Cuadrática de 2do Grado', c='whitesmoke')
    ax1.grid(ls='dashed', c='whitesmoke') # Grilla
    ax1.legend() # Leyenda

    # Gráfico y2
    ax2.plot(x, y2, color='lightsalmon', label='y = x^3') # Se realiza el gráfico
    
    ax2.axvline(0, color='white') # Eje vertical y = 0 (ordenadas)
    ax2.axhline(0, color='white') # Eje horizontal x = 0 (abscisas)
    
    ax2.tick_params(axis='x', colors='whitesmoke') # Color de la línea de eje x
    ax2.tick_params(axis='y', colors='whitesmoke') # Color de la línea de eje y
    ax2.set_xlabel('Eje x', c='whitesmoke', fontweight='bold') # Nombre del eje x
    ax2.set_ylabel('Eje y', c='whitesmoke', fontweight='bold') # Nombre del eje y
    ax2.set_facecolor('#153737') # Color del fondo del grafico (subplot)
    ax2.set_title('Función Cuadrática de 3er Grado', c='whitesmoke')
    ax2.grid(ls='dashed', c='whitesmoke') # Grilla
    ax2.legend() # Leyenda

    # Gráfico y3
    ax3.plot(x, y3, color='lightskyblue', label='y = x^4') # Se realiza el gráfico
    
    ax3.axvline(0, color='white') # Eje vertical y = 0 (ordenadas)
    ax3.axhline(0, color='white') # Eje horizontal x = 0 (abscisas)
    
    ax3.tick_params(axis='x', colors='whitesmoke') # Color de la línea de eje x
    ax3.tick_params(axis='y', colors='whitesmoke') # Color de la línea de eje y
    ax3.set_xlabel('Eje x', c='whitesmoke', fontweight='bold') # Nombre del eje x
    ax3.set_ylabel('Eje y', c='whitesmoke', fontweight='bold') # Nombre del eje y
    ax3.set_facecolor('#153737') # Color del fondo del grafico (subplot)
    ax3.set_title('Función Cuadrática de 4to Grado', c='whitesmoke')
    ax3.grid(ls='dashed', c='whitesmoke') # Grilla
    ax3.legend() # Leyenda
    
    # Gráfico y4
    ax4.plot(x, y3, color='lime', label='y = sqr(x)') # Se realiza el gráfico
    
    ax4.axvline(0, color='white') # Eje vertical y = 0 (ordenadas)
    ax4.axhline(0, color='white') # Eje horizontal x = 0 (abscisas)
    
    ax4.tick_params(axis='x', colors='whitesmoke') # Color de la línea de eje x
    ax4.tick_params(axis='y', colors='whitesmoke') # Color de la línea de eje y
    ax4.set_xlabel('Eje x', c='whitesmoke', fontweight='bold') # Nombre del eje x
    ax4.set_ylabel('Eje y', c='whitesmoke', fontweight='bold') # Nombre del eje y
    ax4.set_facecolor('#153737') # Color del fondo del grafico (subplot)
    ax4.set_title('Función Racional', c='whitesmoke')
    ax4.grid(ls='dashed', c='whitesmoke') # Grilla
    ax4.legend() # Leyenda

    plt.show() # Muestra el gráfico completo
    print("terminamos")