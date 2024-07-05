

from graficos import Canvas
from time import time, sleep
from random import randint
import math

ANCHO_canvas = 1400
ALTURA_canvas = 800
fps = 1 / 60  # Adjusted for a smoother animation
diametro_cursor = 10
color_indices = 0
mouse_press_time = 0
mouse_press_pos = (0, 0)
planetas = []
trazos=[]

is_mouse_pressed = False

class Planeta:
    def __init__(self, x, y, diametro, color, vel_x, vel_y):
        self.x = x
        self.y = y
        self.diametro = diametro
        self.color = color
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = diametro**4

def remover_planetas(planeta1, planeta2):
    global planetas

    if planeta1 in planetas:
        if planeta1.diametro < planeta2.diametro:
            planeta2.diametro=planeta2.diametro+planeta1.diametro*0.1
            planeta2.mass=planeta2.diametro**4
            planetas.remove(planeta1)

    if planeta2 in planetas:
        if planeta2.diametro < planeta1.diametro:
            planeta1.diametro=planeta1.diametro+planeta2.diametro*0.1
            planeta1.mass = planeta1.diametro**4
            planetas.remove(planeta2)

    if planeta2.diametro == planeta1.diametro:
        planetas.remove(planeta1)

def diametro_planeta(canvas):
    global diametro_cursor
    teclas_press = canvas.key_presses
    if len(teclas_press) != 0:
        if teclas_press[0].keysym == "Left":
            diametro_cursor -= 2
        if teclas_press[0].keysym == "Right":
            diametro_cursor += 2
    if diametro_cursor <= 2:
        diametro_cursor = 2
    if diametro_cursor >= 40:
        diametro_cursor = 40
    return diametro_cursor

def color_planeta(canvas):
    global color_indices
    color_planeta = ["Gainsboro", "OliveDrab4", "lightgreen", "Mediumseagreen", "Pink", "Purple4", "Orange", "Red2",
                     "Coral4", "Springgreen4", "RoyalBlue", "Maroon"]
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
    cursor_color = color_planeta(canvas) if is_mouse_pressed else None

    #canvas.create_line(mouse_x,0,mouse_x,ALTURA_canvas, fill="white", tag="cursor")
    #canvas.create_line(0,mouse_y,ANCHO_canvas,mouse_y, fill="white", tag="cursor")
    if is_mouse_pressed:

        canvas.crear_linea(mouse_press_pos[0], mouse_press_pos[1], mouse_x, mouse_y, tags="linea", width=0.5, fill=color_planeta(canvas))
        canvas.crear_ovalo(mouse_press_pos[0] - diametro_planeta(canvas) / 2,
                           mouse_press_pos[1] - diametro_planeta(canvas) / 2,
                           mouse_press_pos[0] + diametro_planeta(canvas),
                           mouse_press_pos[1] + diametro_planeta(canvas),
                           fill=cursor_color, tags="cursor", width=2)
        canvas.crear_ovalo(mouse_x - 4,
                           mouse_y - 4,
                           mouse_x + 4,
                           mouse_y + 4,
                           fill=cursor_color, tags="cursor", width=1)
        canvas.establecer_color_contorno("cursor", color_planeta(canvas))


        draw_launch_preview(canvas, mouse_press_pos[0], mouse_press_pos[1], mouse_x, mouse_y)
    else:
        canvas.crear_ovalo(mouse_x - diametro_planeta(canvas) / 2,
                           mouse_y - diametro_planeta(canvas) / 2,
                           mouse_x + diametro_planeta(canvas),
                           mouse_y + diametro_planeta(canvas),
                           fill=cursor_color, tags="cursor", width=2)
        canvas.establecer_color_contorno("cursor", color_planeta(canvas))


def crear_planeta(canvas, mouse_x, mouse_y, diametro, color, vel_x, vel_y):
    global planetas
    planeta = Planeta(mouse_x, mouse_y, diametro, color, vel_x, vel_y)
    planetas.append(planeta)
    canvas.crear_ovalo(mouse_x - diametro / 2, mouse_y - diametro / 2,
                       mouse_x + diametro, mouse_y + diametro,
                       fill=color, tags="planeta", width=0.5)



def on_mouse_press(event):
    global mouse_press_time, mouse_press_pos, is_mouse_pressed
    mouse_press_time = time()
    mouse_press_pos = (event.x, event.y)
    is_mouse_pressed = True


def on_mouse_release(event, canvas):
    global mouse_press_pos, is_mouse_pressed
    mouse_release_time = time()
    mouse_release_pos = (event.x, event.y)
    press_duration = mouse_release_time - mouse_press_time

    dx = mouse_press_pos[0]-mouse_release_pos[0]
    dy = mouse_press_pos[1]-mouse_release_pos[1]
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if press_duration > 0:
        initial_speed = distance / diametro_cursor
        vel_x = (initial_speed * dx / distance*5)
        vel_y = (initial_speed * dy / distance*5)
    else:
        vel_x = vel_y = 0

    crear_planeta(canvas, mouse_press_pos[0], mouse_press_pos[1], diametro_planeta(canvas), color_planeta(canvas), vel_x, vel_y)
    is_mouse_pressed = False


def crear_estrellas(canvas):
    for i in range(300):
        x1 = randint(0, ANCHO_canvas)
        y1 = randint(0, ALTURA_canvas)
        canvas.crear_ovalo(x1, y1, x1 + 2, y1 + 2, fill="White")


def detectar_colisiones():
    global planetas

    for i in range(len(planetas)):
        for j in range(i + 1, len(planetas)):
            planeta1 = planetas[i]
            planeta2 = planetas[j]
            dx = planeta1.x - planeta2.x
            dy = planeta1.y - planeta2.y
            distancia_cuadrada = dx * dx + dy * dy
            radios_sumados = (planeta1.diametro / 2 + planeta2.diametro / 2)
            if distancia_cuadrada < radios_sumados * radios_sumados:
                return (planeta1, planeta2)
    return None

def actualizar_planetas(canvas):
    global planetas

    G = 2

    dt = 0.2

    for i in range(len(planetas)):
        planeta = planetas[i]


        accel_x = 0
        accel_y = 0

        for j in range(len(planetas)):
            if i != j:
                other_planet = planetas[j]


                dx = other_planet.x - planeta.x
                dy = other_planet.y - planeta.y
                dist_sq = dx ** 2 + dy ** 2
                dist = math.sqrt(dist_sq)


                if dist > 1:
                    force_mag = G * (planeta.mass * other_planet.mass) / dist_sq
                    accel_x += force_mag * dx / dist / planeta.mass
                    accel_y += force_mag * dy / dist / planeta.mass





        planeta.vel_x += accel_x * dt
        planeta.vel_y += accel_y * dt


        planeta.x += planeta.vel_x * dt
        planeta.y += planeta.vel_y * dt


        canvas.crear_ovalo(planeta.x - planeta.diametro / 2, planeta.y - planeta.diametro / 2,
                           planeta.x + planeta.diametro, planeta.y + planeta.diametro,
                           fill=planeta.color, tags="planeta", width=0.5)


"""        canvas.crear_ovalo(planeta.x, planeta.y,
                           (planeta.x)+1, (planeta.y)+1,
                           fill=planeta.color, width=0, tags="trazo")
        trazos.append("trazo")"""



def draw_launch_preview(canvas, start_x, start_y, mouse_x, mouse_y):
    dx = start_x - mouse_x
    dy = start_y - mouse_y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance > 0:
        initial_speed = distance / diametro_cursor
        vel_x = (initial_speed * dx / distance*5)
        vel_y = (initial_speed * dy / distance*5)
    else:
        vel_x = vel_y = 0
    preview_planet = Planeta(start_x, start_y, diametro_cursor, "white", vel_x, vel_y)

    G = 2
    dt = 0.2
    num_steps = 700

    path = []
    for i in range(num_steps):
        accel_x = 0
        accel_y = 0
        for planet in planetas:
            dx = planet.x - preview_planet.x
            dy = planet.y - preview_planet.y
            dist_sq = dx ** 2 + dy ** 2
            dist = math.sqrt(dist_sq)

            if dist > 1:
                force_mag = G * (preview_planet.mass * planet.mass) / dist_sq
                accel_x += force_mag * dx / dist / preview_planet.mass
                accel_y += force_mag * dy / dist / preview_planet.mass


        preview_planet.vel_x += accel_x * dt
        preview_planet.vel_y += accel_y * dt

        preview_planet.x += preview_planet.vel_x * dt
        preview_planet.y += preview_planet.vel_y * dt

        path.append((preview_planet.x, preview_planet.y))


    for i in range(1, len(path)):
        canvas.crear_linea(path[i-1][0], path[i-1][1], path[i][0], path[i][1], tags="launch_preview", fill=color_planeta(canvas), dash=1)






def cuerpo(canvas):
    canvas.configure(cursor="none")
    canvas.establecer_color_fondo_lienzo("gray3")
    global x,y
    crear_estrellas(canvas)
    canvas.bind("<ButtonPress-1>", on_mouse_press)
    canvas.bind("<ButtonRelease-1>", lambda event: on_mouse_release(event, canvas))

    while True:
        collision_pair = detectar_colisiones()
        if collision_pair:
            planeta1, planeta2 = collision_pair
            remover_planetas(planeta1, planeta2)
        canvas.delete("planeta")
        canvas.delete("cursor")
        canvas.delete("linea")
        canvas.delete("launch_preview")
        cursor(canvas)
        actualizar_planetas(canvas)
        canvas.update()
        canvas.delete("cursor")
        sleep(fps)



def main():
    global canvas
    canvas = Canvas(ANCHO_canvas, ALTURA_canvas)  # PREPARACION
    cuerpo(canvas)
    canvas.mainloop()



if __name__ == "__main__":
    main()
