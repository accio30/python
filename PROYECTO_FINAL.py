from graficos import Canvas
from time import sleep
from random import choice, randint
import tkinter as tk
ANCHO_canvas = 1400
ALTURA_canvas = 800
fps= 1/880
diametro_cursor=10
color_indices = 0

def diametro_planeta(canvas):
    global diametro_cursor
    teclas_press= canvas.key_presses
    if len(teclas_press) != 0:
        if teclas_press[0].keysym=="Left":
            diametro_cursor-= 5
        if teclas_press[0].keysym == "Right":
            diametro_cursor += 5
    if diametro_cursor<=0:
        diametro_cursor = 5
    if diametro_cursor>=40:
        diametro_cursor = 40
    return diametro_cursor

def color_planeta(canvas):
    global color_indices
    color_planeta = ["Gainsboro", "OliveDrab4", "lightgreen", "Mediumseagreen", "Pink", "Purple4","Orange", "Red2", "Coral4", "Springgreen4", "RoyalBlue", "Maroon"]
    botones = canvas.obtener_nuevos_clics_boton()
    if len(botones) != 0:
        if botones[0].keysym == "Up":
            color_indices = (color_indices + 1) % len(color_planeta)
        if botones[0].keysym == "Down":
            color_indices = (color_indices - 1) % len(color_planeta)
    return color_planeta[color_indices]

def cursor(canvas):
    mouse_x = canvas.obtener_mouse_x()
    mouse_y = canvas.obtener_mouse_y()
    canvas.crear_ovalo(mouse_x-diametro_planeta(canvas)/2,
    mouse_y-diametro_planeta(canvas)/2,
    mouse_x+diametro_planeta(canvas),
    mouse_y+diametro_planeta(canvas),
    tags="cursor", width=2
    )
    canvas.establecer_color_contorno("cursor", color_planeta(canvas))



def crear_planeta(canvas, mouse_x, mouse_y, diametro, color):
    canvas.crear_ovalo(
        mouse_x - diametro / 2, mouse_y - diametro / 2,
        mouse_x + diametro, mouse_y + diametro,
        fill=color, tags="planeta", width=0
    )
"""    canvas.crear_ovalo(mouse_x - diametro / 2, (mouse_y - diametro / 2)+diametro*0.6,
        mouse_x + diametro, (mouse_y + diametro)-diametro*0.6)
    canvas.crear_ovalo((mouse_x - diametro / 2)+diametro*0.6, (mouse_y - diametro / 2),
        (mouse_x + diametro)-diametro*0.6, (mouse_y + diametro))
    canvas.establecer_color_contorno("planeta", color_planeta(canvas))
"""
    tk.Button(
        bitmap=75)
def cuerpo(canvas):
    for i in range(300):
        x1 = randint(0, ANCHO_canvas)
        y1 = randint(0, ALTURA_canvas)
        canvas.crear_ovalo(x1, y1, x1 + 2, y1 + 2, fill="White")
    while True:
        cursor(canvas)
        clics = canvas.obtener_nuevos_clics_mouse()
        if clics:
            for clic in clics:
                crear_planeta(canvas, clic.x, clic.y,diametro_planeta(canvas), color_planeta(canvas))
        canvas.update()
        canvas.delete("cursor")

def main():

    canvas = Canvas(ANCHO_canvas, ALTURA_canvas) #PREPARACION
    canvas.configure(cursor="none")
    canvas.establecer_color_fondo_lienzo("gray3")
    cuerpo(canvas)

    canvas.mainloop()
if __name__ == "__main__":
    main()