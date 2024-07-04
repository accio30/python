from graficos import Canvas
from time import time, sleep
from random import randint
import math

ANCHO_canvas = 1400
ALTURA_canvas = 800
fps = 1 / 60  # Adjusted for a smoother animation
diametro_cursor = 5
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
        self.mass = diametro


def diametro_planeta(canvas):
    global diametro_cursor
    teclas_press = canvas.key_presses
    if len(teclas_press) != 0:
        if teclas_press[0].keysym == "Left":
            diametro_cursor -= 0.5
        if teclas_press[0].keysym == "Right":
            diametro_cursor += 0.5
    if diametro_cursor <= 0.5:
        diametro_cursor = 0.5
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
    canvas.crear_ovalo(mouse_x - diametro_planeta(canvas) / 2,
                       mouse_y - diametro_planeta(canvas) / 2,
                       mouse_x + diametro_planeta(canvas),
                       mouse_y + diametro_planeta(canvas),
                       fill=cursor_color, tags="cursor", width=2)
    canvas.establecer_color_contorno("cursor", color_planeta(canvas))
    #canvas.create_line(mouse_x,0,mouse_x,ALTURA_canvas, fill="white", tag="cursor")
    #canvas.create_line(0,mouse_y,ANCHO_canvas,mouse_y, fill="white", tag="cursor")
    if is_mouse_pressed:
        canvas.crear_linea(mouse_press_pos[0], mouse_press_pos[1], mouse_x, mouse_y, tags="linea", width=2, fill=color_planeta(canvas), dash=1)


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
    global mouse_press_time, mouse_press_pos, is_mouse_pressed
    mouse_release_time = time()
    mouse_release_pos = (event.x, event.y)
    press_duration = mouse_release_time - mouse_press_time

    dx = mouse_press_pos[0]-mouse_release_pos[0]
    dy = mouse_press_pos[1]-mouse_release_pos[1]
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if press_duration > 0:
        initial_speed = distance / press_duration / diametro_cursor
        vel_x = (initial_speed * dx / distance)
        vel_y = (initial_speed * dy / distance)
    else:
        vel_x = vel_y = 0

    crear_planeta(canvas, event.x, event.y, diametro_planeta(canvas), color_planeta(canvas), vel_x, vel_y)
    is_mouse_pressed = False


def crear_estrellas(canvas):
    for i in range(300):
        x1 = randint(0, ANCHO_canvas)
        y1 = randint(0, ALTURA_canvas)
        canvas.crear_ovalo(x1, y1, x1 + 2, y1 + 2, fill="White")

def calculate_single_body_acceleration(planetas, body_index):
    G_const = 6.67408e-11  # Gravitational constant in m3 kg-1 s-2
    acceleration_x = 0
    acceleration_y = 0
    target_body = planetas[body_index]

    for index, external_body in enumerate(planetas):
        if index != body_index:
            dx = external_body.x - target_body.x
            dy = external_body.y - target_body.y
            r_squared = dx ** 2 + dy ** 2
            r = math.sqrt(r_squared)

            # Avoid division by zero and handle very close bodies gracefully
            if r_squared > 1e-6:
                acceleration = G_const * external_body.diametro / r_squared
                acceleration_x += acceleration * dx / r
                acceleration_y += acceleration * dy / r

    return acceleration_x, acceleration_y


def compute_velocity(bodies, time_step=1):
    for body_index, target_body in enumerate(bodies):
        acceleration_x, acceleration_y = calculate_single_body_acceleration(bodies, body_index)
        target_body.vel_x += acceleration_x * time_step
        target_body.vel_y += acceleration_y * time_step

def update_location(bodies, time_step=1):
    for target_body in bodies:
        target_body.x += target_body.vel_x * time_step
        target_body.y += target_body.vel_y * time_step







def actualizar_planetas(canvas):
    global planetas
    compute_velocity(planetas)
    update_location(planetas)

    for planeta in planetas:

        acc_x, acc_y = calculate_single_body_acceleration(planetas, planetas.index(planeta))

        planeta.vel_x += acc_x
        planeta.vel_y += acc_y

        planeta.x += planeta.vel_x*0.2
        planeta.y += planeta.vel_y*0.2
        canvas.crear_ovalo(planeta.x - planeta.diametro / 2, planeta.y - planeta.diametro / 2,
                           planeta.x + planeta.diametro, planeta.y + planeta.diametro,
                           fill=planeta.color, tags="planeta", width=0)

        canvas.crear_ovalo(planeta.x, planeta.y,
                           (planeta.x)+1, (planeta.y)+1,
                           fill=planeta.color, width=0, tags="trazo")
        trazos.append("trazo")



        print(len(trazos))



def run_simulation(planetas, time_step=0.1, number_of_steps=10000, report_freq=100):
    # Create output container for each body
    body_locations_hist = []
    for current_body in planetas:
        body_locations_hist.append({"x": [], "y": []})

    for i in range(1, number_of_steps):
        actualizar_planetas(canvas)  # Compute gravitational effects and update positions

        if i % report_freq == 0:
            for index, body_location in enumerate(body_locations_hist):
                body_location["x"].append(planetas[index].x)
                body_location["y"].append(planetas[index].y)

    return body_locations_hist
def cuerpo(canvas):
    crear_estrellas(canvas)
    canvas.bind("<ButtonPress-1>", on_mouse_press)
    canvas.bind("<ButtonRelease-1>", lambda event: on_mouse_release(event, canvas))

    while True:
        canvas.delete("planeta")
        canvas.delete("cursor")
        canvas.delete("linea")
        cursor(canvas)
        actualizar_planetas(canvas)
        canvas.update()
        canvas.delete("cursor")
        run_simulation(planetas)
        sleep(fps)



def main():
    global canvas
    canvas = Canvas(ANCHO_canvas, ALTURA_canvas)  # PREPARACION
    canvas.configure(cursor="none")
    canvas.establecer_color_fondo_lienzo("gray3")
    cuerpo(canvas)
    canvas.mainloop()



if __name__ == "__main__":
    main()
